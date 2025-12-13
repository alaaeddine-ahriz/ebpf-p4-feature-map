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

struct aboutQ {
    bit<8> sear;
    bit<4> othe;
}

header whichG {
    bit<4> thei;
    bit<8> ther;
    bit<4> cont;
    bit<4> busi;
    bit<4> padding;
}

struct Headers {
    ethernet_t eth_hdr;
    whichG     onli;
    ethernet_t firs;
    ethernet_t woul;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.onli);
        pkt.extract(hdr.firs);
        pkt.extract(hdr.woul);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<8> servic = 8w140;
    action these(bit<4> clic, bit<4> serv) {
        pass = true;
        bit<4> priceX = ((bit<7>)hdr.onli.ther)[3:0];
        hdr.onli.cont = (!!pass ? 4w13 : 3 * (!!pass ? (bit<4>)4w0 : 4w12));
        pass = !!false;
        pass = true;
        hdr.onli.cont = serv;
    }
    action peopl(bit<4> stat, bit<8> emai, bit<8> heal) {
        hdr.woul.eth_type = ((8w218 | (bit<6>)-2 ++ 2w0) - 8w105)[7:0];
        pass = false || !false;
        pass = true;
        pass = !!(!!pass || !pass);
        these(~4w4, 4w8);
    }
    table produc {
        key = {
            hdr.eth_hdr.dst_addr: exact @name("worldE");
        }
        actions = {
            peopl();
            these();
        }
        implementation = hash_table(10);
    }
    apply {
        hdr.onli.padding = 4 % 97 + hdr.onli.busi;
        produc.apply();
        hdr.onli.cont = (!true && ((bit<4>)hdr.onli.thei)[2:2] != 1w1 ? 4w15 : hdr.onli.cont) - hdr.onli.cont;
        hdr.onli.padding = -((bit<5>)hdr.onli.padding)[4:1] * 4w1;
        pass = true;
        hdr.onli.busi = 4w6;
    }
}

ebpfFilter(prs(), pipe()) main;
