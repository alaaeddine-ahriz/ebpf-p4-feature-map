#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}

typedef enum bit<8> E_t { A = 1, B = 2 } MyE_t;

parser prs(packet_in p, out Headers_t headers) {
    state start {
        bit<8> tmp = 0;
        MyE_t e = MyE_t.A;
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
        MyE_t e = MyE_t.B;
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
