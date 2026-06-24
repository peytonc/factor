---
id: T10
type: proof
title: Generalized Modular Orbit Decomposition (Proof)
slug: generalized-orbit-decomposition-proof
proves: T10
depends_on: [T09]
status: proven
theorem_file: ../theorems/T10-generalized-orbit-decomposition.md
---

# T10 — Generalized Modular Orbit Decomposition (Proof)

> Proof of [T10 — Generalized Modular Orbit Decomposition](../theorems/T10-generalized-orbit-decomposition.md).

## Argument

The CRT applies to rings of the form `Z/MZ ≅ prod Z/(p_i^k_i)Z`, provided the moduli p_i^k_i are pairwise coprime. The transition group G acts independently on each prime power component ring Z/(p_i^k_i)Z. Within each component Z/(p_i^k_i)Z, the orbit cannot be decomposed further using CRT because the factors (p) are not coprime.

The cardinality |O_(Q_i)| is derived by observing that the PPT state vector v is never the zero vector (primitive). The projection from modulo p^k to modulo p is surjective with a fiber size of p^(2(k-1)) for the 2D quadric surface of the PPT orbit, effectively "lifting" the solutions from the base field Z/pZ to the ring Z/p^kZ.

## Cited Results

- [T09 — Square-Free Modular Orbit Decomposition](../theorems/T09-squarefree-orbit-decomposition.md)

## Notation

All symbols are defined in [glossary.md](../glossary.md).
