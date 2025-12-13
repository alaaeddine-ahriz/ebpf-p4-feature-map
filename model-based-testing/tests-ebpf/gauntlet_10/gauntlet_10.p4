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

header aboutc {
    bit<4> sear;
    bit<4> padding;
}

struct Headers {
    ethernet_t eth_hdr;
    ethernet_t othe;
    aboutc     whic;
    aboutc     thei;
    aboutc     ther;
    aboutc     cont;
}

parser prs(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.othe);
        pkt.extract(hdr.whic);
        pkt.extract(hdr.thei);
        pkt.extract(hdr.ther);
        pkt.extract(hdr.cont);
        transition accept;
    }
}

control pipe(inout Headers hdr, out bool pass) {
    bit<4> busine = 1;
    ethernet_t online = { hdr.eth_hdr.src_addr * (hdr.eth_hdr.dst_addr ^ 8w159), ~(bit<8>)((8w222 - hdr.eth_hdr.eth_type) * hdr.othe.src_addr), hdr.othe.eth_type };
    action first(bit<4> woul) {
        online.dst_addr = (true ? 8w11 : online.eth_type);
        pass = (bit<3>)woul == 3 | 5;
        hdr.eth_hdr.dst_addr = 8w144;
        pass = true;
    }
    action servi(bit<8> thes) {
        pass = !(!false && false);
        hdr.thei.sear = 4w9;
        online.src_addr = 8w104;
        hdr.thei.sear = (false ? (bit<4>)4w6 : (bit<4>)-28);
        pass = true;
        hdr.whic.sear = hdr.cont.sear;
    }
    table clickW {
        key = {
        }
        actions = {
            first();
        }
    }
    table people {
        key = {
            hdr.eth_hdr.eth_type     : exact @name("servic");
            hdr.othe.dst_addr - 8w186: exact @name("priceh");
        }
        actions = {
            first();
            servi();
        }
    }
    apply {
        servi(((bit<8>)66)[7:0]);
        online.src_addr[6:3] = hdr.cont.sear - 4w5 | 4w5;
        pass = pass;
        hdr.ther.sear = 4w3 + (false ? hdr.whic.padding : (pass ? hdr.whic.padding : 4w12)) | hdr.cont.padding;
    }
}

ebpfFilter(prs(), pipe()) main;
