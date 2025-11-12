"""P4 statement features to test"""

GENERIC_STATEMENT_FEATURES = {
    # Assignment statements
    "assignmentOrMethodCallStatement" : [
        {
            "variant" : "assign-simple",
            "use" : "counter = 8w42;",
        },
        {
            "variant" : "assign-add",
            "use" : "counter += 8w1;",
        },
        {
            "variant" : "assign-sub",
            "use" : "counter -= 8w1;",
        },
        {
            "variant" : "assign-mul",
            "use" : "counter *= 8w2;",
        },
        {
            "variant" : "assign-div",
            "use" : "icounter = (int<8>)((int<16>)icounter / (int<16>)2);",
        },
        {
            "variant" : "assign-mod",
            "use" : "icounter = (int<8>)((int<16>)icounter % (int<16>)2);",
        },
        {
            "variant" : "assign-shl",
            "use" : "counter <<= 1;",
        },
        {
            "variant" : "assign-shr",
            "use" : "counter >>= 1;",
        },
        {
            "variant" : "assign-and",
            "use" : "counter &= 8w15;",
        },
        {
            "variant" : "assign-or",
            "use" : "counter |= 8w240;",
        },
        {
            "variant" : "assign-xor",
            "use" : "counter ^= 8w255;",
        },
        {
            "variant" : "call-momomorphic",
            "use" : "f(counter);",
        },
        {
            "variant" : "call-polymorphic",
            "use" : "g<bit<8>>(counter);",
        },
    ],
    # Conditional statements
    "conditionalStatement" : [
        {
            "variant" : "simple",
            "use" : "if (flag) { counter = 8w1; }",
        },
        {
            "variant" : "else",
            "use" : "if (flag) { counter = 8w1; } else { counter = 8w0; }",
        },
        {
            "variant" : "nested",
            "use" : "if (flag) { if (counter == 8w0) { counter = 8w1; } }",
        },
    ],
    # Empty statement
    "emptyStatement" : [
        {
            "variant" : "simple",
            "use" : ";",
        },
    ],
    # Block statement
    "blockStatement" : [
        {
            "variant" : "simple",
            "use" : "{ bit<8> local = 8w1; }",
        },
        {
            "variant" : "nested",
            "use" : "{ { bit<8> inner = 8w2; } }",
        },
    ],
    # Exit statement
    "exitStatement" : [
        {
            "variant" : "simple",
            "use" : "exit;",
        },
    ],
    # Return statement - only void return in controls
    "returnStatement" : [
        {
            "variant" : "void",
            "use" : "return;",
        },
    ],
    # Switch statements
    "switchStatement" : [
        {
            "variant" : "general-simple",
            "use" : "switch (counter) { 8w0: { } default: { } }",
        },
        {
            "variant" : "general-fallthrough",
            "use" : "switch (counter) { 8w0: 8w1: { } default: { } }",
        },
    ],
    # For loops
    "forStatement" : [
        {
            "variant" : "3-clause",
            "use" : "for (bit<8> i = 0; i < 8w10; i = i + 1) { }",
        },
        {
            "variant" : "in",
            "use" : "for (bit<8> i in 0..10) { }",
        },
    ],
    # Break and continue
    "breakStatement" : [
        {
            "variant" : "simple",
            "use" : "for (bit<8> i = 0; i < 8w10; i = i + 1) { if (i == 8w5) { break; } }",
        },
    ],
    "continueStatement" : [
        {
            "variant" : "simple",
            "use" : "for (bit<8> i = 0; i < 8w10; i = i + 1) { if (i == 8w5) { continue; } }",
        },
    ],
}

PARSER_STATEMENT_FEATURES = {
    # assignmentOrMethodCallStatement
    "assignmentOrMethodCallStatement" : GENERIC_STATEMENT_FEATURES["assignmentOrMethodCallStatement"],
    # directApplication
    "directApplication" : [
        {
            "variant" : "simple",
            "use" : "subprs.apply(p, headers);",
        },
    ],
    # emptyStatement
    "emptyStatement" : GENERIC_STATEMENT_FEATURES["emptyStatement"],
    # variableDeclaration
    "variableDeclaration" : [
        {
            "variant" : "init",
            "use" : "bit<8> local_var = 8w10;",
        },
        {
            "variant" : "non-init",
            "use" : "bit<8> local_var2;",
        },
    ],
    # constantDeclaration
    "constantDeclaration" : [
        {
            "variant" : "simple",
            "use" : "const bit<8> LOCAL_CONST = 255; bit<8> a = LOCAL_CONST;",
        },
    ],
    # parserBlockStatement
    "parserBlockStatement" : [
        {
            "variant" : "simple",
            "use" : "{ bit<8> local = 8w1; }",
        },
        {
            "variant" : "nested",
            "use" : "{ { bit<8> inner = 8w2; } }",
        },
    ],
    # conditionalStatement
    "conditionalStatement" : GENERIC_STATEMENT_FEATURES["conditionalStatement"],
}

CONTROL_STATEMENT_FEATURES = {
    # Variable declaration
    "variableDeclaration" : [
        {
            "variant" : "init",
            "use" : "bit<8> counter = 0;",
        },
        {
            "variant" : "non-init",
            "use" : "bit<8> counter2;",
        },
    ],
    # Constant declaration
    "constantDeclaration" : [
        {
            "variant" : "simple",
            "use" : "const bit<8> LOCAL_CONST = 255; bit<8> a = LOCAL_CONST;",
        },
    ],
    # Assignment or method call statements
    "assignmentOrMethodCallStatement" : GENERIC_STATEMENT_FEATURES["assignmentOrMethodCallStatement"],
    # Direct application
    "directApplication" : [
        {
            "variant" : "simple",
            "use" : "subpipe.apply(headers, flag);",
        },
    ],
    # Conditional statements
    "conditionalStatement" : GENERIC_STATEMENT_FEATURES["conditionalStatement"],
    # Empty statement
    "emptyStatement" : GENERIC_STATEMENT_FEATURES["emptyStatement"],
    # Block statement
    "blockStatement" : GENERIC_STATEMENT_FEATURES["blockStatement"],
    # Exit statement
    "exitStatement" : GENERIC_STATEMENT_FEATURES["exitStatement"],
    # Return statement - only void return in controls
    "returnStatement" : GENERIC_STATEMENT_FEATURES["returnStatement"],
    # Switch statements
    "switchStatement" : GENERIC_STATEMENT_FEATURES["switchStatement"],
    # For loops
    "forStatement" : GENERIC_STATEMENT_FEATURES["forStatement"],
    # Break and continue
    "breakStatement" : GENERIC_STATEMENT_FEATURES["breakStatement"],
    "continueStatement" : GENERIC_STATEMENT_FEATURES["continueStatement"],
}
