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
    bit<4> sear;
    bit<4> othe;
    bit<8> whic;
    bit<4> thei;
    bit<4> ther;
}

header contac {
    bit<4> busi;
    bit<8> onli;
    bit<4> firs;
    bit<4> woul;
    bit<4> serv;
}

struct Headers {
    ethernet_t eth_hdr;
    contac     thes;
    ethernet_t clic;
    contac     pric;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.thes);
        pkt.extract(hdr.clic);
        pkt.extract(hdr.pric);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bool people = !!false;
    bit<4> stateW = (hdr.pric.woul - 4w0 & -4w0) - 4w11;
    bit<8> emaill = -(bit<8>)(hdr.thes.onli >> (bit<8>)4);
    action healt(bit<4> worl) {
        people = pass;
        hdr.pric.woul = hdr.thes.woul;
        people = false;
        hdr.pric.woul = 11 | 1 ^ 2 * 2;
        hdr.thes.woul = 4w12 & (bit<3>)3w0 ++ (true && !people ? 1w1 : (bit<1>)21);
        const bit<8> produc = 8w20;
    }
    table system {
        key = {
            (bit<4>)(stateW + hdr.thes.serv): exact @name("should");
        }
        actions = {
            healt();
        }
        implementation = hash_table(10);
    }
    apply {
	pass = true;
        hdr.pric.woul = 4w13 | 4w15;
        pass = pass;
        people = !false;
        hdr.pric.serv = 4w9;
        bit<8> policy = 8w3;
        people = system.apply().hit && true || (!false || !false);
    }
}

ebpfFilter(prs(), pipe()) main;
