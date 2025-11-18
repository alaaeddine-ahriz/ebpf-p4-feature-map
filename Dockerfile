# --------------------------------------
# Stage 1: System dependencies
# --------------------------------------
FROM ubuntu:22.04 AS base

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y git make curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /home

# --------------------------------------
# Stage 2: Clone repo
# --------------------------------------
FROM base AS source

RUN git clone https://github.com/alaaeddine-ahriz/ebpf-p4-feature-map.git

WORKDIR /home/ebpf-p4-feature-map

RUN git submodule update --init --recursive

# ---------------------------------------
# Stage 3: P4Cherry dependencies
# ---------------------------------------
FROM source AS opambase

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul

RUN apt-get update && \
    apt-get install -y opam libgmp-dev pkg-config && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Initialize opam
RUN opam init --disable-sandboxing --auto-setup && \
    opam switch create 5.1.0 && \
    eval $(opam env) && \
    opam install dune menhir bignum core core_unix bisect_ppx -y

# Set opam environment permanently
ENV OPAM_SWITCH_PREFIX=/root/.opam/5.1.0
ENV PATH=$OPAM_SWITCH_PREFIX/bin:$PATH
ENV CAML_LD_LIBRARY_PATH=$OPAM_SWITCH_PREFIX/lib/stublibs:$OPAM_SWITCH_PREFIX/lib/ocaml/stublibs:$OPAM_SWITCH_PREFIX/lib/ocaml

# ---------------------------------------
# Stage 4: Build P4Cherry
# ---------------------------------------
FROM opambase AS p4cherrybase

WORKDIR /home/ebpf-p4-feature-map/p4cherry

RUN make build-p4 && \
    chmod a+x ./p4cherry

# --------------------------------------
# Stage 5: P4C dependencies
# --------------------------------------
FROM opambase AS p4cbase
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
    sudo bison build-essential cmake curl flex g++ git lld \
    libboost-dev libboost-graph-dev libboost-iostreams-dev \
    libfl-dev ninja-build pkg-config python3 python3-pip \
    python3-setuptools tcpdump wget ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# ---------------------------------------
# Stage 7: Build P4C
# ---------------------------------------
WORKDIR /home/ebpf-p4-feature-map/p4c/build
RUN cmake -G "Unix Makefiles" .. \
    -DENABLE_BMV2=OFF \
    -DENABLE_EBPF=ON \
    -DENABLE_P4TC=OFF \
    -DENABLE_UBPF=OFF \
    -DENABLE_DPDK=OFF \
    -DENABLE_TEST_TOOLS=ON \
    -DENABLE_GTESTS=OFF \
RUN make -j$(nproc) VERBOSE=1
RUN make install .

RUN pip3 install gcovr
WORKDIR /home/ebpf-p4-feature-map
