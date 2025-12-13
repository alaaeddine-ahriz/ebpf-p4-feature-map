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

struct aboutF {
    bit<4> sear;
    bit<8> othe;
}

struct whichc {
    ethernet_t[1] thei;
    bit<8>        ther;
    bit<8>        cont;
    ethernet_t    busi;
    bit<4>        onli;
}

struct Headers {
    ethernet_t eth_hdr;
    ethernet_t firs;
    ethernet_t woul;
    ethernet_t serv;
    ethernet_t thes;
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
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<8> clicks = 8w63;
    bit<4> servic = 4w12;
    bit<4> priceb = ~-(7w17 - (bit<7>)servic)[6:3];
    action peopl() {
        hdr.firs.src_addr = hdr.firs.dst_addr;
        const bit<8> stateC = 8w107;
        bool emailk = pass;
        servic = 4w11;
    }
    table musicO {
        key = {
            ((bit<6>)hdr.thes.dst_addr)[4:1]: exact @name("health");
            hdr.woul.eth_type               : exact @name("worldq");
        }
        actions = {
        }
    }
    apply {
        peopl();
        const ethernet_t should = { 8w229, 4w8 ++ (4w14 & 4w1), 8w22 | 85 };
        pass = 8w84 == should.eth_type;
        hdr.woul.src_addr = hdr.thes.src_addr;
        const bit<4> system = 4w6;
    }
}

ebpfFilter(prs(), pipe()) main;
