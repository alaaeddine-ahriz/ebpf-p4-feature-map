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

struct aboutM {
    bit<8> sear;
    bit<8> othe;
    bit<8> whic;
    bit<8> thei;
    bit<4> ther;
}

header contac {
    bit<4> busi;
    bit<8> onli;
    bit<4> firs;
    bit<4> woul;
    bit<4> padding;
}

struct servic {
    bit<4> thes;
}

struct Headers {
    ethernet_t eth_hdr;
    contac     clic;
    ethernet_t serv;
    ethernet_t pric;
    ethernet_t peop;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.clic);
        pkt.extract(hdr.serv);
        pkt.extract(hdr.pric);
        pkt.extract(hdr.peop);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<8> stateP = (pass ? -hdr.serv.dst_addr & 8w242 : (bit<8>)-9);
    bit<8> emailQ = 8w71[7:0];
    action healt(bit<4> worl, bit<4> prod) {
        const bit<8> musicC = (~8w163 | 8w114)[7:0];
        hdr.eth_hdr.eth_type = hdr.eth_hdr.dst_addr[7:0];
        hdr.serv.eth_type = (8w174[7:0] | 8w42) ^ (pass ? 8w60 : 8w20);
        const bit<8> should = 8 * (3 | 6) ^ 9;
    }
    action produ() {
        hdr.clic.onli = 8w185;
        hdr.clic.padding = 4w1;
        pass = !(2w2 != 2w1);
        hdr.clic.woul = 4w9;
    }
    action syste(inout bit<8> poli, bit<8> numb) {
        healt(4w8, 4w8);
        hdr.pric.eth_type = 8w44 | (bit<4>)4w12 ++ (true ? hdr.clic.woul : 4w9);
        pass = !(6w40 == 6w18);
        pass = pass;
    }
    apply {
	pass = true;
        syste(hdr.serv.dst_addr, 8w103);
        pass = pass;
        emailQ = 8w233;
        const contac softwa = { 4w1, 8w58, 4w15[3:0], (true ? 4w14 : 8w63[6:3]), -((4w6 | 4w11 | 4w4) + 4w5) };
        pass = !false;
    }
}

ebpfFilter(prs(), pipe()) main;
