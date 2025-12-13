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

header aboutp {
    bit<4> sear;
    bit<4> padding;
}

struct Headers {
    ethernet_t eth_hdr;
    aboutp     othe;
    aboutp     whic;
    aboutp     thei;
    ethernet_t ther;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.othe);
        pkt.extract(hdr.whic);
        pkt.extract(hdr.thei);
        pkt.extract(hdr.ther);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    Headers contac = hdr;
    bit<4> busine = hdr.othe.sear;
    action onlin() {
        hdr.eth_hdr.eth_type = contac.ther.dst_addr;
        aboutp firsta = { (115 ^ 103) - 6, 4w8 / 4w5 };
        contac.eth_hdr.src_addr = -(8w43 + 8w187);
        pass = !(2w0 / 2w2 != 2w0);
        hdr.eth_hdr.eth_type = -contac.eth_hdr.src_addr;
    }
    table theseu {
        key = {
        }
        actions = {
            onlin();
        }
    }
    apply {
        hdr.eth_hdr.src_addr = (bit<3>)3w2 ++ 5w23;
        pass = !!!!!!false;
        busine = ~contac.othe.padding & contac.othe.sear;
        contac.whic.padding = ((!true ? 5w8 : 5w2) | 5w25)[3:0];
        const int clickt = 39;
    }
}

ebpfFilter(prs(), pipe()) main;
