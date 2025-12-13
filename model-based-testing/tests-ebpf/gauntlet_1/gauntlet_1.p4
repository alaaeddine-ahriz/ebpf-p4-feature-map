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

header aboutR {
    bit<8> sear;
    bit<4> othe;
    bit<4> whic;
}

struct Headers {
    ethernet_t eth_hdr;
    aboutR     thei;
    ethernet_t ther;
    aboutR     cont;
    ethernet_t busi;
    aboutR     onli;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.thei);
        pkt.extract(hdr.ther);
        pkt.extract(hdr.cont);
        pkt.extract(hdr.busi);
        pkt.extract(hdr.onli);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<8> firstp = hdr.eth_hdr.dst_addr;
    action would(bit<4> serv) {
        hdr.thei.whic = 3;
        const ethernet_t theseP = { 8w153, (bit<8>)(8w186 % 8w143) - (bit<8>)(60 % 91), -(bit<8>)8w222 };
        const Headers clickX = { { 8w10, 8w193, ((8w147 ^ 8w203) + (bit<8>)-18 - 8w24)[7:0] }, { -(8w252 + 8w140), 4w0, 4w11 }, { 8w31 / 8w25 ^ 8w70, 8w65, 8w252 - 8w252 }, { 7, 4w7, ((!!(false || true) ? (bit<5>)5w20 + 5w8 : 5w22) | 5w18)[3:0] }, { 8w38, (bit<8>)-8w155, 8w90 - (8w243 | 8w203 - 8w65 - 8w130) }, { 8w114, 4w14, 4w4 } };
        hdr.cont.whic = 9;
    }
    action servi(bit<8> pric, bit<8> peop, bit<8> stat) {
        ethernet_t emailX = { 8w65, 8w48, ((bit<8>)19)[7:0] };
        would(4w10 + 4w15);
        would(4w1);
        hdr.eth_hdr.eth_type = (bit<8>)hdr.busi.eth_type;
        const bit<4> health = 4w10;
        hdr.onli.othe = 4w6 / 4w9;
    }
    table produc {
        key = {
            hdr.busi.eth_type: exact @name("worldF");
        }
        actions = {
            would();
        }
    }
    table policy {
        key = {
            8w8 + hdr.eth_hdr.src_addr: exact @name("musicw");
        }
        actions = {
            would();
        }
    }
    table messag {
        key = {
            hdr.cont.sear                      : exact @name("please");
        }
        actions = {
        }
    }
    apply {
        pass = true;
        hdr.onli.sear = 8w152 | 8w36;
        hdr.eth_hdr.dst_addr = 8w174 | (hdr.busi.dst_addr | 8w225 + hdr.cont.sear) & 8w136;
        pass = !!pass;
        pass = (bit<2>)hdr.thei.whic != 2w1 ^ (pass ? 2w1 / 2w3 : 2w0) + 2w1;
        pass = !true;
    }
}

ebpfFilter(prs(), pipe()) main;
