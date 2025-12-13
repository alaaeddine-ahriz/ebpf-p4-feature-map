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

header aboutS {
    bit<8> sear;
    bit<4> othe;
    bit<8> whic;
    bit<8> thei;
    bit<8> ther;
    bit<4> padding;
}

header contac {
    bit<4> busi;
    bit<4> padding;
}

struct Headers {
    ethernet_t eth_hdr;
    aboutS     onli;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.onli);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<4> firstE = 11 | (bit<4>)4w12 - ~hdr.onli.padding;
    bit<4> wouldg = 4w15;
    bit<8> servic = hdr.eth_hdr.eth_type;

    apply {
        pass = !(!true || false);
        hdr.onli.sear = 8w29;
        hdr.eth_hdr.dst_addr = hdr.eth_hdr.src_addr[7:0];
        hdr.onli.ther = hdr.onli.sear;
        pass = 6w49 == 6w60;
        const bit<4> system = 12;
    }
}

ebpfFilter(prs(), pipe()) main;
