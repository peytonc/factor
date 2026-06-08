---
id: T17
type: proof
title: Multi-Swap Differential (Proof)
slug: multiswap-differential-proof
proves: T17
depends_on: [T11, T15]
status: proven
theorem_file: ../theorems/T17-multiswap-differential.md
---

# T17 — Multi-Swap Differential (Proof)

> Proof of [T17 — Multi-Swap Differential](../theorems/T17-multiswap-differential.md).

## Argument

According to Theorem 11, a single isolated matrix swap at depth d_m introduces an instantaneous error vector between the two paths equal to (sigma_m * alpha_m * delta_m). Because the subsequent steps along the tree are governed by linear transformations represented by the generator matrices, this error vector propagates downstream to the leaf via direct matrix multiplication by the suffix product R_m, resulting in the leaf-level contribution: `sigma_m * alpha_m * R_m * delta_m`.

Since matrix multiplication is fully distributive over vector addition, the cumulative downstream impact of k distinct localized swaps is the exact linear sum of their individual propagated error vectors.

Substituting `delta_m = 2 * e_m` into the expression allows the scalar 2 to be grouped with alpha_m, forming `M_m = 2 * alpha_m`. This shows that every individual vector term in the sum is a strict integer multiple of M_m, meaning the final total vector difference is a precise integer linear combination of the basis vectors `M_m * (R_m * e_m)`, proving strict membership in the lattice Lambda.

## Cited Results

- [T11 — Sibling Divergence](../theorems/T11-sibling-divergence.md)
- [T15 — Differential Suffix Propagation](../theorems/T15-differential-suffix-propagation.md)

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
