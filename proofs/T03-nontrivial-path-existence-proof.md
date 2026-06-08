---
id: T03
type: proof
title: Non-Trivial Unique Path (Unique Existence) (Proof)
slug: nontrivial-path-existence-proof
proves: T03
depends_on: [T01]
status: proven
theorem_file: ../theorems/T03-nontrivial-path-existence.md
---

# T03 — Non-Trivial Unique Path (Unique Existence) (Proof)

> Proof of [T03 — Non-Trivial Unique Path (Unique Existence)](../theorems/T03-nontrivial-path-existence.md).

## Argument

Euclid's formula states `a = (m - n)(m + n)`.

Setting `m - n = p` and `m + n = q` yields a unique solution for m, n (and thus b, c) for every factor pair.

Because the Berggren tree provides a one-to-one mapping between Primitive Pythagorean Triples and the set of all coprime factor pairs (p, q) of odd parity, and since the semiprime a_target possesses exactly one factor pair where p > 1, there exists exactly one non-trivial path in the tree corresponding to this node.

## Cited Results

- [T01 — Linearized Algebraic State Transition](../theorems/T01-linearized-state-transition.md)

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
