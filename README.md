# P4 eBPF Backend Analysis

CS540 term project to identify the key limitations and supported features in the eBPF backend of P4.

## P4-to-eBPF Compliant Features

We focus on the *syntactic* features that are supported by the P4 eBPF backend.
By *syntactic*, we mean the P4 grammar constructs that can be successfully recognized by the P4-to-eBPF compiler.
In this study, we do not look into the *semantic* features, i.e., whether the eBPF backend can handle behavior such as packet recirculation.

### Idea - Splicing syntactic features into a holed P4 program

Below is a very simple P4 program for the eBPF backend.

```p4
#include <core.p4>
#include <ebpf_model.p4>

struct Headers_t {}

parser prs(packet_in p, out Headers_t headers) {
    state start {
        transition accept;
    }
}

control pipe(inout Headers_t headers, out bool pass) {
    action Reject(bool rej) {
        pass = rej;
    }

    apply {
        bool x = true;
        Reject(x);
    }
}

ebpfFilter(prs(), pipe()) main;
```

Now consider the grammar of P4 statements, as defined in the P4 specification.

```bison
statement
    : assignmentOrMethodCallStatement
    | conditionalStatement
    | emptyStatement
    | blockStatement
    | exitStatement
    | returnStatement
    | switchStatement
    | loopStatement
    ;
```

We can insert a simple hole into the P4 program above, e.g. (showing the control block only),

```p4
control pipe(inout Headers_t headers, out bool pass) {
    action Reject(bool rej) {
        pass = rej;
    }

    apply {
        /* HOLE */
    }
}
```

And we can implement a very naive P4 statement generator that inserts a hardcoded P4 statement for each grammar rule into the hole.

```
statement
    : assignmentOrMethodCallStatement --> "bit<8> x = 8w0;"
    | conditionalStatement --> "if (true) { } else { }"
    | emptyStatement --> ";"
    | blockStatement --> "{ bit<8> y = 8w1; }"
    | exitStatement --> "exit;"
    | returnStatement --> "return;"
    | switchStatement --> "switch (8w2) { case 8w2: break; }"
    | loopStatement --> "for (bit<8> i = 0; i < 8w3; i = i + 1) { }"
    ;
```

But of course, DCE (dead code elimination) is likely to eliminate most of these naive statements, even before reaching the core P4-to-eBPF compilation stage.
So we would need to later refine the generated statements to make them more meaningful.

I think for now, using hardcoded strings would be a good starting point.
But after we have the basic framework set up, we can consider using a proper P4 AST to generate more complex statements.
Take a look at the [P4 AST in OCaml](https://github.com/kaist-plrg/p4cherry/blob/main/p4/lib/el/ast.ml).
We can re-implement this in Python, for this simple task LLMs will do fine.
