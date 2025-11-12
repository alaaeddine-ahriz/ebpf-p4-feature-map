"""Simple P4 eBPF fuzzer.

Generates P4 programs by injecting statements into a base template,
runs p4cherry parse/typecheck, and prints a basic table + CSV.
"""
import subprocess
import sys
import shutil
from pathlib import Path

import config
from decls import *
from stmts import *
from typing import List, Dict, Tuple

def p4c_has_error(text: str) -> bool:
    return "error" in text.lower()

def run_p4c(file: Path) -> Tuple[bool, str]:
    """Run p4c-ebpf compiler and return (success, output)."""
    try:
        # Use project root as cwd and pass relative paths to avoid spaces in absolute paths
        rel_file = file.relative_to(config.PROJECT_ROOT)
        include_dir = config.P4_INCLUDE_DIR
        result = subprocess.run(
            [
                str(config.P4C_EBPF),
                str(rel_file),
                "-o",
                "/dev/null",
            ],
            cwd=str(config.PROJECT_ROOT),
            capture_output=True,
            text=True,
            timeout=30,
        )
        stdout = (result.stdout or "").strip()
        stderr = (result.stderr or "").strip()
        combined = (stderr + ("\n" if stderr and stdout else "") + stdout).strip()
        success = not p4c_has_error(combined)
        return (success, combined)
    except subprocess.TimeoutExpired:
        return (False, "TIMEOUT")
    except Exception as e:
        return (False, str(e))

def p4cherry_has_error(text: str) -> bool:
    if not text:
        return False
    return (
        "error:" in text.lower()
        or "parser error" in text.lower()
        or "type error" in text.lower()
    )

def run_p4cherry(file: Path) -> Tuple[bool, str]:
    """Run p4cherry command and return (success, output)."""
    try:
        # Use project root as cwd and pass relative paths to avoid spaces in absolute paths
        rel_file = file.relative_to(config.PROJECT_ROOT)
        include_dir = config.P4_INCLUDE_DIR
        result = subprocess.run(
            [
                str(config.P4CHERRY_PATH),
                "typecheck",
                "-i",
                str(include_dir),
                str(rel_file),
            ],
            cwd=str(config.PROJECT_ROOT),
            capture_output=True,
            text=True,
            timeout=30,
        )
        stdout = (result.stdout or "").strip()
        stderr = (result.stderr or "").strip()
        combined = (stderr + ("\n" if stderr and stdout else "") + stdout).strip()
        success = not p4cherry_has_error(combined)
        return (success, combined)
    except subprocess.TimeoutExpired:
        return (False, "TIMEOUT")
    except Exception as e:
        return (False, str(e))

def run_variant(name: str, file: Path) -> Dict[str, str]:
    # Run p4cherry typecheck
    p4cherry_ok, p4cherry_msg = run_p4cherry(file)
    # Run p4c-ebpf compile
    compile_ok, compile_msg = run_p4c(file)

    result = {
        "name": name,
        "p4cherry": "PASS" if p4cherry_ok else "FAIL",
        "p4c-ebpf": "PASS" if compile_ok else "FAIL",
        "p4cherry_msg": p4cherry_msg[:200] if not p4cherry_ok else "",
        "p4c-ebpf_msg": compile_msg[:200] if not compile_ok else "",
    }

    return result

def run_variants(grammar: str, files: List[Tuple[str, Path]]) -> List[Dict[str, str]]:
    """Run a batch of tests for a given grammar."""
    results = []

    for name, file in files:
        result = run_variant(name, file)
        results.append(result)

    return results

def output_results(category : str, results: List[Dict[str, List[Dict[str, str]]]]) -> None:
    """Print results in a table format and CSV."""
    print(f"\nResults for {category}")
    print("=" * 80)
    print(f"{'Grammar':<30} {'Variant':<20} {'P4Cherry':<10} {'P4C-eBPF':<10}")
    print("-" * 80)

    for result in results:
        grammar = result["grammar"]
        for variant in result["variants"]:
            name = variant["name"]
            p4cherry_status = variant["p4cherry"]
            p4c_status = variant["p4c-ebpf"]
            print(f"{grammar:<30} {name:<20} {p4cherry_status:<10} {p4c_status:<10}")

    # Make CSV
    csv_file = config.PROJECT_ROOT / f"results_{category.lower().replace(' ', '_')}.csv"
    with open(csv_file, "w") as f:
        f.write("Grammar,Variant,P4Cherry,P4C-eBPF,P4Cherry Error, P4C-eBPF Error\n")
        for result in results:
            grammar = result["grammar"]
            for variant in result["variants"]:
                name = variant["name"]
                p4cherry_status = variant["p4cherry"]
                p4c_status = variant["p4c-ebpf"]
                p4cherry_msg = variant["p4cherry_msg"].replace("\n", " ").replace(",", " ")
                p4c_msg = variant["p4c-ebpf_msg"].replace("\n", " ").replace(",", " ")
                f.write(f"{grammar},{name},{p4cherry_status},{p4c_status},{p4cherry_msg},{p4c_msg}\n")
    print(f"\nCSV results written to {csv_file}")

def fuzz_toplevel_declarations() -> None:
    """Fuzz top-level declaration features."""

    results: List[Dict[str, List[Dict[str, str]]]] = []

    for grammar, variants in TOPLEVEL_DECLARATION_FEATURES.items():
        output_files = []

        for variant in variants:
            name = variant["variant"]
            p4_code = config.TOPLEVEL_DECLARATION_TEMPLATE.replace("/* DEF */", variant["def"])
            p4_code = p4_code.replace("/* USE_P */", variant["use_p"])
            p4_code = p4_code.replace("/* USE_C */", variant["use_c"])

            output_file = config.OUTPUT_DIR / f"toplevelDecl_{grammar}_{name}.p4"
            with open(output_file, "w") as f:
                f.write(p4_code)

            output_files.append((name, output_file))

        results_grammar = run_variants(grammar, output_files)
        results.append({
            "grammar": grammar,
            "variants": results_grammar
        })

    output_results("Top-level Declarations", results)

def fuzz_parser_declarations() -> None:
    """Fuzz parser declaration features."""

    results: List[Dict[str, List[Dict[str, str]]]] = []

    for grammar, variants in PARSER_DECLARATION_FEATURES.items():
        output_files = []

        for variant in variants:
            name = variant["variant"]
            p4_code = config.PARSER_DECLARATION_TEMPLATE.replace("/* DEF */", variant["def"])
            p4_code = p4_code.replace("/* USE */", variant["use"])

            output_file = config.OUTPUT_DIR / f"parserDecl_{grammar}_{name}.p4"
            with open(output_file, "w") as f:
                f.write(p4_code)

            output_files.append((name, output_file))

        results_grammar = run_variants(grammar, output_files)
        results.append({
            "grammar": grammar,
            "variants": results_grammar
        })

    output_results("Parser Declarations", results)

def fuzz_control_declarations() -> None:
    """Fuzz control declaration features."""

    results: List[Dict[str, List[Dict[str, str]]]] = []

    for grammar, variants in CONTROL_DECLARATION_FEATURES.items():
        output_files = []

        for variant in variants:
            name = variant["variant"]
            p4_code = config.CONTROL_DECLARATION_TEMPLATE.replace("/* DEF */", variant["def"])
            p4_code = p4_code.replace("/* USE */", variant["use"])

            output_file = config.OUTPUT_DIR / f"controlDecl_{grammar}_{name}.p4"
            with open(output_file, "w") as f:
                f.write(p4_code)

            output_files.append((name, output_file))

        results_grammar = run_variants(grammar, output_files)
        results.append({
            "grammar": grammar,
            "variants": results_grammar
        })

    output_results("Control Declarations", results)

def fuzz_parser_statements() -> None:
    """Fuzz parser declaration features."""

    results: List[Dict[str, List[Dict[str, str]]]] = []

    for grammar, variants in PARSER_STATEMENT_FEATURES.items():
        output_files = []

        for variant in variants:
            name = variant["variant"]
            p4_code = config.PARSER_STATEMENT_TEMPLATE.replace("/* USE */", variant["use"])

            output_file = config.OUTPUT_DIR / f"controlStmt_{grammar}_{name}.p4"
            with open(output_file, "w") as f:
                f.write(p4_code)

            output_files.append((name, output_file))

        results_grammar = run_variants(grammar, output_files)
        results.append({
            "grammar": grammar,
            "variants": results_grammar
        })

    output_results("Parser Statements", results)

def fuzz_control_statements() -> None:
    """Fuzz control declaration features."""

    results: List[Dict[str, List[Dict[str, str]]]] = []

    for grammar, variants in CONTROL_STATEMENT_FEATURES.items():
        output_files = []

        for variant in variants:
            name = variant["variant"]
            p4_code = config.CONTROL_STATEMENT_TEMPLATE.replace("/* USE */", variant["use"])

            output_file = config.OUTPUT_DIR / f"controlStmt_{grammar}_{name}.p4"
            with open(output_file, "w") as f:
                f.write(p4_code)

            output_files.append((name, output_file))

        results_grammar = run_variants(grammar, output_files)
        results.append({
            "grammar": grammar,
            "variants": results_grammar
        })

    output_results("Control Statements", results)

def main() -> None:
    """Run the fuzzer."""
    print("P4 eBPF Feature Fuzzer")
    print("=" * 80)

    # Check p4cherry exists
    if not config.P4CHERRY_PATH.exists():
        print(f"ERROR: p4cherry not found at {config.P4CHERRY_PATH}")
        print("Please build p4cherry first.")
        sys.exit(1)
    # Check p4c-ebpf exists by $ which p4c-ebpf
    # if shutil.which("p4c-ebpf") is None:
    #     print("ERROR: p4c-ebpf not found")
    #     print("Please build/install p4c-ebpf first.")
    #     sys.exit(1)

    fuzz_toplevel_declarations()
    fuzz_parser_declarations()
    fuzz_control_declarations()
    fuzz_parser_statements()
    fuzz_control_statements()

if __name__ == "__main__":
    main()
