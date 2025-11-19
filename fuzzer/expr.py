"""P4 expression features to test."""

EXPRESSION_FEATURES = {
    # Integer literal
    "INTEGER" : [
        {
            "variant" : "arbitrary",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(bit<8>) 42",
        },
        {
            "variant" : "fixed-signed",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4s2",
        },
        {
            "variant" : "fixed-unsigned",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "8w255",
        },
    ],
    # Default
    "DOTS" : [
        {
            "variant" : "default",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(H1_t) ...",
        },
    ],
    # String literal
    "STRING_LITERAL" : [
        {
            "variant" : "simple",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "const string foo = \"Hello, World!\";",
            "use_c" : "8w1",
        },
    ],
    # Boolean literal
    "TRUE" : [
        {
            "variant" : "true",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "true",
        },
    ],
    "FALSE" : [
        {
            "variant" : "false",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "false",
        },
    ],
    # THIS - can only be def_cined in an extern
    # prefixedNonTypeName
    "prefixedNonTypeName" : [
        {
            "variant" : "dot-prefix",
            "def_g" : "const bit<8> GLOB = 8w255;",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : ".GLOB",
        },
        {
            "variant" : "no-prefix",
            "def_g" : "const bit<8> GLOB = 8w255;",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "GLOB",
        }
    ],
    # expression "[" expression "]"
    "indexAccessExpression" : [
        {
            "variant" : "tuple",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "tuple<bit<8>, int<8>> tup =  { headers.h1.a, headers.h2.c };",
            "use_c" : "tup[0]",
        },
        {
            "variant" : "header-stack",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "H1_t[2] hdr_stack;",
            "use_c" : "hdr_stack[0]",
        }
    ],
    # expression "[" expression ":" expression "]"
    "bitSliceExpression" : [
        {
            "variant" : "simple",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w3[3:0]",
        },
    ],
    # "{" expressionList optTrailingComma "}"
    "bracedListExpression" : [
        {
            "variant" : "simple",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(H1_t) { 1, 2 }",
        },
        {
            "variant" : "trailing-comma",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(H1_t) { 1, 2, }",
        },
        {
            "variant" : "dots",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(H1_t) { 1, ... }",
        },
        {
            "variant" : "dots-trailing-comma",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(H1_t) { 1, ..., }",
        },
        {
            "variant" : "nested",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(Headers_t) { { 1, 2 }, { 3, 4 } }",
        },
    ],
    # "{#}"
    "invalidHeaderExpression" : [
        {
            "variant" : "simple",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(H1_t) {#}",
        },
    ],
    # "{" kvList optTrailingComma "}"
    # "{" kvList "," DOTS optTrailingComma "}"
    "bracedKeyValueListExpression" : [
        {
            "variant" : "simple",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(H1_t) { a = 1, b = 2 }",
        },
        {
            "variant" : "trailing-comma",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(H1_t) { a = 1, b = 2 }",
        },
        {
            "variant" : "dots",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(H1_t) { a = 1, ... }",
        },
        {
            "variant" : "dots-trailing-comma",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(H1_t) { a = 1, ..., }",
        },
        {
            "variant" : "nested",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(Headers_t) { h1 = { a = 1, b = 2 }, h2 = { c = 3, d = 4 } }",
        },
    ],
    # "(" expression ")"
    "parenthesizedExpression" : [
        {
            "variant" : "simple",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "( (bit<8>) 42 )",
        },
        {
            "variant" : "nested",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "( ( (bit<8>) 42 ) )",
        },
    ],
    # "!" "~" "-" "+" expression
    "unaryExpression" : [
        {
            "variant" : "logical-not",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "!true",
        },
        {
            "variant" : "bitwise-not",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "~8w255",
        },
        {
            "variant" : "negation",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "-8s42",
        },
        {
            "variant" : "plus",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "+8s42",
        },
    ],
    # typeName "." member
    "typeAccessExpression" : [
        {
            "variant" : "enum-non-serializable",
            "def_g" : "enum E1_t { A, B, C }",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "E1_t.A",
        },
        {
            "variant" : "enum-serializable",
            "def_g" : "enum bit<8> E2_t { A = 1, B = 2, C = 3 }",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "E2_t.A",
        },
    ],
    # ERROR "." member
    "errorAccessExpression" : [
        {
            "variant" : "simple",
            "def_g" : "error { ERR_A, ERR_B, ERR_C }",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "def_c" : "",
            "use_c" : "error.ERR_A",
        },
    ],
    # expression "." member
    "memberAccessExpression" : [
        {
            "variant" : "header-stack-size",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "H1_t[4] hdr_stack;",
            "use_c" : "hdr_stack.size",
        },
        {
            "variant" : "header-stack-lastIndex",
            "def_g" : "",
            "def_p" : "H1_t[4] hdr_stack;",
            "use_p" : "hdr_stack.lastIndex",
            "def_c" : "",
            "use_c" : "8w1",
        },
        {
            "variant" : "header-stack-last",
            "def_g" : "",
            "def_p" : "H1_t[4] hdr_stack;",
            "use_p" : "hdr_stack.last",
            "def_c" : "",
            "use_c" : "8w1",
        },
        {
            "variant" : "header-stack-next",
            "def_g" : "",
            "def_p" : "H1_t[4] hdr_stack;",
            "use_p" : "hdr_stack.next",
            "def_c" : "",
            "use_c" : "8w1",
        },
        {
            "variant" : "struct",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "headers.h1",
        },
        {
            "variant" : "header",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "headers.h2.c",
        },
        {
            "variant" : "header-union",
            "def_g" : "header_union H_u { H1_t h1; H2_t h2; }",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "H_u hu;",
            "use_c" : "hu.h1",
        },
        {
            "variant" : "table",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : """
                table t {
                    actions = { Reject; }
                    default_action = Reject(true);
                }
            """,
            "use_c" : "t.apply().hit",
        }
    ],
    # expression
    #   "*" "/" "%" "+" "-" "|+|" "|-|" "<<" ">>"
    #   "<=" ">=" "<" ">" "!=" "==" "&" "^" "|" "++" "&&" "||"
    # expression
    "binaryExpression" : [
        {
            "variant" : "mul",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w3 * 4w2",
        },
        {
            "variant" : "div",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "((bit<8>) (6 / 2))",
        },
        {
            "variant" : "mod",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "((bit<8>) (7 % 3))",
        },
        {
            "variant" : "add",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w2 + 4w3",
        },
        {
            "variant" : "sub",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w3 - 4w2",
        },
        {
            "variant" : "add-saturating",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w250 |+| 4w10",
        },
        {
            "variant" : "sub-saturating",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w10 |-| 4w20",
        },
        {
            "variant" : "shift-left",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w2 << 1",
        },
        {
            "variant" : "shift-right",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w8 >> 2",
        },
        {
            "variant" : "le",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w2 <= 4w3",
        },
        {
            "variant" : "ge",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w3 >= 4w2",
        },
        {
            "variant" : "lt",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w2 < 4w3",
        },
        {
            "variant" : "gt",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w3 > 4w2",
        },
        {
            "variant" : "ne",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w2 != 4w3",
        },
        {
            "variant" : "eq",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w2 == 4w2",
        },
        {
            "variant" : "bitwise-and",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w3 & 4w1",
        },
        {
            "variant" : "bitwise-xor",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w3 ^ 4w1",
        },
        {
            "variant" : "bitwise-or",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w3 | 4w1",
        },
        {
            "variant" : "logical-and",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "true && false",
        },
        {
            "variant" : "logical-or",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "true || false",
        },
        {
            "variant" : "concat-integer",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "4w2 ++ 4w3",
        },
        {
            "variant" : "concat-string",
            "def_g" : "const string foo = \"Hello, \" ++ \"World!\";",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "8w1",
        },
    ],
    # expression "?" expression ":" expression
    "ternaryExpression" : [
        {
            "variant" : "simple",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "bool flag;",
            "use_c" : "flag ? 8w1 : 8w2",
        },
    ],
    # expression "<" realTypeArgumentList ">" "(" argumentList ")"
    # expression "(" argumentList ")"
    "callExpression" : [
        {
            "variant" : "simple",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "bit<8> local;",
            "use_c" : "f(local)",
        },
        {
            "variant" : "generic",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "bit<8> local;",
            "use_c" : "f<bit<8>>(local)",
        },
    ],
    # namedType "(" argumentList ")" - no object to construct
    # "(" typeRef ")" expression
    "castExpression" : [
        {
            "variant" : "simple",
            "def_g" : "",
            "def_p" : "",
            "use_p" : "8w1",
            "def_c" : "",
            "use_c" : "(bit<8>) 2",
        },
    ],
}
