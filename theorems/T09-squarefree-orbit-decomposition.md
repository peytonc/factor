---
id: T09
type: theorem
title: Square-Free Modular Orbit Decomposition
slug: squarefree-orbit-decomposition
depends_on: [T06, T08]
notation: ../glossary.md
variables: [M, O_M, O_pi, Phi]
status: proven
proof_file: ../proofs/T09-squarefree-orbit-decomposition-proof.md
---

# T09 — Square-Free Modular Orbit Decomposition

> For square-free M, the orbit is isomorphic to the Cartesian product of its prime orbits (CRT).

## Definitions

- Let `M` be any odd square-free integer with the prime factorization `M = pi_1 * pi_2 * ... * pi_n`, where pi_i are distinct primes.
- Let `O_M = Orbit(M)` be the set of reachable states in the PPT graph modulo M.
- Let `O_(p_i) = Orbit(p_i)` be the set of reachable states modulo the prime factor p_i.
- Let `Phi : O_M -> O_(p_1) x ... x O_(p_n)` be the canonical projection map `v |-> (v mod p_1, ..., v mod p_n)`.
- `O_M ≅ prod O_(p_i)` for `i = 1..n` is the modular orbit decomposition.
- `|O_M| = prod |O_(p_i)| = prod (p_i^2 - 1)/2` for `i = 1..n` is the modular orbit cardinality.

## Statement

The modular orbit of a square-free modulus M is isomorphic to the Cartesian product of the modular orbits of its prime factors. When M has no repeated prime factors, the global structure of the orbit space is uniquely determined by the atomic structures of its prime factors acting independently.

**Corollary.** Since the generators {A, B, C} are elements of GL(3, Z), their inverses {A^-1, B^-1, C^-1} are also integer matrices. Therefore the isomorphism Phi preserves both forward transitions (`v_child = G . v_parent`) and inverse transitions (`v_parent = G^-1 . v_child`). The predecessors of a state modulo M are uniquely determined by the predecessors of its prime projections.
