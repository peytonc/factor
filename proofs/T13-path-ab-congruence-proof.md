---
id: T13
type: proof
title: Path A/B Modular Congruence (Proof)
slug: path-ab-congruence-proof
proves: T13
depends_on: [T11]
status: proven
theorem_file: ../theorems/T13-path-ab-congruence.md
---

# T13 — Path A/B Modular Congruence (Proof)

> Proof of [T13 — Path A/B Modular Congruence](../theorems/T13-path-ab-congruence.md).

## Argument

Consider the base case at the divergence. By Theorem 11, the difference between the immediate children is `v_B - v_A = b_parent * delta_b`. Since `delta_b = [2, 6, 4]^T` contains only even integers, every component of the difference vector is a multiple of `2*b_parent`. Thus the immediate children are congruent modulo 2*b_parent.

By the property of linear modular arithmetic `v_(k+1) = G * v_k ≡ G * w_k = w_(k+1) (mod 2*b_parent)`. Since the base case is congruent, and the transition preserves congruence, the relationship holds for all subsequent descendants in the path.

## Cited Results

- [T11 — Sibling Divergence](../theorems/T11-sibling-divergence.md)

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
