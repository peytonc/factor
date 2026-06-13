---
id: T02
type: theorem
title: Trivial Path (Unique Existence)
slug: trivial-path-existence
depends_on: [T01]
notation: ../glossary.md
variables: [a_target, d_target, A, p, q]
status: proven
proof_file: ../proofs/T02-trivial-path-existence-proof.md
---

# T02 — Trivial Path (Unique Existence)

> The trivial factorization 1*a_target sits on the all-A branch at depth (a_target - 3)/2.

## Definitions

- Let `d_target = (a_target - 3) / 2` be the tree depth of a_target on the A-branch.
- Let `a_target = (A^d_target * v_root)[2]` be the trivial unique solution.
- Let `p = 1` and `q = a_target` define the trivial factorization on the A-branch.

## Statement

Generator A acts as the trivial operator. It preserves the smaller factor p=1 and increments the odd leg a linearly. This path contains every odd integer a>=3 exactly once. Therefore, a trivial solution for a_target always exists on the A-branch at depth d_target and corresponds to the factorization 1*a_target.
