"""P4 declaration features to test."""

TOPLEVEL_DECLARATION_FEATURES = {
    # Constant declarations
    "const_simple": {
        "def": "const bit<8> BIT8_MAX = 255;",
        "use_p": "bit<8> a = BIT8_MAX;",
        "use_c": "bit<8> b = BIT8_MAX;",
        "grammar": "constantDeclaration",
    },
    # Extern declarations
    ## Extern function declarations - can only be defined in the architecture file
    ## Extern object declarations - can only be defined in the architecture file
    # Action declarations
    "action_simple": {
        "def": "action set_to_one(inout bit<8> x) { x = 8w1; }",
        # Action call in parser is disallowed
        "use_p": "",
        "use_c": "set_to_one(tmp);",
        "grammar": "actionDeclaration",
    },
    # Parser declarations
    "parser_simple": {
        "def": """
            parser subprs(packet_in p, out Headers_t h) {
                state start {
                    transition accept;
                }
            }
        """,
        "use_p": "subprs.apply(p, headers);",
        # Parser call in control is disallowed
        "use_c": "",
        "grammar": "parserDeclaration",
    },
    # Control declarations
    "control_simple": {
        "def": """
            control subpipe(inout Headers_t h, out bool pass) {
                action mark_pass(bool p) {
                    pass = p;
                }
                apply {
                    mark_pass(true);
                }
            }
        """,
        # Control call in parser is disallowed
        "use_p": "",
        "use_c": "subpipe.apply(headers, flag);",
        "grammar": "controlDeclaration",
    },
    # Type declarations
    ## Derived type declarations
    ### Header type declarations
    "header_monomorphic": {
        "def": "header H_t { bit<8> field1; bit<16> field2; }",
        "use_p": "H_t h; h.field1 = 8w1; h.field2 = 16w256;",
        "use_c": "H_t h; h.field1 = 8w2; h.field2 = 16w512;",
        "grammar": "headerTypeDeclaration (monomorphic)",
    },
    "header_polymorphic": {
        "def": "header H_t<T, U> { T field1; U field2; }",
        "use_p": "H_t<bit<8>, bit<16>> h; h.field1 = 8w1; h.field2 = 16w256;",
        "use_c": "H_t<bit<8>, bit<16>> h; h.field1 = 8w2; h.field2 = 16w512;",
        "grammar": "headerTypeDeclaration (polymorphic)",
    },
    ### Header union type declarations
    "header_union_monomorphic": {
        "def": """
            header H1_t { bit<8> f1; }
            header H2_t { bit<16> f2; }
            header_union HU_t { H1_t h1; H2_t h2; }
        """,
        "use_p": "HU_t hu; hu.h1.f1 = 8w1;",
        "use_c": "HU_t hu; hu.h2.f2 = 16w256;",
        "grammar": "headerUnionTypeDeclaration (monomorphic)",
    },
    "header_union_polymorphic": {
        "def": """
            header H1_t<T> { T f1; }
            header H2_t<U> { U f2; }
            header_union HU_t<T, U> { H1_t<T> h1; H2_t<U> h2; }
        """,
        "use_p": "HU_t<bit<8>, bit<16>> hu; hu.h1.f1 = 8w1;",
        "use_c": "HU_t<bit<8>, bit<16>> hu; hu.h2.f2 = 16w256;",
        "grammar": "headerUnionTypeDeclaration (polymorphic)",
    },
    ### Struct type declarations
    "struct_monomorphic": {
        "def": "struct S_t { bit<8> a; bit<16> b; }",
        "use_p": "S_t s; s.a = 8w1; s.b = 16w256;",
        "use_c": "S_t s; s.a = 8w2; s.b = 16w512;",
        "grammar": "structTypeDeclaration (monomorphic)",
    },
    "struct_polymorphic": {
        "def": "struct S_t<T, U> { T a; U b; }",
        "use_p": "S_t<bit<8>, bit<16>> s; s.a = 8w1; s.b = 16w256;",
        "use_c": "S_t<bit<8>, bit<16>> s; s.a = 8w2; s.b = 16w512;",
        "grammar": "structTypeDeclaration (polymorphic)",
    },
    ### Enum type declarations
    #### Non-serializable enum type declarations
    "enum_non_serializable": {
        "def": "enum E_t { A, B }",
        "use_p": "E_t e = E_t.A;",
        "use_c": "E_t e = E_t.B;",
        "grammar": "enumTypeDeclaration",
    },
    #### Serializable enum type declarations
    "enum_serializable": {
        "def": "enum bit<8> E2_t { C = 1, D = 2 }",
        "use_p": "E2_t e = E2_t.C;",
        "use_c": "E2_t e = E2_t.D;",
        "grammar": "enumTypeDeclaration (serializable)",
    },
    ## Typedef declarations
    ### Alias typedef declarations
    "typedef_alias": {
        "def": "typedef bit<16> MyBit16;",
        "use_p": "MyBit16 v = 16w100;",
        "use_c": "MyBit16 v = 16w200;",
        "grammar": "typedefDeclaration (alias)",
    },
    ### Derived typedef declarations
    "typedef_derived_header": {
        "def": "typedef header H_t { bit<8> field1; } MyH_t;",
        "use_p": "MyH_t h; h.field1 = 8w1;",
        "use_c": "MyH_t h; h.field1 = 8w2;",
        "grammar": "typedefDeclaration (derived header)",
    },
    "typedef_derived_header_union": {
        "def": """
            header H1_t { bit<8> f1; }
            header H2_t { bit<16> f2; }
            typedef header_union HU_t { H1_t h1; H2_t h2; } MyHU_t;
        """,
        "use_p": "MyHU_t hu; hu.h1.f1 = 8w1;",
        "use_c": "MyHU_t hu; hu.h2.f2 = 16w256;",
        "grammar": "typedefDeclaration (derived header union)",
    },
    "typedef_derived_struct": {
        "def": "typedef struct S_t { bit<8> a; } MyS_t;",
        "use_p": "MyS_t s; s.a = 8w1;",
        "use_c": "MyS_t s; s.a = 8w2;",
        "grammar": "typedefDeclaration (derived struct)",
    },
    "typedef_derived_enum": {
        "def": "typedef enum bit<8> E_t { A = 1, B = 2 } MyE_t;",
        "use_p": "MyE_t e = MyE_t.A;",
        "use_c": "MyE_t e = MyE_t.B;",
        "grammar": "typedefDeclaration (derived enum)",
    },
    ### New type declarations
    "typedef_new": {
        "def": "type bit<16> MyBit16;",
        "use_p": "MyBit16 v = (MyBit16) 16w100;",
        "use_c": "MyBit16 v = (MyBit16) 16w200;",
        "grammar": "typedefDeclaration (new type)",
    },
    ## Parser type declarations - can only be defined in the architecture file
    ## Control type declarations - can only be defined in the architecture file
    ## Package type declarations - can only be defined in the architecture file
    # Instantiations - no instantiable object in the eBPF architecture
    # Error declarations
    "error_simple": {
        "def": "error { ERROR_A, ERROR_B }",
        "use_p": "error e = error.ERROR_A;",
        "use_c": "error e = error.ERROR_B;",
        "grammar": "errorDeclaration",
    },
    # Match kind declarations - can only be defined in the architecture file
    # Function declarations
    "function_simple": {
        "def": """
            bit<8> add_one(in bit<8> x) {
                return x + 8w1;
            }
        """,
        "use_p": "bit<8> y = add_one(tmp);",
        "use_c": "bit<8> z = add_one(tmp);",
        "grammar": "functionDeclaration",
    },
}

PARSER_DECLARATION_FEATURES = {
    # Constant declarations
    "const_simple": {
        "def": "const bit<8> BIT8_MAX = 255;",
        "use": "bit<8> a = BIT8_MAX;",
        "grammar": "constantDeclaration",
    },
    # Instantiations - no instantiable object in the eBPF architecture
    # Variable declarations
    "var_simple": {
        "def": "bit<8> local_var = 8w10;",
        "use": "local_var = local_var + 8w1;",
        "grammar": "variableDeclaration",
    },
    # Value set declarations
    "value_set_simple": {
        "def": "value_set<bit<8>>(4) pvs;",
        "use": "",
        "grammar": "valueSetDeclaration",
    },
}

CONTROL_DECLARATION_FEATURES = {
    # Constant declarations
    "const_simple": {
        "def": "const bit<8> BIT8_MAX = 255;",
        "use": "bit<8> a = BIT8_MAX;",
        "grammar": "constantDeclaration",
    },
    # Action declarations
    "action_simple": {
        "def": "action set_to_one(inout bit<8> x) { x = 8w1; }",
        "use": "set_to_one(counter);",
        "grammar": "actionDeclaration",
    },
    # Table declarations
    "table_simple": {
        "def": """
            table t {
                actions = { Reject; }
                default_action = Reject(true);
            }
        """,
        "use": "t.apply();",
        "grammar": "tableDeclaration",
    },
    # Instantiations - no instantiable object in the eBPF architecture
    # Variable declarations
    "var_simple": {
        "def": "bit<8> local_var = 8w10;",
        "use": "local_var = local_var + 8w1;",
        "grammar": "variableDeclaration",
    },
}

"""P4 statement features to test"""

CONTROL_STATEMENT_FEATURES = {
    # Assignment statements
    "assign_simple": {
        "code": "counter = 8w42;",
        "grammar": "assignmentOrMethodCallStatement",
    },
    "assign_add": {
        "code": "counter += counter + 8w1;",
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
