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

header aboutb {
    bit<8> sear;
    bit<4> othe;
    bit<8> whic;
    bit<4> thei;
}

struct Headers {
    ethernet_t eth_hdr;
    ethernet_t ther;
    aboutb     cont;
    aboutb     busi;
    aboutb     onli;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.ther);
        pkt.extract(hdr.cont);
        pkt.extract(hdr.busi);
        pkt.extract(hdr.onli);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<8> firstZ = ((bit<8>)(90 ^ 8w140))[7:0];
    action would() {
        pass = pass;
        pass = !pass;
        pass = !(false && ((4w1 ^ 4w7) - 4w4)[3:0] | hdr.onli.othe != -125);
        hdr.cont.othe = ((bit<7>)(bit<7>)hdr.busi.othe)[3:0];
        hdr.cont.sear = firstZ;
    }
    apply {
        pass = false;
        firstZ = (bit<8>)(8w121 - (hdr.onli.sear - hdr.eth_hdr.dst_addr) + 8w111);
        pass = false;
        pass = !true;
    }
}

ebpfFilter(prs(), pipe()) main;
