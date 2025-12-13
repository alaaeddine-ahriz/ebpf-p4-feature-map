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

header aboutY {
    bit<4> sear;
    bit<4> padding;
}

struct Headers {
    ethernet_t    eth_hdr;
    ethernet_t[1] othe;
    aboutY        whic;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.othe.next);
        pkt.extract(hdr.whic);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<8> theirt = 81;
    bit<8> thereP = theirt;
    bit<4> contac = hdr.whic.padding;
    action busin() {
        pass = !!!(theirt & hdr.eth_hdr.eth_type != 8w192 / 8w236 | -8w33) && true;
        pass = !false;
        hdr.eth_hdr.src_addr = hdr.othe[0].src_addr;
        hdr.whic.sear = 4w12 / 4w4;
        pass = !(7w1 == (bit<7>)hdr.whic.padding);
        hdr.eth_hdr.src_addr = 18;
    }
    action onlin(out bit<8> firs, bit<8> woul) {
        bit<8> servic = 8w117 & 8w6 & 8w13;
        const bit<8> theseN = ~(bit<8>)8w249;
        pass = !true;
        hdr.whic.sear = thereP[3:0] | 4w12;
        pass = pass;
        pass = true;
    }
    table stateT {
        key = {
            ~hdr.eth_hdr.src_addr: exact @name("people");
        }
        actions = {
            onlin(hdr.othe[max(2, 3w0)].dst_addr);
            busin();
        }
    }
    table emails {
        key = {
        }
        actions = {
        }
    }
    apply {
        thereP = hdr.othe[0].dst_addr | 8w147;
        busin();
        pass = false;
        bit<8> health = 8w176 * hdr.othe[0].eth_type | hdr.eth_hdr.src_addr;
    }
}

ebpfFilter(prs(), pipe()) main;
