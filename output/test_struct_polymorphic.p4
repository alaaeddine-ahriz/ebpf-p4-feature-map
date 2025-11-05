#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}

struct S_t<T, U> { T a; U b; }

parser prs(packet_in p, out Headers_t headers) {
    state start {
        bit<8> tmp = 0;
        S_t<bit<8>, bit<16>> s; s.a = 8w1; s.b = 16w256;
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
        S_t<bit<8>, bit<16>> s; s.a = 8w2; s.b = 16w512;
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
