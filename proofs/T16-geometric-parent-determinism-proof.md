---
id: T16
type: proof
title: Geometric Parent Determinism (Proof)
slug: geometric-parent-determinism-proof
proves: T16
depends_on: [T01]
status: proven
theorem_file: ../theorems/T16-geometric-parent-determinism.md
---

# T16 — Geometric Parent Determinism (Proof)

> Proof of [T16 — Geometric Parent Determinism](../theorems/T16-geometric-parent-determinism.md).

## Argument

Consider the forward transformations from a parent node (p_parent, q_parent) to a child node (p, q).

The child factors for A are `p = p_parent`, `q = 2 p_parent + q_parent`. The ratio is `lambda = (2 p_parent + q_parent)/p_parent = 2 + q_parent/p_parent`. Since q_parent > p_parent, `q_parent/p_parent > 1`, implying `lambda > 3`.

The child factors for B are `p = q_parent`, `q = 2 q_parent + p_parent`. The ratio is `lambda = (2 q_parent + p_parent)/q_parent = 2 + p_parent/q_parent`. Since `0 < p_parent < q_parent`, the term `p_parent/q_parent in (0, 1)`, implying `2 < lambda < 3`.

The child factors for C are `p = q_parent`, `q = 2 q_parent - p_parent`. The ratio is `lambda = (2 q_parent - p_parent)/q_parent = 2 - p_parent/q_parent`. Since `0 < p_parent < q_parent`, the term `p_parent/q_parent in (0, 1)`, implying `1 < lambda < 2`.

Because the intervals (1, 2), (2, 3), and (3, inf) are disjoint, and lambda = 3 uniquely identifies the root (1, 3), the factor ratio lambda uniquely identifies the generator that created the child.

## Cited Results

- [T01 — Linearized Algebraic State Transition](../theorems/T01-linearized-state-transition.md)

## Notation

All symbols are defined in [glossary.md](../glossary.md).
