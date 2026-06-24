---
id: T11
type: proof
title: Sibling Divergence (Proof)
slug: sibling-divergence-proof
proves: T11
depends_on: [T01]
status: proven
theorem_file: ../theorems/T11-sibling-divergence.md
---

# T11 — Sibling Divergence (Proof)

> Proof of [T11 — Sibling Divergence](../theorems/T11-sibling-divergence.md).

## Argument

The difference matrix between sibling generators is `Delta_a = B - C = [[0,0,0],[0,0,8],[0,0,2]]`. Apply this difference matrix to the current state vector `v = [p^2, q^2, a]^T`, giving `Delta_a * v = [0, 8a, 2a]^T`. Applying this to the parent yields the difference between the immediate children `v_B - v_C = Delta_a * v_parent = [0, 8a, 2a]^T = a_parent * delta_a`.

The difference matrix between sibling generators is `Delta_b = B - A = [[-1,1,0],[-3,3,0],[-2,2,0]]`. Apply this difference matrix to the current state vector `v = [p^2, q^2, a]^T`, giving `Delta_b * v = [2b, 6b, 4b]^T`. Applying this to the parent yields the difference between the immediate children `v_B - v_A = Delta_b * v_parent = [2b, 6b, 4b]^T = b_parent * delta_b`.

## Cited Results

- [T01 — Linearized Algebraic State Transition](../theorems/T01-linearized-state-transition.md)

## Notation

All symbols are defined in [glossary.md](../glossary.md).
