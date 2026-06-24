---
id: T14
type: proof
title: Multiple Swaps Modular Congruence (Proof)
slug: multiswap-congruence-proof
proves: T14
depends_on: [T12, T13]
status: proven
theorem_file: ../theorems/T14-multiswap-congruence.md
---

# T14 — Multiple Swaps Modular Congruence (Proof)

> Proof of [T14 — Multiple Swaps Modular Congruence](../theorems/T14-multiswap-congruence.md).

## Argument

From Theorems 12 and 13, a single swap at depth d_i introduces an algebraic difference vector Delta_i that is a scalar multiple of M_i.

Because the state transitions (matrix multiplications) are linear maps over integers, the total difference between the shadow path and the key path at the leaf is the linear sum of the propagated differences from each swap `v_shadow - v_key = Sum [ Phi_i * Delta_i ]` for `i = 1 to k`, where Phi_i represents the transformation product of the subsequent generators along P_shadow after depth d_i.

Since each term (Phi_i * Delta_i) is a multiple of M_i, the total sum is divisible by any integer that divides all M_i simultaneously. Therefore, the tightest guaranteed modular constraint is GCD(M_1, ..., M_k).

## Cited Results

- [T12 — Path B/C Modular Congruence](../theorems/T12-path-bc-congruence.md)
- [T13 — Path A/B Modular Congruence](../theorems/T13-path-ab-congruence.md)

## Notation

All symbols are defined in [glossary.md](../glossary.md).
