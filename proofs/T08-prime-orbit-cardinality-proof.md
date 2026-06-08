---
id: T08
type: proof
title: Prime Modular Orbit Cardinality (Proof)
slug: prime-orbit-cardinality-proof
proves: T08
depends_on: [T06, T07]
status: proven
theorem_file: ../theorems/T08-prime-orbit-cardinality.md
---

# T08 — Prime Modular Orbit Cardinality (Proof)

> Proof of [T08 — Prime Modular Orbit Cardinality](../theorems/T08-prime-orbit-cardinality.md).

## Argument

The total number of parameter pairs (p, q) in the 2D space modulo M is M^2. Excluding the zero vector (0, 0) leaves M^2 - 1 pairs. Since M is an odd prime, (p, q) is never equal to (-p, -q) for any non-zero pair.

For the zero residue (v[2] ≡ 0), this implies the product of factors `pq ≡ 0`. Since M is prime, either p or q must be 0. Geometrically this corresponds to the axes of the (p, q) parameter space. There are M-1 vectors on the p-axis and M-1 on the q-axis. Summing and adjusting for sign equivalence yields M-1 states.

For any non-zero residue k, fixing one coordinate p (M-1 choices) uniquely determines q (since `q = k p^-1`). This results in M-1 vectors, which form (M-1)/2 sign-invariant states.

## Cited Results

- [T06 — Modular Orbit Graph (Finite State Machine)](../theorems/T06-modular-orbit-graph.md)
- [T07 — Prime Modular Axis Alignment](../theorems/T07-prime-axis-alignment.md)

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
