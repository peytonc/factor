---
id: T03
type: theorem
title: Non-Trivial Unique Path (Unique Existence)
slug: nontrivial-path-existence
depends_on: [T01]
notation: ../glossary.md
variables: [a_target, p_target, q_target]
status: proven
proof_file: ../proofs/T03-nontrivial-path-existence-proof.md
---

# T03 — Non-Trivial Unique Path (Unique Existence)

> Exactly one non-trivial path reaches the (p_target, q_target) node; it must use at least one B or C transition.

## Definitions

- Let `a_target = p_target * q_target` denote the unique non-trivial factorization of the semiprime, satisfying `1 < p_target < q_target`. This corresponds to exactly one node in the PPT tree distinct from the trivial A-branch solution.

## Statement

The non-trivial path is the unique finite sequence of state transition matrices starting at v_root and terminating at the node defined by the factors (p_target, q_target), which must contain at least one transition using generator B or C to satisfy the condition p_target > 1.
