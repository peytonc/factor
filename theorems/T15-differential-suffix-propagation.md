---
id: T15
type: theorem
title: Differential Suffix Propagation
slug: differential-suffix-propagation
depends_on: [T11]
notation: ../glossary.md
variables: [P_key, P_shadow, Q, Q_swap, R, v_parent, alpha, delta, sigma]
status: proven
proof_file: ../proofs/T15-differential-suffix-propagation-proof.md
---

# T15 — Differential Suffix Propagation

> Gives the exact single-swap leaf error vector: v_shadow - v_key = sigma * alpha * (R * delta).

## Definitions

- Let `P_key = R * Q * P` be the target matrix sequence leading to a leaf node v_key.
- Let `P_shadow = R * Q_swap * P` be a shadow matrix sequence differing from P_key by a single swap at depth d.
- Let `v_parent = P * v_root` be the parent node at depth d along the key path where the swap occurs.
- Let `(Q, Q_swap)` be an ordered pair of distinct generators restricted to the adjacent branch sets {A, B} or {B, C}.
- Let `R = G_leaf * ... * G_(d+3) * G_(d+2)` be the remaining suffix string of matrices applied after the swap point (maintaining right-to-left multiplication order).
- Let `alpha` be the scalar geometric property of the parent node: if the swap involves B and C, `alpha = a_parent`; if A and B, `alpha = b_parent`.
- Let `delta` be the constant structural divergence vector for the swap type (delta_a for B vs C, delta_b for A vs B).
- Let `sigma` be the directional sign operator: `sigma = 1` if (Q, Q_swap) = (C, B) or (A, B); `sigma = -1` if (Q, Q_swap) = (B, C) or (B, A).
- Let `v_key` and `v_shadow` be the resulting leaf state vectors.

## Statement

Provides an exact linear error vector formula at the leaf level when a single traversal path deviates from a key sequence via an adjacent generator swap. The total algebraic discrepancy at the leaf level (v_shadow - v_key) equals the signed product of the directional operator sigma, the scalar geometric property of the parent node alpha, and the transformation of the structural divergence vector delta under the remaining suffix sequence R. This serves as a global algebraic tracking tool to calculate the structural distance between parallel matrix branches without recomputing entire paths.
