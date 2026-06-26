---
id: T07
type: theorem
title: Prime Modular Axis Alignment
slug: prime-axis-alignment
depends_on: [T06]
notation: ../glossary.md
variables: [M, v, B_M, I_M, X_axes, p, q, a]
status: proven
proof_file: ../proofs/T07-prime-axis-alignment-proof.md
---

# T07 — Prime Modular Axis Alignment

> For prime M, a zero odd-leg residue holds iff exactly one factor (p or q) is congruent to zero.

## Definitions

- Let `M` be an odd prime modulus.
- Let `v = [p^2, q^2, a]^T in Orbit(M)` be a state vector in the modular orbit Orbit(M).
- Let `B_M = { v in Orbit(M) : v[2] ≡ 0 (mod M) }` be the set of axis nodes.
- Let `I_M = { v in Orbit(M) : v[2] ≢ 0 (mod M) }` be the set of interior nodes.
- Let `X_axes = { v in Orbit(M) : v[0] ≡ 0 (mod M) XOR v[1] ≡ 0 (mod M) }` be the set of nodes lying strictly on exactly one geometric axis of the parameter space.
- `v in B_M  <=>  v in X_axes` asserts that a node has a modular odd leg of zero iff exactly one of its generating factors (p or q) is congruent to zero.
- `v in I_M  =>  p ≢ 0 (mod M) AND q ≢ 0 (mod M)` asserts that a non-zero odd leg forces both factors p and q to be non-zero.

## Statement

A strict geometric equivalence exists between the zero-residue of the odd leg (a) and the geometric axes of the parameter space (p, q) for prime moduli. It partitions the modular graph into interior nodes (where p, q != 0) and axis nodes. The origin point p ≡ 0 and q ≡ 0 is unreachable due to coprimality.
