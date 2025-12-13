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

header aboutd {
    bit<8> sear;
    bit<4> othe;
    bit<8> whic;
    bit<4> thei;
}

header thereW {
    bit<8> cont;
    bit<8> busi;
    bit<4> onli;
    bit<4> padding;
}

struct Headers {
    ethernet_t eth_hdr;
    ethernet_t firs;
    thereW     woul;
    ethernet_t serv;
    thereW     thes;
    ethernet_t clic;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.firs);
        pkt.extract(hdr.woul);
        pkt.extract(hdr.serv);
        pkt.extract(hdr.thes);
        pkt.extract(hdr.clic);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<4> servic = 6w19[4:1];
    bit<8> priceI = (bit<8>)(hdr.woul.busi + hdr.eth_hdr.src_addr)[7:0];
    bit<8> people = 8w158;
    action state(bit<4> emai) {
        pass = 7w98 == (bit<7>)hdr.clic.src_addr || !false;
        bit<8> health = 8w139;
        pass = 2w0 != 2w2;
        const aboutd worlde = { 8w213, 4w11, 8w153, (~4w6 | 4w4) & 4w15 };
    }
    action produ(bit<4> musi, bit<4> shou, bit<8> prod) {
        hdr.clic.src_addr = 8w21;
        hdr.firs.src_addr = 8w237;
        hdr.thes.onli = hdr.woul.padding & musi;
        pass = true;
        pass = !!!pass;
    }
    table please {
        key = {
            hdr.thes.onli * 4w10                         : exact @name("system");
            ((bit<5>)hdr.clic.src_addr - -6w48[4:0])[3:0]: exact @name("policy");
        }
        actions = {
            state();
        }
        implementation = hash_table(10);
    }
    table softwa {
        key = {
            4w11 ++ -hdr.woul.onli                                              : exact @name("suppor");
            people                                                              : exact @name("messag");
            ((!pass ? hdr.thes.padding : 4w7) >> (bit<8>)hdr.woul.padding) * 4w6: exact @name("afterb");
        }
        actions = {
            produ();
        }
    }
    apply {
        pass = (please.apply().hit ? 8w60 : hdr.serv.src_addr & 8w154) == 8w17 && !false && (!false || !false);
        hdr.thes.busi = 12 | 12;
        const bit<4> videoE = ((bit<7>)(7w36 | 7w102))[4:1] | 4w12 | 4w7;
        pass = false;
        hdr.woul.onli = hdr.thes.padding;
        pass = !true;
    }
}

ebpfFilter(prs(), pipe()) main;
