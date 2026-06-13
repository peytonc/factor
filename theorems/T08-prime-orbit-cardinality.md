---
id: T08
type: theorem
title: Prime Modular Orbit Cardinality
slug: prime-orbit-cardinality
depends_on: [T06, T07]
notation: ../glossary.md
variables: [M, Orbit_M]
status: proven
proof_file: ../proofs/T08-prime-orbit-cardinality-proof.md
---

# T08 — Prime Modular Orbit Cardinality

> Gives exact state counts per odd-leg residue class in the prime modular orbit.

## Definitions

- Let `M` be an odd prime modulus.
- `|Orbit(M)| = (M^2 - 1) / 2` is the cardinality of reachable states modulo M.
- `|{ v in Orbit(M) : v[2] ≡ 0 (mod M) }| = M - 1` is the count of reachable states with v[2] ≡ 0.
- `|{ v in Orbit(M) : v[2] ≡ k (mod M) }| = (M - 1)/2` for each `k in {1, ..., M-1}` is the count for each non-zero residue.

## Statement

For an odd prime modulus M, the PPT tree projection explores the quadratic state space over the finite field of M. The theorem provides the exact count of states where the accumulated odd leg (v[2]) matches a specific residue, describing the probability distribution of the target residue within the orbit.
