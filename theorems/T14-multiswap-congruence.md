---
id: T14
type: theorem
title: Multiple Swaps Modular Congruence
slug: multiswap-congruence
depends_on: [T12, T13]
notation: ../glossary.md
variables: [P_key, P_shadow, mu__i, a_parent, b_parent]
status: proven
proof_file: ../proofs/T14-multiswap-congruence-proof.md
---

# T14 — Multiple Swaps Modular Congruence

> After k swaps, the leaf stays congruent to the key path modulo the GCD of the per-swap moduli.

## Definitions

- Let `P_key` be the target sequence of generators leading to a leaf node v_key.
- Let `P_shadow` be a sequence differing from P_key by k distinct swaps (restricted to A vs B or B vs C) at depths d_1, ..., d_k.
- Let `v_parent_i` be the parent node at depth d_i along the key path where the i-th swap occurs.
- Let `mu_i` be the modular consequence of the i-th swap: if the swap is B vs C, `mu_i = 2*a_parent_i`; if the swap is A vs B, `mu_i = 2*b_parent_i`.
- Let `v_key` and `v_shadow` be the resulting leaf state vectors.
- `v_shadow ≡ v_key (mod GCD(mu_1, mu_2, ..., mu_k))`.

## Statement

When a traversal path deviates from a key path via multiple substitutions (swaps) at different depths, the resulting leaf node maintains a congruence relative to the key node. The modulus of this congruence is the GCD of the moduli associated with each individual swap. The shadow path remains "locked" to the key path within the lattice grid defined by the shared divisors of the divergence points.
