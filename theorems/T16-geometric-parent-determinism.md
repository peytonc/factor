---
id: T16
type: theorem
title: Geometric Parent Determinism
slug: geometric-parent-determinism
depends_on: [T01]
variables: [p, q, lambda]
status: proven
proof_file: ../proofs/T16-geometric-parent-determinism-proof.md
---

# T16 — Geometric Parent Determinism

> For a node with known (p,q), the generating parent's matrix is read off from the ratio lambda = q/p.

## Definitions

- Let `p` and `q` be the known integer factors of a PPT node (such as a surrogate node v_S), satisfying `1 <= p < q`.
- Let `lambda = q / p` be the factor ratio of the child node.

## Statement

Unlike the target semiprime a_target, where the path is obscured by unknown factors, any node with known p and q values allows for immediate backtracking. The specific generator matrix used to create the current node from its parent can be identified deterministically by checking the interval of lambda.

If `lambda > 3`, the current node is an A-child.

If `2 < lambda < 3`, the current node is a B-child.

If `1 < lambda < 2`, the current node is a C-child.

If `lambda = 3`, the node is the root v_root and has no parent.

## Proof

See [T16-geometric-parent-determinism-proof.md](../proofs/T16-geometric-parent-determinism-proof.md).

## Dependencies

- [T01 — Linearized Algebraic State Transition](T01-linearized-state-transition.md)

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
