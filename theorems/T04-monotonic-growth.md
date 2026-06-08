---
id: T04
type: theorem
title: Monotonic Growth
slug: monotonic-growth
depends_on: [T01]
variables: [v, G, a, p, q]
status: proven
proof_file: ../proofs/T04-monotonic-growth-proof.md
---

# T04 — Monotonic Growth

> The odd leg a strictly increases at every transition, guaranteeing a monotonic descent.

## Definitions

- Let `v_(d+1) = G_d * v_d` be the state transition to a child node at depth d+1.
- Let `a_d = v_d[2]` be the odd leg at depth d.
- `a_(d+1) > a_d` is the growth inequality.

## Statement

The odd leg a_d strictly increases at every step of the tree.

## Proof

See [T04-monotonic-growth-proof.md](../proofs/T04-monotonic-growth-proof.md).

## Dependencies

- [T01 — Linearized Algebraic State Transition](T01-linearized-state-transition.md)

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
