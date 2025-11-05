#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}

typedef header H_t { bit<8> field1; } MyH_t;

parser prs(packet_in p, out Headers_t headers) {
    state start {
        bit<8> tmp = 0;
        MyH_t h; h.field1 = 8w1;
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
        MyH_t h; h.field1 = 8w2;
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
