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

header aboutb {
    bit<8> sear;
}

header otherW {
    bit<8> whic;
    bit<8> thei;
    bit<4> ther;
    bit<4> cont;
    bit<4> busi;
    bit<4> padding;
}

struct Headers {
    ethernet_t eth_hdr;
    aboutb     onli;
    aboutb     firs;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.onli);
        pkt.extract(hdr.firs);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<8> wouldE = 8w169;
    action servi(bit<8> thes, bit<4> clic, bit<4> serv) {
        bool priceq = (bit<7>)wouldE != (bit<7>)clic;
        priceq = false;
        hdr.eth_hdr.src_addr = 7 * 11 | thes;
        const bit<4> people = 4w14;
        pass = (bit<5>)clic != (bit<5>)hdr.onli.sear;
    }
    action state(bit<8> emai) {
        bool health = !pass;
        pass = 1w1 == (1 ^ 1) & 1w1;
        bool worldC = false && false;
        pass = true;
    }
    action produ(bit<8> musi) {
        bit<8> should = (pass && true ? (bit<8>)musi : 8w115);
        bool produc = !((bit<2>)should == 2w0);
        bit<8> system = 8w213 - 83;
        bit<4> policy = 4w10 - ((bit<4>)hdr.onli.sear | ~(bit<4>)4w13);
        policy = -4w5;
        pass = true || true;
    }
    apply {
        pass = (bit<1>)hdr.eth_hdr.src_addr != 1 ^ 1;
        hdr.eth_hdr.eth_type = ~(bit<8>)8w224;
        pass = !!!((bit<2>)hdr.onli.sear != (!(-(6w37 >> (bit<8>)(bit<6>)hdr.eth_hdr.eth_type == 8 ? (bit<1>)1w0 : 1w0) == 1w0) ? 2w2 : 2w1));
        const bit<8> messag = (-6w18 ++ 8w196[2:1])[7:0];
    }
}

ebpfFilter(prs(), pipe()) main;
