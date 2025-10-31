#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}

parser prs(packet_in p, out Headers_t headers) {
    state start {
        transition accept;
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
        int<16> t = (int<16>)icounter; t = t / (int<16>)2; icounter = (int<8>)t;
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
