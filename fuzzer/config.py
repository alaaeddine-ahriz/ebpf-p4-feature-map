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

# Base P4 template with a hole for parser-level statement injection
PARSER_STATEMENT_TEMPLATE = """#include <core.p4>
#include <ebpf_model.p4>

header H_t {
    bit<8> f1;
    bit<16> f2;
}

struct Headers_t {
    H_t h1;
    H_t h2;
}

bit<8> f(inout bit<8> a) {
    a = a + 1;
    return a;
}

T g<T>(inout T a) {
    return a;
}

parser subprs(packet_in p, out Headers_t h) {
    state start {
        p.extract(h.h1);
        transition accept;
    }
}

parser prs(packet_in p, out Headers_t headers) {
    state start {
        bool flag = true;
        bit<8> counter = 0;
        int<8> icounter = 0;
        bit<16> value = 16w100;
        /* USE */
        p.extract(headers.h2);
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

# Base P4 template with a hole for control-level statement injection
CONTROL_STATEMENT_TEMPLATE = """#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}

bit<8> f(inout bit<8> a) {
    a = a + 1;
    return a;
}

T g<T>(inout T a) {
    return a;
}

parser prs(packet_in p, out Headers_t headers) {
    state start {
        transition accept;
    }
}

control subpipe(inout Headers_t h, out bool pass) {
    action mark_pass(bool p) {
        pass = p;
    }
    apply {
        mark_pass(true);
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
        /* USE */
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
"""

# Base P4 template with a hole for expression injection
EXPRESSION_TEMPLATE = """#include <core.p4>
#include <ebpf_model.p4>

header H1_t { bit<8> a; bit<16> b; }
header H2_t { int<8> c; int<16> d; }

struct Headers_t {
    H1_t h1;
    H2_t h2;
}

/* DEF_G */

T f<T>(in T t) { return t; }

parser prs(packet_in p, out Headers_t headers) {
    /* DEF_P */
    state start {
        p.extract(headers.h1);
        p.extract(headers.h2);
        f(/* USE_P */);
        transition accept;
    }
}

control pipe(inout Headers_t headers, out bool pass) {
    action Reject(bool rej) {
        pass = rej;
    }
    /* DEF_C */

    apply {
        f(/* USE_C */);
        Reject(true);
    }
}

ebpfFilter(prs(), pipe()) main;
"""
