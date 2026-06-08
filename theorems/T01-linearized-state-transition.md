---
id: T01
type: theorem
title: Linearized Algebraic State Transition
slug: linearized-state-transition
depends_on: []
variables: [v, G, A, B, C, p, q, a]
status: proven
proof_file: ../proofs/T01-linearized-state-transition-proof.md
---

# T01 — Linearized Algebraic State Transition

> Maps PPT geometry (c,b) to algebraic factors via linear matrices A/B/C acting on v=[p^2,q^2,a]^T.

## Definitions

- Let `v_(d+1) = G_d * v_d` be the state transition to a child node at depth d+1.

## Statement

Establishes a linear system by mapping the geometric properties of the PPT (c,b) to the algebraic factors (p^2, q^2).

Matrix **A** preserves the factor p, increases a, and preserves orientation with det(A)=1.

Matrix **B** promotes the old q to the new p, increases a, and reverses orientation with det=-1.

Matrix **C** promotes the old q to the new p, increases a, and preserves orientation with det(C)=1.

## Proof

See [T01-linearized-state-transition-proof.md](../proofs/T01-linearized-state-transition-proof.md).

## Dependencies

- None (foundational).

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
