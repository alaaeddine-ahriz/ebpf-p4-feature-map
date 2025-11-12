#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}

parser prs(packet_in p, out Headers_t headers) {
    state start {
        bit<8> tmp = 0;
        transition accept;
    }
}

control pipe(inout Headers_t headers, out bool pass) {
    action Reject(bool rej) {
        pass = rej;
    }

    action set_to_one(inout bit<8> x) { x = 8w1; }

    apply {
        bool flag = true;
        bit<8> counter = 0;
        set_to_one(counter);
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
