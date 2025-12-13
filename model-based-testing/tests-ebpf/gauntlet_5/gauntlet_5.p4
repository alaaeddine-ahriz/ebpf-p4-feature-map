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

header aboutB {
    bit<4> sear;
    bit<4> othe;
    bit<8> whic;
}

struct Headers {
    ethernet_t eth_hdr;
    ethernet_t thei;
    ethernet_t ther;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.thei);
        pkt.extract(hdr.ther);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    ethernet_t contac = { hdr.ther.eth_type + 6, 8w167, -(true ? 86 + ((bit<8>)8w48)[7:0] : 8w203) };
    bit<8> busine = 8w183;
    action onlin(bit<4> firs, bit<4> woul, bit<4> serv) {
        hdr.eth_hdr.dst_addr = 8w168;
        pass = (bit<3>)hdr.ther.src_addr |-| 3w5 != (bit<3>)hdr.thei.src_addr;
        pass = !!(7w40 | -7w46 == 7w117 && !!!!true);
        hdr.thei.src_addr = hdr.thei.eth_type;
        contac.eth_type = 8w186;
        contac.dst_addr = 8w255 ^ hdr.thei.dst_addr - (~8w93)[7:0];
    }
    table theseU {
        key = {
        }
        actions = {
        }
    }
    apply {
        pass = !!false || theseU.apply().hit;
        hdr.eth_hdr.src_addr = 8w70;
        hdr.ther.src_addr = 8w50;
        pass = !((bit<5>)contac.src_addr ^ 5w0 == (bit<5>)hdr.ther.dst_addr);
    }
}

ebpfFilter(prs(), pipe()) main;
