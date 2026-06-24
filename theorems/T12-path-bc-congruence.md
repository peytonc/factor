---
id: T12
type: theorem
title: Path B/C Modular Congruence
slug: path-bc-congruence
depends_on: [T11]
notation: ../glossary.md
variables: [P, Q_fork, Q_swap, R, v_parent, a_parent, M]
status: proven
proof_file: ../proofs/T12-path-bc-congruence-proof.md
---

# T12 — Path B/C Modular Congruence

> A B<->C swap keeps every descendant congruent to the key path modulo 2*a_parent.

## Definitions

- Let `P` be a sequence of generators applied to v_root to reach a parent node v_parent at depth d (maintaining right-to-left multiplication order).
- Let `Q_fork in {B, C}`.
- Let `Q_swap in {B, C}` and `Q_swap != Q_fork`.
- Let `R = G_leaf * ... * G_(d+3) * G_(d+2)` be an arbitrary sequence of subsequent generators applied after the fork (maintaining right-to-left multiplication order).
- Let `P_1 = R * Q_fork * P` be the original matrix sequence (multiplication order is reverse of path order).
- Let `P_2 = R * Q_swap * P` be the shadow matrix sequence (multiplication order is reverse of path order).
- Let `v_i = P_1 * v_root` and `w_i = P_2 * v_root`.
- `v_i ≡ w_i (mod 2*a_parent)` for any depth i > d.

## Statement

If a single substitution is made between generator B and generator C at node v_parent, and all subsequent operations remain identical for both branches, then every resulting descendant node on the shadow path P_2 is congruent to the corresponding node on the original path P_1 modulo 2*a_parent. While the descendant values diverge rapidly in magnitude, their residues relative to twice the divergence point's odd leg remain locked together for the remainder of the path.
