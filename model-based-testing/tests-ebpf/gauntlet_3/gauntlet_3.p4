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

struct abouth {
    bit<4> sear;
}

struct Headers {
    ethernet_t eth_hdr;
    ethernet_t othe;
    ethernet_t whic;
    ethernet_t thei;
    ethernet_t ther;
    ethernet_t cont;
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
        pkt.extract(hdr.cont);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    ethernet_t busine = hdr.ther;
    action onlin(bit<4> firs, bit<8> woul) {
        const bit<4> servic = 4w10;
        hdr.cont.src_addr = hdr.whic.src_addr;
        pass = true || (true || false);
        pass = pass;
    }
    apply {
        const bit<8> people = 8w162[7:0];
        bit<4> stateL = 4w1;
        hdr.thei.src_addr = 8w245;
	onlin(stateL, hdr.thei.src_addr);
        const bit<8> emailM = 8w4;
    }
}

ebpfFilter(prs(), pipe()) main;
