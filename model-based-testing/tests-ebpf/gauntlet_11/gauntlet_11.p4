#include <core.p4>
#include <ebpf_model.p4>

bit<3> max(in bit<3> val, in bit<3> bound) {
    return val < bound ? val : bound;
}
header ethernet_t {
    bit<8> dst_addr;
    bit<8> src_addr;
    bit<8> eth_type;
}

header aboutA {
    bit<8> sear;
    bit<4> othe;
    bit<4> padding;
}

struct Headers {
    ethernet_t eth_hdr;
    ethernet_t whic;
    ethernet_t thei;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.whic);
        pkt.extract(hdr.thei);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<4> thereT = 4w6 & 4w4;
    action conta(bit<8> busi, bit<8> onli) {
        hdr.whic.dst_addr = 8w158;
        const bit<4> firstK = 9;
        const int wouldw = 89 / 38;
        hdr.thei.eth_type = 8w139 / 8w77;
        hdr.eth_hdr.eth_type = hdr.whic.src_addr;
        const bit<8> servic = 8w52;
    }
    table pricey {
        key = {
            8w129 ^ (!pass ? (bit<8>)8w7 : 8w135): exact @name("theseT");
            (!true ? ~8w128 : hdr.whic.eth_type) : exact @name("clickk");
        }
        actions = {
            conta();
        }
    }
    table people {
        key = {
        }
        actions = {
        }
    }
    apply {
        bool stateT = !true;
        hdr.whic.dst_addr = 15 % 16 + 38 | 8w55;
        bit<4> emaild = thereT;
	pass = true;
        stateT = !pass && !(!!!!!pass || (pass || !pass));
        emaild = emaild;
    }
}

ebpfFilter(prs(), pipe()) main;
