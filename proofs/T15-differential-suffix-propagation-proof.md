---
id: T15
type: proof
title: Differential Suffix Propagation (Proof)
slug: differential-suffix-propagation-proof
proves: T15
depends_on: [T11]
status: proven
theorem_file: ../theorems/T15-differential-suffix-propagation.md
---

# T15 — Differential Suffix Propagation (Proof)

> Proof of [T15 — Differential Suffix Propagation](../theorems/T15-differential-suffix-propagation.md).

## Argument

The leaf vectors are defined as `v_key = R * Q * P * v_root` and `v_shadow = R * Q_swap * P * v_root`. Substituting `P * v_root = v_parent` yields `v_key = R * Q * v_parent` and `v_shadow = R * Q_swap * v_parent`.

Taking the difference yields `v_shadow - v_key = (R * Q_swap * v_parent) - (R * Q * v_parent)`. By the distributive property of matrix multiplication, this factors into `R * (Q_swap - Q) * v_parent`.

By restricting the swap to adjacent branches, the matrix difference term `Delta = Q_swap - Q` evaluates to a signed difference matrix (+/-Delta_a or +/-Delta_b). If the swap involves B and C, then `Delta * v_parent = sigma * Delta_a * v_parent = sigma * alpha * delta_a`. If the swap involves A and B, then `Delta * v_parent = sigma * Delta_b * v_parent = sigma * alpha * delta_b`.

Substituting this back into the difference equation gives `v_shadow - v_key = R * (sigma * alpha * delta)`. Because sigma and alpha are pure scalars, they commute with the matrix multiplication of the suffix sequence R, which results in the exact expression: `v_shadow - v_key = sigma * alpha * (R * delta)`.

## Cited Results

- [T11 — Sibling Divergence](../theorems/T11-sibling-divergence.md)

## Notation

All symbols are defined in [glossary.md](../glossary.md).
