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

header aboutz {
    bit<8> sear;
    bit<4> othe;
    bit<4> whic;
}

header theirw {
    bit<8> ther;
}

header contac {
    bit<4> busi;
    bit<4> padding;
}

struct Headers {
    ethernet_t eth_hdr;
    ethernet_t onli;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.onli);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    theirw firstC = { 8w123 };
    action would() {
        ethernet_t servic = hdr.onli;
        firstC.ther = ~8w53 << (bit<8>)(8w108 ^ servic.eth_type);
        pass = !(((pass ? (bit<3>)hdr.eth_hdr.dst_addr : (bit<2>)hdr.eth_hdr.src_addr ++ (bit<1>)1w1) != 3w2 || pass || false) && !!pass);
        servic.eth_type = hdr.onli.dst_addr;
    }
    action these(bit<8> clic, bit<4> serv, bit<8> pric) {
        pass = !!true;
        hdr.onli.dst_addr = (true ? hdr.onli.src_addr : firstC.ther);
        bit<4> people = 4w1;
        pass = !!pass;
    }
    action state(out bit<4> emai, bit<8> heal) {
        pass = false;
        emai = 4w0;
        pass = true;
        hdr.onli.dst_addr = hdr.onli.dst_addr;
        bit<8> worldM = 8w69;
        pass = !!true;
    }
    table should {
        key = {
        }
        actions = {
            would();
        }
    }
    apply {
        pass = true;
        theirw[7] system;
        hdr.eth_hdr.src_addr = hdr.eth_hdr.src_addr;
        hdr.onli.eth_type = hdr.eth_hdr.eth_type + (true ? 8w199 : firstC.ther);
    }
}

ebpfFilter(prs(), pipe()) main;
