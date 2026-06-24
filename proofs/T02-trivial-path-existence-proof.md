---
id: T02
type: proof
title: Trivial Path (Unique Existence) (Proof)
slug: trivial-path-existence-proof
proves: T02
depends_on: [T01]
status: proven
theorem_file: ../theorems/T02-trivial-path-existence.md
---

# T02 — Trivial Path (Unique Existence) (Proof)

> Proof of [T02 — Trivial Path (Unique Existence)](../theorems/T02-trivial-path-existence.md).

## Argument

From Theorem 1, row 3 of Matrix A implies `a_next = a + 2p^2`. The first row of Matrix A (`[1, 0, 0]`) ensures `p_next^2 = p^2`. Since `p_root^2 = 1`, p^2 is invariant. Substituting this into the recurrence yields `a_next = a + 2`.

## Cited Results

- [T01 — Linearized Algebraic State Transition](../theorems/T01-linearized-state-transition.md)

## Notation

All symbols are defined in [glossary.md](../glossary.md).
