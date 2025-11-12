#include <core.p4>
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
        { { bit<8> inner = 8w2; } }
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
