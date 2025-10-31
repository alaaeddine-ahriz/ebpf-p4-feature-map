"""P4 statement features to test."""


STATEMENT_FEATURES = {
    # Assignment statements
    "assign_simple": {
        "code": "bit<8> y = 8w0;",
        "grammar": "assignmentOrMethodCallStatement",
    },
    "assign_to_var": {
        "code": "counter = 8w42;",
        "grammar": "assignmentOrMethodCallStatement",
    },
    "assign_add": {
        "code": "counter = counter + 8w1;",
        "grammar": "assignmentOrMethodCallStatement (expanded +=)",
    },
    "assign_sub": {
        "code": "counter = counter - 8w1;",
        "grammar": "assignmentOrMethodCallStatement (expanded -=)",
    },
    "assign_mul": {
        "code": "counter = counter * 8w2;",
        "grammar": "assignmentOrMethodCallStatement (expanded *=)",
    },
    "assign_div": {
        "code": "int<16> t = (int<16>)icounter; t = t / (int<16>)2; icounter = (int<8>)t;",
        "grammar": "assignmentOrMethodCallStatement (icounter div via int<16>)",
    },
    "assign_mod": {
        "code": "int<16> t = (int<16>)icounter; t = t % (int<16>)2; icounter = (int<8>)t;",
        "grammar": "assignmentOrMethodCallStatement (icounter mod via int<16>)",
    },
    "assign_shl": {
        "code": "counter = counter << 1;",
        "grammar": "assignmentOrMethodCallStatement (expanded <<=)",
    },
    "assign_shr": {
        "code": "counter = counter >> 1;",
        "grammar": "assignmentOrMethodCallStatement (expanded >>=)",
    },
    "assign_and": {
        "code": "counter = counter & 8w15;",
        "grammar": "assignmentOrMethodCallStatement (expanded &=)",
    },
    "assign_or": {
        "code": "counter = counter | 8w240;",
        "grammar": "assignmentOrMethodCallStatement (expanded |=)",
    },
    "assign_xor": {
        "code": "counter = counter ^ 8w255;",
        "grammar": "assignmentOrMethodCallStatement (expanded ^=)",
    },

    # Conditional statements
    "if_simple": {
        "code": "if (true) { }",
        "grammar": "conditionalStatement",
    },
    "if_else": {
        "code": "if (flag) { counter = 8w1; } else { counter = 8w0; }",
        "grammar": "conditionalStatement",
    },
    "if_nested": {
        "code": "if (flag) { if (counter == 8w0) { counter = 8w1; } }",
        "grammar": "conditionalStatement",
    },

    # Empty statement
    "empty": {
        "code": ";",
        "grammar": "emptyStatement",
    },

    # Block statement
    "block_simple": {
        "code": "{ bit<8> local = 8w1; }",
        "grammar": "blockStatement",
    },
    "block_nested": {
        "code": "{ { bit<8> inner = 8w2; } }",
        "grammar": "blockStatement",
    },

    # Exit statement
    "exit": {
        "code": "exit;",
        "grammar": "exitStatement",
    },

    # Return statement
    "return_void": {
        "code": "return;",
        "grammar": "returnStatement",
    },

    # Switch statements
    "switch_simple": {
        "code": "switch (counter) { 8w0: { } default: { } }",
        "grammar": "switchStatement",
    },
    "switch_break": {
        "code": "switch (counter) { 8w0: { } default: { } }",
        "grammar": "switchStatement (no break)",
    },
    "switch_fallthrough": {
        "code": "switch (counter) { 8w0: 8w1: { } default: { } }",
        "grammar": "switchStatement (fallthrough)",
    },

    # For loops
    "for_simple": {
        "code": "for (bit<8> i = 0; i < 8w10; i = i + 1) { }",
        "grammar": "forStatement",
    },
    "for_with_body": {
        "code": "for (bit<8> i = 0; i < 8w5; i = i + 1) { counter = counter + 8w1; }",
        "grammar": "forStatement (with body)",
    },
    "for_range": {
        "code": "for (bit<8> i in 0..10) { }",
        "grammar": "forStatement (range)",
    },

    # Break and continue
    "break": {
        "code": "for (bit<8> i = 0; i < 8w10; i = i + 1) { if (i == 8w5) { break; } }",
        "grammar": "breakStatement",
    },
    "continue": {
        "code": "for (bit<8> i = 0; i < 8w10; i = i + 1) { if (i == 8w5) { continue; } }",
        "grammar": "continueStatement",
    },
}


