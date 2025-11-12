#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}

parser prs(packet_in p, out Headers_t headers) {
    bit<8> local_var = 8w10;
    state start {
        bit<8> tmp = 0;
        local_var = local_var + 8w1;
        transition accept;
    }
}

control pipe(inout Headers_t headers, out bool pass) {
    action Reject(bool rej) {
        pass = rej;
    }

    apply {
        bool flag = true;
        Reject(flag);
    }
}

ebpfFilter(prs(), pipe()) main;
