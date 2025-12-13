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

header abouti {
    bit<8> sear;
    bit<4> othe;
    bit<4> padding;
}

header whichs {
    bit<8> thei;
    bit<4> ther;
    bit<4> padding;
}

struct Headers {
    ethernet_t eth_hdr;
    whichs     cont;
    whichs     busi;
    abouti     onli;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.cont);
        pkt.extract(hdr.busi);
        pkt.extract(hdr.onli);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<4> firstY = 7w8[4:1];
    action would(in bit<8> serv, bit<4> thes, bit<4> clic) {
        hdr.busi.ther = hdr.busi.ther;
        hdr.onli.padding = 4;
        pass = !(5w0 == (bit<5>)(false ? (bit<5>)(121 + (25 ^ 98)) : 5w7) || !!pass);
        bit<8> servic = hdr.eth_hdr.src_addr;
    }
    action price(bit<4> peop) {
        hdr.eth_hdr.dst_addr = 8w106 | (!false ? 8w233 : -8w240);
        bit<8> stateB = (!(true && true) ? 8w152 % 8w184 : 8w244)[7:0] & 8w208;
        pass = false;
        hdr.busi.thei = hdr.busi.thei;
        pass = false;
        bit<8> emailA = hdr.eth_hdr.dst_addr & (!!!true ? ~8w105 : 8w132) * 8w54;
    }
    table produc {
        key = {
            hdr.eth_hdr.eth_type & (bit<8>)(!false ? 8w138 : 8w178[7:0]): exact @name("health");
        }
        actions = {
            would((true ? 8w248[7:0] : 8w175 % 8w84));
            price();
        }
    }
    table policy {
        key = {
            firstY: exact @name("system");
        }
        actions = {
            would(8w94);
        }
    }
    apply {
        pass = true;
        const bit<4> number = 9;
        hdr.eth_hdr.dst_addr = 8w171 & 8w215;
        hdr.busi.thei = hdr.cont.thei;
        firstY = 4w14 | 4w11;
    }
}

ebpfFilter(prs(), pipe()) main;
