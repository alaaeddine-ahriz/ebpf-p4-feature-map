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

header aboutH {
    bit<4> sear;
    bit<8> othe;
    bit<4> whic;
    bit<4> thei;
    bit<4> ther;
}

header contac {
    bit<4> busi;
    bit<4> padding;
}

struct Headers {
    ethernet_t    eth_hdr;
    contac        onli;
    ethernet_t[8] firs;
    aboutH        woul;
    contac        serv;
    contac        thes;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.onli);
        pkt.extract(hdr.firs.next);
        pkt.extract(hdr.firs.next);
        pkt.extract(hdr.firs.next);
        pkt.extract(hdr.firs.next);
        pkt.extract(hdr.firs.next);
        pkt.extract(hdr.firs.next);
        pkt.extract(hdr.firs.next);
        pkt.extract(hdr.firs.next);
        pkt.extract(hdr.woul);
        pkt.extract(hdr.serv);
        pkt.extract(hdr.thes);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<8> clickc = --127 ^ (!!pass ? (bit<8>)8w242 : 8w122);
    bit<4> servic = (((bit<6>)hdr.woul.othe)[3:0] | hdr.serv.busi) + hdr.woul.whic;
    action price(bit<4> peop, bit<4> stat) {
        const bit<8> emailg = 8w254;
        hdr.woul.sear = hdr.woul.ther;
        hdr.woul.othe = 8w165;
        bool health = !pass;
        hdr.eth_hdr.eth_type = 8w161 >> (bit<8>)6;
        pass = false;
    }
    action world(bit<8> prod) {
        hdr.firs[max((bit<3>)servic, 3w7)].eth_type = (bit<8>)-(9 / 120) << (bit<8>)(pass ? 8w137 : hdr.firs[7].src_addr);
        price(4w8, (4w6 ^ 4w7 % 4w1) + -4w15);
        hdr.serv.busi = hdr.woul.sear;
        pass = pass;
        bit<8> musici = prod;
    }
    table policy {
        key = {
            hdr.serv.padding: exact @name("system");
        }
        actions = {
            price();
        }
    }
    table suppor {
        key = {
            servic       : exact @name("number");
            hdr.thes.busi: exact @name("please");
        }
        actions = {
            price();
        }
    }
    apply {
	pass = true;
        bit<8> messag = 8w245 & (clickc ^ 8w64);
        hdr.serv.busi = 4w14 | 3;
        const bit<8> afterC = ~(bit<8>)8w22;
        hdr.woul.othe = hdr.woul.othe;
        hdr.woul.sear = 4w0;
    }
}

ebpfFilter(prs(), pipe()) main;
