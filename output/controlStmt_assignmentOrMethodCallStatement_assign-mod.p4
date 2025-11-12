#include <core.p4>
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
        icounter = (int<8>)((int<16>)icounter % (int<16>)2);
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
