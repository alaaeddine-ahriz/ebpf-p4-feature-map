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

header aboutU {
    bit<4> sear;
    bit<8> othe;
    bit<4> padding;
}

header whichi {
    bit<4> thei;
    bit<8> ther;
    bit<8> cont;
    bit<4> padding;
}

struct Headers {
    ethernet_t eth_hdr;
    aboutU     busi;
    whichi     onli;
    whichi     firs;
    aboutU     woul;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.busi);
        pkt.extract(hdr.onli);
        pkt.extract(hdr.firs);
        pkt.extract(hdr.woul);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<8> servic = 8w68 << (bit<8>)hdr.eth_hdr.dst_addr;
    bit<4> theseu = 4w10;
    bit<8> clickM = 8w32;
    action servi(bit<8> pric, bit<4> peop) {
        const bit<4> statez = 4w1;
        bit<8> emailf = hdr.busi.othe;
        pass = pass;
        hdr.firs.thei = hdr.woul.padding;
    }
    action healt(bit<8> worl, bit<8> prod, bit<8> musi) {
        pass = !false;
        hdr.onli.cont = (pass ? hdr.busi.othe : 8w175 + 8w198)[7:0];
        hdr.onli.padding = (true ? hdr.woul.padding : -4w10);
        hdr.onli.cont = (hdr.woul.othe | 8w16 % 8w126 ^ 8w147) << (bit<8>)hdr.eth_hdr.eth_type;
        bit<8> should = 8w86 | prod;
        servic = 8w216 & musi;
    }
    table system {
        key = {
            (bit<4>)hdr.firs.thei: exact @name("produc");
        }
        actions = {
            servi();
        }
    }
    apply {
	pass = true;
        hdr.eth_hdr.dst_addr[3:0] = hdr.busi.sear;
        bit<8> suppor = hdr.eth_hdr.src_addr;
        bit<8> messag = 8w198 | hdr.firs.cont;
        messag = 4 * ((6 + 3) * 2);
        servic = ~(!!true ? (bit<8>)hdr.onli.ther : hdr.firs.ther[7:0]) | servic;
    }
}

ebpfFilter(prs(), pipe()) main;
