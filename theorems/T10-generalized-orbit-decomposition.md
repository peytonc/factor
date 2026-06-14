---
id: T10
type: theorem
title: Generalized Modular Orbit Decomposition
slug: generalized-orbit-decomposition
depends_on: [T09]
notation: ../glossary.md
variables: [M, Q_i, O_M, O_Qi, Phi]
status: proven
proof_file: ../proofs/T10-generalized-orbit-decomposition-proof.md
---

# T10 — Generalized Modular Orbit Decomposition

> Generalizes the decomposition to prime-power (Hensel-lifted) atomic moduli for any odd M.

## Definitions

- Let `M` be any odd integer with the prime factorization `M = pi_1^k_1 * ... * pi_n^k_n`, where pi_i are distinct primes and k_i >= 1.
- Let `Q_i = p_i^k_i` be the maximal prime power component of the modulus.
- Let `O_M = Orbit(M)` be the set of reachable states modulo M.
- Let `O_(Q_i) = Orbit(Q_i)` be the set of reachable states modulo the prime power Q_i.
- Let `Phi : O_M -> O_(Q_1) x ... x O_(Q_n)` be the canonical projection map `v |-> (v mod Q_1, ..., v mod Q_n)`.
- `O_M ≅ prod O_(Q_i)` for `i = 1..n` is the generalized modular orbit decomposition.
- `|O_(Q_i)| = p_i^(2(k_i - 1)) * |O_(p_i)|` is the cardinality of the prime power orbit (derived via Hensel lifting of non-singular points).
- `|O_M| = prod |O_(Q_i)|` for `i = 1..n` is the generalized modular orbit cardinality.

## Statement

Generalizes the decomposition of any odd integer M by treating maximal prime powers (p^k) as atomic moduli. While the orbit modulo a composite M splits into orthogonal components, the orbit modulo a prime power p^k does not split; instead, it is a "lifted" structure of the base prime orbit. The global orbit is isomorphic to the Cartesian product of these prime power orbits.
