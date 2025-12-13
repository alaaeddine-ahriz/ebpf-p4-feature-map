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

header aboutg {
    bit<4> sear;
    bit<4> othe;
}

header whichf {
    bit<8> thei;
    bit<8> ther;
    bit<4> cont;
    bit<4> busi;
}

header online {
    bit<8> firs;
    bit<4> woul;
    bit<4> padding;
}

struct Headers {
    ethernet_t eth_hdr;
    aboutg     serv;
    online     thes;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.serv);
        pkt.extract(hdr.thes);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bool clickb = !false;
    bit<4> servic = hdr.thes.padding;
    action price() {
        hdr.thes.woul = (true ? 4w10 % 4w4 : 4w14);
        hdr.thes.woul = 4w15 / 4w10;
        clickb = !!(1w1 != (true ? (bit<1>)hdr.serv.othe : 1w0) || clickb);
        hdr.thes.woul = 4w10;
        bool people = !false;
        people = false;
    }
    action state(bit<4> emai) {
        servic = emai |-| 4w4;
        hdr.serv.othe = 4w11;
        price();
        clickb = !!(!clickb && pass || !!!!!!((bit<5>)hdr.serv.sear ++ (bit<1>)servic != (bit<6>)hdr.serv.sear |+| hdr.eth_hdr.dst_addr[6:1]));
        hdr.eth_hdr.src_addr = 8w100;
    }
    table musics {
        key = {
            (!!!clickb ? (pass ? 8w61 : (!!(hdr.eth_hdr.eth_type != 8w50) ? hdr.thes.firs : 8w111))[7:0] : 8w153): exact @name("produc");
        }
        actions = {
            state();
            price();
        }
        implementation = hash_table(10);
    }
    table should {
        key = {
        }
        actions = {
        }
    }
    apply {
	pass = true;
        const bit<4> system = 7w87[5:2] - 4w3;
        price();
        clickb = !pass;
        hdr.thes.padding = 4w6;
        clickb = !musics.apply().hit;
    }
}

ebpfFilter(prs(), pipe()) main;
