#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}


                header H1_t { bit<8> f1; }
                header H2_t { bit<16> f2; }
                header_union HU_t { H1_t h1; H2_t h2; }
            

parser prs(packet_in p, out Headers_t headers) {
    state start {
        bit<8> tmp = 0;
        HU_t hu; hu.h1.f1 = 8w1;
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
        HU_t hu; hu.h2.f2 = 16w256;
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
