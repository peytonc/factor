---
id: T04
type: proof
title: Monotonic Growth (Proof)
slug: monotonic-growth-proof
proves: T04
depends_on: [T01]
status: proven
theorem_file: ../theorems/T04-monotonic-growth.md
---

# T04 — Monotonic Growth (Proof)

> Proof of [T04 — Monotonic Growth](../theorems/T04-monotonic-growth.md).

## Argument

Examine the third row of each transition matrix acting on the state vector `v = [p^2, q^2, a]^T`.

For A: `a_A = 2p^2 + a`. Since p >= 1, `a_A > a`.

For B: `a_B = 2q^2 + a`. Since q > 1, `a_B > a`.

For C: `a_C = 2q^2 - a`. Since `a = pq` and q > p, `q^2 > a`. Thus `a_C > 2a - a = a`.

## Cited Results

- [T01 — Linearized Algebraic State Transition](../theorems/T01-linearized-state-transition.md)

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
