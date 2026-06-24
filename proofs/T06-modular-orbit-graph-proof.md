---
id: T06
type: proof
title: Modular Orbit Graph (Finite State Machine) (Proof)
slug: modular-orbit-graph-proof
proves: T06
depends_on: [T05]
status: proven
theorem_file: ../theorems/T06-modular-orbit-graph.md
---

# T06 — Modular Orbit Graph (Finite State Machine) (Proof)

> Proof of [T06 — Modular Orbit Graph (Finite State Machine)](../theorems/T06-modular-orbit-graph.md).

## Argument

The state space `v = (Z/MZ)^3` has a finite cardinality of M^3. The factor state matrices A, B, and C have determinants of +/-1. Since `gcd(det(G), M) = 1`, these matrices are invertible elements of the group GL(3, Z/MZ). Invertibility ensures that each generator acts as a permutation of the finite state space.

Since all projected PPT nodes share the same quadratic invariant `v[0] . v[1] ≡ v[2]^2 (mod M)`, the group action is restricted to this modular quadric surface. The invertibility of the generators ensures that this surface (the "null-cone") is a single strongly connected orbit.

## Cited Results

- [T05 — Modular Algebraic State Transition](../theorems/T05-modular-state-transition.md)

## Notation

All symbols are defined in [glossary.md](../glossary.md).
