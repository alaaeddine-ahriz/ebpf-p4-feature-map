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

header aboutD {
    bit<4> sear;
    bit<8> othe;
    bit<4> padding;
}

header whichI {
    bit<4> thei;
    bit<8> ther;
    bit<8> cont;
    bit<4> padding;
}

header busine {
    bit<4> onli;
    bit<4> padding;
}

struct Headers {
    ethernet_t eth_hdr;
    aboutD     firs;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.firs);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<8> wouldW = 8w163;
    action servi(bit<4> thes, bit<8> clic) {
        pass = !true;
        hdr.firs.sear = (4w13 | (!false ? hdr.firs.padding : 4w11) + 4w10) + 4w15;
        pass = false;
        pass = !!(hdr.firs.othe[7:0][3:1] == 3w3);
        pass = !!!(false || !(true || false));
    }
    table people {
        key = {
            hdr.firs.padding: exact @name("pricef");
        }
        actions = {
            servi();
        }
    }
    apply {
        hdr.firs.sear = 4w6;
        hdr.firs.padding = ((bit<3>)hdr.eth_hdr.src_addr << (bit<8>)3w1) * 3w0 ++ (bit<1>)-51;
        pass = !false || (!!(3w6 != 3w7) || !!(!false && false));
        hdr.firs.padding = 9;
        hdr.eth_hdr.dst_addr = 8w32;
    }
}

ebpfFilter(prs(), pipe()) main;
