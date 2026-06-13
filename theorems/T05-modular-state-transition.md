---
id: T05
type: theorem
title: Modular Algebraic State Transition
slug: modular-state-transition
depends_on: [T01]
notation: ../glossary.md
variables: [v, G, M, d]
status: proven
proof_file: ../proofs/T05-modular-state-transition-proof.md
---

# T05 — Modular Algebraic State Transition

> Projects the infinite tree into a finite ring (Z/MZ)^3 via a ring homomorphism that commutes with the generators.

## Definitions

- Let `M` be an odd integer modulus such that `3 <= M < sqrt(a_target)`.
- Let `v_(d+1) ≡ G_d * v_d (mod M)` define the state transition over the finite ring (Z/MZ)^3.

## Statement

Establishes a homomorphism mapping the infinite PPT tree into a finite directed state-transition graph over Z/MZ. The linear algebraic structure of Theorem 1 is preserved under modular arithmetic. By projecting the state transitions onto a finite ring, the trajectory of any path in the infinite tree is mapped to a path within a bounded modular state space.
