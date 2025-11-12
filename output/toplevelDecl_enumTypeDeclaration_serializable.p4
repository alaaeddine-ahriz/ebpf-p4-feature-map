#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}

enum bit<8> E2_t { C = 1, D = 2 }

parser prs(packet_in p, out Headers_t headers) {
    state start {
        bit<8> tmp = 0;
        E2_t e = E2_t.C;
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
        E2_t e = E2_t.D;
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
