"""P4 declaration features to test."""

TOPLEVEL_DECLARATION_FEATURES = {
    # Constant declarations
    "constantDeclaration" : [
        {
            "variant" : "simple",
            "def" : "const bit<8> BIT8_MAX = 255;",
            "use_p" : "bit<8> a = BIT8_MAX;",
            "use_c" : "bit<8> b = BIT8_MAX;"
        },
    ],
    # Extern declarations
    ## Extern function declarations - can only be defined in the architecture file
    ## Extern object declarations - can only be defined in the architecture file
    # Action declarations
    "actionDeclaration": [
        {
            "variant" : "simple",
            "def" : "action set_to_one(inout bit<8> x) { x = 8w1; }",
            # Action call in parser is disallowed
            "use_p" : "",
            "use_c" : "set_to_one(tmp);",
        },
    ],
    # Parser declarations
    "parserDeclaration": [
        {
            "variant" : "simple",
            "def" : """
                parser subprs(packet_in p, out Headers_t h) {
                    state start {
                        transition accept;
                    }
                }
            """,
            "use_p" : "subprs.apply(p, headers);",
            # Parser call in control is disallowed
            "use_c" : "",
        },
    ],
    # Control declarations
    "controlDeclaration": [
        {
            "variant" : "simple",
            "def" : """
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
            "use_p" : "",
            "use_c" : "subpipe.apply(headers, flag);",
        },
    ],
    # Type declarations
    ## Derived type declarations
    ### Header type declarations
    "headerTypeDeclaration": [
        {
            "variant" : "monomorphic",
            "def" : "header H_t { bit<8> field1; bit<16> field2; }",
            "use_p" : "H_t h; h.field1 = 8w1; h.field2 = 16w256;",
            "use_c" : "H_t h; h.field1 = 8w2; h.field2 = 16w512;",
        },
        {
            "variant" : "polymorphic",
            "def" : "header H_t<T, U> { T field1; U field2; }",
            "use_p" : "H_t<bit<8>, bit<16>> h; h.field1 = 8w1; h.field2 = 16w256;",
            "use_c" : "H_t<bit<8>, bit<16>> h; h.field1 = 8w2; h.field2 = 16w512;",
        },
    ],
    ### Header union type declarations
    "headerUnionTypeDeclaration": [
        {
            "variant" : "monomorphic",
            "def" : """
                header H1_t { bit<8> f1; }
                header H2_t { bit<16> f2; }
                header_union HU_t { H1_t h1; H2_t h2; }
            """,
            "use_p" : "HU_t hu; hu.h1.f1 = 8w1;",
            "use_c" : "HU_t hu; hu.h2.f2 = 16w256;",
        },
        {
            "variant" : "polymorphic",
            "def" : """
                header H1_t<T> { T f1; }
                header H2_t<U> { U f2; }
                header_union HU_t<T, U> { H1_t<T> h1; H2_t<U> h2; }
            """,
            "use_p" : "HU_t<bit<8>, bit<16>> hu; hu.h1.f1 = 8w1;",
            "use_c" : "HU_t<bit<8>, bit<16>> hu; hu.h2.f2 = 16w256;",
        },
    ],
    ### Struct type declarations
    "structTypeDeclaration": [
        {
            "variant" : "monomorphic",
            "def" : "struct S_t { bit<8> a; bit<16> b; }",
            "use_p" : "S_t s; s.a = 8w1; s.b = 16w256;",
            "use_c" : "S_t s; s.a = 8w2; s.b = 16w512;",
        },
        {
            "variant" : "polymorphic",
            "def" : "struct S_t<T, U> { T a; U b; }",
            "use_p" : "S_t<bit<8>, bit<16>> s; s.a = 8w1; s.b = 16w256;",
            "use_c" : "S_t<bit<8>, bit<16>> s; s.a = 8w2; s.b = 16w512;",
        },
    ],
    ### Enum type declarations
    "enumTypeDeclaration": [
        {
            "variant" : "non-serializable",
            "def" : "enum E_t { A, B }",
            "use_p" : "E_t e = E_t.A;",
            "use_c" : "E_t e = E_t.B;",
        },
        {
            "variant" : "serializable",
            "def" : "enum bit<8> E2_t { C = 1, D = 2 }",
            "use_p" : "E2_t e = E2_t.C;",
            "use_c" : "E2_t e = E2_t.D;",
        },
    ],
    ## Typedef declarations
    "typedefDeclaration": [
        {
            "variant" : "typedef-base",
            "def" : "typedef bit<16> MyBit16;",
            "use_p" : "MyBit16 v = 16w100;",
            "use_c" : "MyBit16 v = 16w200;",
        },
        {
            "variant" : "typedef-derived-header",
            "def" : "typedef header H_t { bit<8> field1; } MyH_t;",
            "use_p" : "MyH_t h; h.field1 = 8w1;",
            "use_c" : "MyH_t h; h.field1 = 8w2;",
        },
        {
            "variant" : "typedef-derived-header-union",
            "def" : """
                header H1_t { bit<8> f1; }
                header H2_t { bit<16> f2; }
                typedef header_union HU_t { H1_t h1; H2_t h2; } MyHU_t;
            """,
            "use_p" : "MyHU_t hu; hu.h1.f1 = 8w1;",
            "use_c" : "MyHU_t hu; hu.h2.f2 = 16w256;",
        },
        {
            "variant" : "typedef-derived-struct",
            "def" : "typedef struct S_t { bit<8> a; } MyS_t;",
            "use_p" : "MyS_t s; s.a = 8w1;",
            "use_c" : "MyS_t s; s.a = 8w2;",
        },
        {
            "variant" : "typedef-derived-enum",
            "def" : "typedef enum bit<8> E_t { A = 1, B = 2 } MyE_t;",
            "use_p" : "MyE_t e = MyE_t.A;",
            "use_c" : "MyE_t e = MyE_t.B;",
        },
        {
            "variant" : "type",
            "def" : "type bit<16> MyBit16;",
            "use_p" : "MyBit16 v = (MyBit16) 16w100;",
            "use_c" : "MyBit16 v = (MyBit16) 16w200;",
        },
    ],
    ## Parser type declarations - can only be defined in the architecture file
    ## Control type declarations - can only be defined in the architecture file
    ## Package type declarations - can only be defined in the architecture file
    # Instantiations - no instantiable object in the eBPF architecture
    # Error declarations
    "errorDeclaration" : [ 
        {
            "variant" : "simple",
            "def" : "error { ERROR_A, ERROR_B }",
            "use_p" : "error e = error.ERROR_A;",
            "use_c" : "error e = error.ERROR_B;",
        },
    ],
    # Match kind declarations - can only be defined in the architecture file
    # Function declarations
    "functionDeclaration" :  [
        {
            "variant" : "simple",
            "def" : """
                bit<8> add_one(in bit<8> x) {
                    return x + 8w1;
                }
            """,
            "use_p" : "bit<8> y = add_one(tmp);",
            "use_c" : "bit<8> z = add_one(tmp);",
        },
    ],
}

PARSER_DECLARATION_FEATURES = {
    # Constant declarations
    "constantDeclaration" : [
        {
            "variant" : "simple",
            "def" : "const bit<8> BIT8_MAX = 255;",
            "use" : "bit<8> a = BIT8_MAX;",
        },
    ],
    # Instantiations - no instantiable object in the eBPF architecture
    # Variable declarations
    "variableDeclaration" : [
        {
            "variant" : "simple",
            "def" : "bit<8> local_var = 8w10;",
            "use" : "local_var = local_var + 8w1;",
        },
    ],
    # Value set declarations
    "valueSetDeclaration" : [
        {
            "variant" : "simple",
            "def" : "value_set<bit<8>>(4) pvs;",
            "use" : "",
        },
    ],
}

CONTROL_DECLARATION_FEATURES = {
    # Constant declarations
    "constantDeclaration" : [
        {
            "variant" : "simple",
            "def" : "const bit<8> BIT8_MAX = 255;",
            "use" : "bit<8> a = BIT8_MAX;",
        },
    ],
    # Action declarations
    "actionDeclaration" : [
        {
            "variant" : "simple",
            "def" : "action set_to_one(inout bit<8> x) { x = 8w1; }",
            "use" : "set_to_one(counter);",
        },
    ],
    # Table declarations
    "tableDeclaration" : [
        {
            "variant" : "simple",
            "def" : """
                table t {
                    actions = { Reject; }
                    default_action = Reject(true);
                }
            """,
            "use" : "t.apply();",
        },
    ],
    # Instantiations - no instantiable object in the eBPF architecture
    # Variable declarations
    "variableDeclaration" : [
        {
            "variant" : "simple",
            "def" : "bit<8> local_var = 8w10;",
            "use" : "local_var = local_var + 8w1;",
        },
    ],
}
