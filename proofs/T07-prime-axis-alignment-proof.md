---
id: T07
type: proof
title: Prime Modular Axis Alignment (Proof)
slug: prime-axis-alignment-proof
proves: T07
depends_on: [T06]
status: proven
theorem_file: ../theorems/T07-prime-axis-alignment.md
---

# T07 — Prime Modular Axis Alignment (Proof)

> Proof of [T07 — Prime Modular Axis Alignment](../theorems/T07-prime-axis-alignment.md).

## Argument

The odd leg is defined as `a = pq`. Since M is an odd prime, the ring Z/MZ is a field and contains no zero divisors. By the zero-product property, `a ≡ 0 (mod M)` implies `p ≡ 0` or `q ≡ 0`.

For a PPT, the factors p and q are always coprime with `gcd(p, q) = 1`. Therefore, the prime M cannot divide both p and q simultaneously. Consequently, the state vector cannot be zero on both axes.

## Cited Results

- [T06 — Modular Orbit Graph (Finite State Machine)](../theorems/T06-modular-orbit-graph.md)

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
