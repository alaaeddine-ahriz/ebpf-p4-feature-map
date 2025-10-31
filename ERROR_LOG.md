## P4 eBPF — Quick Status Log

### Division / Modulo
- True `/` and `%` fail typecheck here (even on `int<N>`). Bitwise stand-ins pass:
  - div2 → `counter >> 1`
  - mod2 → `counter & 1`

### Fuzzer vs manual mismatch
- Fixed: treat stderr as failure; use relative paths to avoid spaces issues.

### Paths with spaces
- Fixed: run with project-root cwd; pass relative paths.

### Parser constraints (current setup)
- Compound ops (e.g. -=) replaced with expanded forms (PASS).
- `for`/`break`/`continue` tested verbatim (currently FAIL here).

---

## Open

### Typecheck errors for division and modulo (still open)
- bit<8> version (example): `counter = counter / 8w2;` → FAIL (coercion).
- int<8>/int<16> casts and temps (several variants) → FAIL (same class of error).
- Working alternatives recorded above; keeping true div/mod as expected FAIL.

### switch with break in case block (addressed by workaround)
- Snippet (original):
```p4
switch (counter) { 8w0: { break; } default: { } }
```
- Error:
```
Error: File output/test_switch_break.p4, line 21, characters 39-40
parser error
```
- Status: avoided for now (no `break` in cases); will revisit accepted form.

### for loops
- Snippet (simple):
```p4
for (bit<8> i = 0; i < 8w10; i = i + 1) { }
```
- Snippet (with body):
```p4
for (bit<8> i = 0; i < 8w5; i = i + 1) { counter = counter + 8w1; }
```
- Snippet (range):
```p4
for (bit<8> i in 0..10) { }
```
- These currently fail to parse with p4cherry here. I keep them to show they fail.

### break / continue inside loop
- Snippet (break):
```p4
for (bit<8> i = 0; i < 8w10; i = i + 1) { if (i == 8w5) { break; } }
```
- Snippet (continue):
```p4
for (bit<8> i = 0; i < 8w10; i = i + 1) { if (i == 8w5) { continue; } }
```
- Error: parser error (kept in suite to document lack of support).

---

## PASS (baseline)
- Assignments, if/else (incl. nested), empty `;`, blocks, exit, return.
- switch without `break` (incl. fallthrough labels).
- Bitwise div/mod stand-ins: `>> 1`, `& 1`.

---

## Next
- Keep true div/mod and loop constructs in the suite (expected FAIL) to track support. @Jaehyun check if they passe the p4c.
- When backend/parser support improves, re-test and update this log.


