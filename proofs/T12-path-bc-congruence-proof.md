---
id: T12
type: proof
title: Path B/C Modular Congruence (Proof)
slug: path-bc-congruence-proof
proves: T12
depends_on: [T11]
status: proven
theorem_file: ../theorems/T12-path-bc-congruence.md
---

# T12 — Path B/C Modular Congruence (Proof)

> Proof of [T12 — Path B/C Modular Congruence](../theorems/T12-path-bc-congruence.md).

## Argument

Consider the base case at the divergence. By Theorem 11, the difference between the immediate children is `v_B - v_C = a_parent * delta_a`. Since `delta_a = [0, 8, 2]^T` contains only even integers, every component of the difference is a multiple of `2*a_parent`, so `diff ≡ [0, 0, 0]^T (mod 2*a_parent)`. Thus the immediate children are congruent modulo 2*a_parent.

Consider the inductive step for the descendants. Assume two state vectors v_k and w_k are congruent modulo 2*a_parent. By the property of linear modular arithmetic `v_(k+1) = G * v_k ≡ G * w_k = w_(k+1) (mod 2*a_parent)`. Since the base case is congruent, and the transition preserves congruence, the relationship holds for all subsequent descendants in the path.

## Cited Results

- [T11 — Sibling Divergence](../theorems/T11-sibling-divergence.md)

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
