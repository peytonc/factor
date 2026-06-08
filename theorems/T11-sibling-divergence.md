---
id: T11
type: theorem
title: Sibling Divergence
slug: sibling-divergence
depends_on: [T01]
variables: [delta_a, delta_b, a_parent, b_parent]
status: proven
proof_file: ../proofs/T11-sibling-divergence-proof.md
---

# T11 — Sibling Divergence

> The difference between sibling children is strictly linear in the parent's odd leg (B vs C) or even leg (B vs A).

## Definitions

- Let `delta_a = [0, 8, 2]^T` be the odd-leg divergence vector for B vs C.
- Let `delta_b = [2, 6, 4]^T` be the even-leg divergence vector for B vs A.
- Let `a_parent = v_parent[2]` be the odd leg of the parent node.
- Let `b_parent = (v_parent[1] - v_parent[0]) / 2` be the even leg of the parent node.
- `v_B - v_C = a_parent * delta_a`.
- `v_B - v_A = b_parent * delta_b`.

## Statement

The algebraic difference between the B-child and C-child is strictly linear with respect to the parent's odd leg a.

The algebraic difference between the B-child and A-child is strictly linear with respect to the parent's even leg b.

## Proof

See [T11-sibling-divergence-proof.md](../proofs/T11-sibling-divergence-proof.md).

## Dependencies

- [T01 — Linearized Algebraic State Transition](T01-linearized-state-transition.md)

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
