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

    bit<8> local_var = 8w10;

    apply {
        bool flag = true;
        bit<8> counter = 0;
        local_var = local_var + 8w1;
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
