#include <core.p4>
#include <ebpf_model.p4>

header H1_t { bit<8> a; bit<16> b; }
header H2_t { int<8> c; int<16> d; }

struct Headers_t {
    H1_t h1;
    H2_t h2;
}



T f<T>(in T t) { return t; }

parser prs(packet_in p, out Headers_t headers) {
    
    state start {
        p.extract(headers.h1);
        p.extract(headers.h2);
        f(8w1);
        transition accept;
    }
}

control pipe(inout Headers_t headers, out bool pass) {
    action Reject(bool rej) {
        pass = rej;
    }
    tuple<bit<8>, int<8>> tup =  { headers.h1.a, headers.h2.c };

    apply {
        f(tup[0]);
        Reject(true);
    }
}

ebpfFilter(prs(), pipe()) main;
