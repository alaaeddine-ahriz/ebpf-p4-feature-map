#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}


            bit<8> add_one(in bit<8> x) {
                return x + 8w1;
            }
        

parser prs(packet_in p, out Headers_t headers) {
    state start {
        bit<8> tmp = 0;
        bit<8> y = add_one(tmp);
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
        bit<8> z = add_one(tmp);
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
