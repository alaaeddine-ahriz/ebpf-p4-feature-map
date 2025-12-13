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
}

struct otherL {
    bit<4> whic;
}

struct theirI {
    bit<4> ther;
}

struct Headers {
    ethernet_t eth_hdr;
    aboutS     cont;
    aboutS[8]  busi;
    aboutS     onli;
    aboutS     firs;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.cont);
        pkt.extract(hdr.busi.next);
        pkt.extract(hdr.busi.next);
        pkt.extract(hdr.busi.next);
        pkt.extract(hdr.busi.next);
        pkt.extract(hdr.busi.next);
        pkt.extract(hdr.busi.next);
        pkt.extract(hdr.busi.next);
        pkt.extract(hdr.busi.next);
        pkt.extract(hdr.onli);
        pkt.extract(hdr.firs);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    aboutS wouldy = hdr.firs;
    action servi(out bit<4> thes, bit<4> clic) {
        thes = thes - (4w1 << (bit<8>)4w3 & 4w1);
        thes = 4w2;
        wouldy.sear[3:0] = (5w30 / 5w9)[3:0];
        hdr.busi[max(((bit<3>)clic | 3w6) & 1w0 ++ (bit<2>)(2w1 ^ 3), 3w7)].sear = 8w65;
        const int servic = (4 & 18) * (82 | 54) & 75;
        hdr.eth_hdr.src_addr = 8w255;
    }
    table priceU {
        key = {
        }
        actions = {
        }
    }
    apply {
        pass = !false;
        pass = true;
        pass = pass;
        pass = pass;
    }
}

ebpfFilter(prs(), pipe()) main;
