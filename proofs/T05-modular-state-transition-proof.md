---
id: T05
type: proof
title: Modular Algebraic State Transition (Proof)
slug: modular-state-transition-proof
proves: T05
depends_on: [T01]
status: proven
theorem_file: ../theorems/T05-modular-state-transition.md
---

# T05 — Modular Algebraic State Transition (Proof)

> Proof of [T05 — Modular Algebraic State Transition](../theorems/T05-modular-state-transition.md).

## Argument

The state transition `v_(d+1) = G_d * v_d` represents a linear transformation in Z^3. The natural projection map `phi : Z -> Z/MZ` is a ring homomorphism, which implies that it commutes with matrix multiplication, satisfying `phi(G_d * v_d) = phi(G_d) * phi(v_d)`.

By induction, the state at any depth d is given by the composite transformation of the generator sequence modulo M: `v_d ≡ (prod G_i) * v_root (mod M)` for `i = 0..d-1`. Since the cardinality of (Z/MZ)^3 is finite (M^3), the infinite sequence of transitions is mapped into a finite set of states.

## Cited Results

- [T01 — Linearized Algebraic State Transition](../theorems/T01-linearized-state-transition.md)

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
