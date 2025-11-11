"""Configuration for the fuzzer."""
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent
P4C_EBPF = "p4c-ebpf"
P4CHERRY_PATH = PROJECT_ROOT / "p4cherry" / "p4cherry"
OUTPUT_DIR = PROJECT_ROOT / "output"
# Prefer relative include dir (avoid spaces in absolute path breaking downstream tools)
P4_INCLUDE_DIR = Path("p4cherry/p4/testdata/arch")

# Ensure output directory exists at runtime
OUTPUT_DIR.mkdir(exist_ok=True)

# Base P4 template with a hole for top-level declaration injection
TOPLEVEL_DECLARATION_TEMPLATE = """#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}

/* DEF */

parser prs(packet_in p, out Headers_t headers) {
    state start {
        bit<8> tmp = 0;
        /* USE_P */
        transition accept;
    }
}

control pipe(inout Headers_t headers, out bool pass) {
    action Reject(bool rej) {
        pass = rej;
    }

    apply {
        bool flag = true;
        bit<8> tmp = 0;
        bit<8> counter = 0;
        int<8> icounter = 0;
        bit<16> value = 16w100;
        /* USE_C */
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
"""

# Base P4 template with a hole for parser-level declaration injection
PARSER_DECLARATION_TEMPLATE = """#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}

parser prs(packet_in p, out Headers_t headers) {
    /* DEF */
    state start {
        bit<8> tmp = 0;
        /* USE */
        transition accept;
    }
}

control pipe(inout Headers_t headers, out bool pass) {
    action Reject(bool rej) {
        pass = rej;
    }

    apply {
        bool flag = true;
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
"""

# Base P4 template with a hole for control-level declaration injection
CONTROL_DECLARATION_TEMPLATE = """#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}

parser prs(packet_in p, out Headers_t headers) {
    state start {
        bit<8> tmp = 0;
        transition accept;
    }
}

control pipe(inout Headers_t headers, out bool pass) {
    action Reject(bool rej) {
        pass = rej;
    }

    /* DEF */

    apply {
        bool flag = true;
        bit<8> counter = 0;
        /* USE */
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
"""

# Base P4 template with a hole for control-level statement injection
CONTROL_STATEMENT_TEMPLATE = """#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}

parser prs(packet_in p, out Headers_t headers) {
    state start {
        transition accept;
    }
}

control pipe(inout Headers_t headers, out bool pass) {
    action Reject(bool rej) {
        pass = rej;
    }

    apply {
        bool flag = true;
        bit<8> counter = 0;
        int<8> icounter = 0;
        bit<16> value = 16w100;
        /* HOLE */
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
"""
