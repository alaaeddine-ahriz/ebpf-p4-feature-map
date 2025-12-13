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

header aboutt {
    bit<4> sear;
    bit<4> padding;
}

struct Headers {
    ethernet_t eth_hdr;
    aboutt     othe;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.othe);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<4> whichC = 4w2;
    bool theirx = !(1 != -(81 * (116 ^ 50)));
    action there(bit<4> cont) {
        pass = !true;
        hdr.othe.sear = 4w15;
        whichC = 4w8;
        whichC = ((bit<7>)((false ? (bit<7>)(bit<7>)hdr.othe.sear : (bit<7>)hdr.eth_hdr.dst_addr) >> (bit<8>)7w1))[5:2];
    }
    action busin(bit<8> onli) {
        theirx = !(true || !true);
        const bit<8> firstP = 8w102;
        const bit<8> wouldt = 8w255 | 8w59 / 8w130;
        pass = theirx;
    }
    action servi(bit<4> thes, bit<8> clic) {
        hdr.eth_hdr.eth_type = hdr.eth_hdr.src_addr;
        hdr.othe.padding = hdr.othe.sear;
        theirx = theirx;
        hdr.othe.sear = --hdr.othe.padding;
        hdr.othe.sear = (!true ? 4w11 : 4w14) + whichC;
        pass = !true;
    }
    table people {
        key = {
            -(!(hdr.othe.sear == whichC) ? 8w135 : 8w43): exact @name("servic");
        }
        actions = {
            servi();
            there();
        }
    }
    apply {
        hdr.othe.padding = 4w10 + ((bit<6>)hdr.eth_hdr.dst_addr)[3:0];
        whichC = 4w0;
        hdr.othe.sear = whichC;
        const bit<4> stateF = 4w8;
        busin(34 + (8w80 ^ 8w169 != 8w52 | 8w16 || false ? (bit<8>)8w119 : 8w51));
    }
}

ebpfFilter(prs(), pipe()) main;
