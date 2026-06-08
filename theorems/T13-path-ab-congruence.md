---
id: T13
type: theorem
title: Path A/B Modular Congruence
slug: path-ab-congruence
depends_on: [T11]
variables: [P, Q_fork, Q_swap, R, v_parent, b_parent, M]
status: proven
proof_file: ../proofs/T13-path-ab-congruence-proof.md
---

# T13 — Path A/B Modular Congruence

> An A<->B swap keeps every descendant congruent to the key path modulo 2*b_parent.

## Definitions

- Let `P` be a sequence of generators applied to v_root to reach a parent node v_parent at depth d.
- Let `Q_fork in {A, B}`.
- Let `Q_swap in {A, B}` and `Q_swap != Q_fork`.
- Let `R = G_(d+2) * G_(d+3) * ...` be an arbitrary sequence of subsequent generators applied after the fork.
- Let `P_1 = R * Q_fork * P` be the original matrix sequence (multiplication order is reverse of path order).
- Let `P_2 = R * Q_swap * P` be the shadow matrix sequence.
- Let `v_i = P_1 * v_root` and `w_i = P_2 * v_root`.
- `v_i ≡ w_i (mod 2*b_parent)` for any depth i > d.

## Statement

If a single substitution is made between generator A and generator B at node v_parent, and all subsequent operations remain identical for both branches, then every resulting descendant node on the shadow path P_2 is congruent to the corresponding node on the original path P_1 modulo 2*b_parent. While the descendant values diverge rapidly in magnitude, their residues relative to twice the divergence point's even leg remain locked together for the remainder of the path.

## Proof

See [T13-path-ab-congruence-proof.md](../proofs/T13-path-ab-congruence-proof.md).

## Dependencies

- [T11 — Sibling Divergence](T11-sibling-divergence.md)

## Notation

All symbols are defined in [docs/glossary.md](../docs/glossary.md).
