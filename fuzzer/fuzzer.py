"""Simple P4 eBPF fuzzer.

Generates P4 programs by injecting statements into a base template,
runs p4cherry parse/typecheck, and prints a basic table + CSV.
"""
import subprocess
import sys
from pathlib import Path

import config
from features import STATEMENT_FEATURES


def _has_error(text: str) -> bool:
    if not text:
        return False
    lowered = text.lower()
    return (
        "error:" in lowered
        or "parser error" in lowered
        or "type error" in lowered
    )


def run_p4cherry(p4_file: Path, command: str) -> tuple[bool, str]:
    """Run p4cherry command and return (success, output)."""
    try:
        # Use project root as cwd and pass relative paths to avoid spaces in absolute paths
        rel_file = p4_file.relative_to(config.PROJECT_ROOT)
        include_dir = config.P4_INCLUDE_DIR
        result = subprocess.run(
            [
                str(config.P4CHERRY_PATH),
                command,
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
        # Strict success: zero exit, empty stderr, and no error markers anywhere
        success = (result.returncode == 0) and (stderr == "") and not _has_error(combined)
        return (success, combined)
    except subprocess.TimeoutExpired:
        return (False, "TIMEOUT")
    except Exception as e:
        return (False, str(e))


def main() -> None:
    """Run the fuzzer."""
    print("P4 eBPF Feature Fuzzer")
    print("=" * 80)

    # Check p4cherry exists
    if not config.P4CHERRY_PATH.exists():
        print(f"ERROR: p4cherry not found at {config.P4CHERRY_PATH}")
        print("Please build p4cherry first.")
        sys.exit(1)

    results: list[dict[str, str]] = []

    for i, (name, feature) in enumerate(STATEMENT_FEATURES.items(), 1):
        print(f"[{i}/{len(STATEMENT_FEATURES)}] Testing {name}...", end=" ")

        # Generate P4 code
        p4_code = config.TEMPLATE.replace("/* HOLE */", feature["code"]) 

        # Save to file
        output_file = config.OUTPUT_DIR / f"test_{name}.p4"
        with open(output_file, "w") as f:
            f.write(p4_code)

        # Run p4cherry parse
        parse_ok, parse_msg = run_p4cherry(output_file, "parse")

        # Run p4cherry typecheck (only if parse succeeded)
        if parse_ok:
            typecheck_ok, typecheck_msg = run_p4cherry(output_file, "typecheck")
        else:
            typecheck_ok, typecheck_msg = False, "SKIPPED (parse failed)"

        # Store result
        results.append({
            "name": name,
            "grammar": feature["grammar"],
            "parse": "PASS" if parse_ok else "FAIL",
            "typecheck": "PASS" if typecheck_ok else "FAIL",
            "parse_msg": parse_msg[:200] if not parse_ok else "",
            "typecheck_msg": typecheck_msg[:200] if not typecheck_ok else "",
        })

        # Print quick status
        if parse_ok and typecheck_ok:
            print("\u2713")
        elif not parse_ok:
            print("\u2717 (parse)")
        else:
            print("\u2717 (typecheck)")

    # Print table
    print("\n" + "=" * 80)
    print("RESULTS")
    print("=" * 80)
    print(f"{'Feature':<20} {'Grammar':<34} {'Parse':<8} {'Typecheck':<10}")
    print("-" * 80)

    for r in results:
        print(f"{r['name']:<20} {r['grammar']:<34} {r['parse']:<8} {r['typecheck']:<10}")

    # Print summary
    print("-" * 80)
    total = len(results)
    parse_pass = sum(1 for r in results if r["parse"] == "PASS")
    typecheck_pass = sum(1 for r in results if r["typecheck"] == "PASS")
    both_pass = sum(1 for r in results if r["parse"] == "PASS" and r["typecheck"] == "PASS")

    print(
        f"Total: {total} | Parse: {parse_pass}/{total} | "
        f"Typecheck: {typecheck_pass}/{total} | Both: {both_pass}/{total}"
    )

    # Save CSV
    csv_file = config.PROJECT_ROOT / "results.csv"
    with open(csv_file, "w") as f:
        f.write("feature,grammar,parse,typecheck,parse_error,typecheck_error\n")
        for r in results:
            f.write(
                f"{r['name']},{r['grammar']},{r['parse']},{r['typecheck']},"
                f'"{r["parse_msg"]}","{r["typecheck_msg"]}"\n'
            )

    print(f"\nResults saved to: {csv_file}")


if __name__ == "__main__":
    main()


