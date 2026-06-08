---
id: T17
type: theorem
title: Multi-Swap Differential
slug: multiswap-differential
depends_on: [T11, T15]
variables: [P_key, P_shadow, alpha_m, delta_m, e_m, M_m, sigma_m, R_m, Lambda]
status: proven
proof_file: ../proofs/T17-multiswap-differential-proof.md
---

# T17 — Multi-Swap Differential

> Gives the exact 3D leaf difference for k swaps as a linear combination lying inside the lattice Lambda.

## Definitions

- Let `P_key` be the chronological sequence of generators leading to a leaf node v_key.
- Let `P_shadow` be a parallel sequence differing from P_key by k distinct adjacent matrix swaps at depths d_1, ..., d_k.
- Let `v_parent_m` be the key-path node at depth d_m immediately preceding the m-th swap point.
- Let `alpha_m` be the localized scalar parameter of v_parent_m: if the swap is B <-> C, `alpha_m = a_parent_m` (odd leg); if A <-> B, `alpha_m = b_parent_m` (even leg).
- Let `delta_m` be the constant sibling-divergence vector from Theorem 11: `delta_a = [0, 8, 2]^T` for B<->C; `delta_b = [2, 6, 4]^T` for A<->B.
- Let `e_m = delta_m / 2` be the half-divergence vector: `e_a = [0, 4, 1]^T`, `e_b = [1, 3, 2]^T`.
- Let `M_m = 2*alpha_m` be the modular base scalar for the m-th swap.
- Let `sigma_m` be the directional swap sign: `+1` if (C -> B) or (A -> B); `-1` if (B -> C) or (B -> A).
- Let `R_m` be the shadow-path suffix matrix product of all subsequent generators applied after depth d_m down to the leaf: `R_m = G_n * G_(n-1) * ... * G_(d_m+1)`.
- Let `v_key` and `v_shadow` be the final 3-D algebraic state vectors evaluated at the leaf.

## Statement

The exact 3-dimensional vector difference between the shadow leaf (v_shadow) and the key leaf (v_key) is the linear combination of the independently propagated divergence vectors. Instead of causing chaotic or non-linear divergence, multiple path deviations accumulate via a perfect linear relationship. This exact difference vector lies strictly within the discrete integer vector lattice Lambda defined by the integer span of the propagated half-divergence vectors scaled by M_m:

```
v_shadow - v_key = Sum [ sigma_m * alpha_m * (R_m * delta_m) ]
                 = Sum [ sigma_m * M_m * (R_m * e_m) ]
```

where the summation runs from m = 1 to k, and the vector difference is an explicit element of the lattice `Lambda = Z-span{ M_m * (R_m * e_m) }`.

## Proof

See [T17-multiswap-differential-proof.md](../proofs/T17-multiswap-differential-proof.md).

## Dependencies

- [T11 — Sibling Divergence](T11-sibling-divergence.md)
- [T15 — Differential Suffix Propagation](T15-differential-suffix-propagation.md)

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
