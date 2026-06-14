# Factorization via PPT Tree Navigation

Factor odd semiprimes by navigating the **Berggren tree of Primitive Pythagorean
Triples (PPTs)** with linear factor-state vectors. Each tree node is encoded as a
state vector `v = [p^2, q^2, a]^T`, and the three Berggren generators are realized
as integer matrices **A**, **B**, **C** acting on `v`. The research goal is to locate
the node whose odd leg equals a known semiprime `a_target` whose factors are unknown.

> **Symbol reference:** every variable used across the repository is defined once in
> [`glossary.md`](glossary.md). Theorem and proof files reference it instead
> of re-defining symbols.

## Project Goal

- **Input:** an odd semiprime `a_target` (the odd leg `a` of an unknown PPT node).
- **Output:** the non-trivial factor pair `(p_target, q_target)` with `1 < p_target < q_target`.
- **Method:** navigate or constrain the PPT tree efficiently.

## Theorem Catalog

| ID | Title | Core Purpose | Depends On |
| :-- | :-- | :-- | :-- |
| [T01](theorems/T01-linearized-state-transition.md) | Linearized Algebraic State Transition | Maps PPT geometry (c,b) to algebraic factors via linear matrices A/B/C acting on v=[p^2,q^2,a]^T. | — |
| [T02](theorems/T02-trivial-path-existence.md) | Trivial Path (Unique Existence) | The trivial factorization 1*a_target sits on the all-A branch at depth (a_target - 3)/2. | T01 |
| [T03](theorems/T03-nontrivial-path-existence.md) | Non-Trivial Unique Path (Unique Existence) | Exactly one non-trivial path reaches the (p_target, q_target) node; it must use at least one B or C transition. | T01 |
| [T04](theorems/T04-monotonic-growth.md) | Monotonic Growth | The odd leg a strictly increases at every transition, guaranteeing a monotonic descent. | T01 |
| [T05](theorems/T05-modular-state-transition.md) | Modular Algebraic State Transition | Projects the infinite tree into a finite ring (Z/MZ)^3 via a ring homomorphism that commutes with the generators. | T01 |
| [T06](theorems/T06-modular-orbit-graph.md) | Modular Orbit Graph (Finite State Machine) | The modular state graph is strongly connected because the generators are invertible permutations of a finite space. | T05 |
| [T07](theorems/T07-prime-axis-alignment.md) | Prime Modular Axis Alignment | For prime M, a zero odd-leg residue holds iff exactly one factor (p or q) is congruent to zero. | T06 |
| [T08](theorems/T08-prime-orbit-cardinality.md) | Prime Modular Orbit Cardinality | Gives exact state counts per odd-leg residue class in the prime modular orbit. | T06, T07 |
| [T09](theorems/T09-squarefree-orbit-decomposition.md) | Square-Free Modular Orbit Decomposition | For square-free M, the orbit is isomorphic to the Cartesian product of its prime orbits (CRT). | T06, T08 |
| [T10](theorems/T10-generalized-orbit-decomposition.md) | Generalized Modular Orbit Decomposition | Generalizes the decomposition to prime-power (Hensel-lifted) atomic moduli for any odd M. | T09 |
| [T11](theorems/T11-sibling-divergence.md) | Sibling Divergence | The difference between sibling children is strictly linear in the parent's odd leg (B vs C) or even leg (B vs A). | T01 |
| [T12](theorems/T12-path-bc-congruence.md) | Path B/C Modular Congruence | A B<->C swap keeps every descendant congruent to the key path modulo 2*a_parent. | T11 |
| [T13](theorems/T13-path-ab-congruence.md) | Path A/B Modular Congruence | An A<->B swap keeps every descendant congruent to the key path modulo 2*b_parent. | T11 |
| [T14](theorems/T14-multiswap-congruence.md) | Multiple Swaps Modular Congruence | After k swaps, the leaf stays congruent to the key path modulo the GCD of the per-swap moduli. | T12, T13 |
| [T15](theorems/T15-differential-suffix-propagation.md) | Differential Suffix Propagation | Gives the exact single-swap leaf error vector: v_shadow - v_key = sigma * alpha * (R * delta). | T11 |
| [T16](theorems/T16-geometric-parent-determinism.md) | Geometric Parent Determinism | For a node with known (p,q), the generating parent's matrix is read off from the ratio lambda = q/p. | T01 |
| [T17](theorems/T17-multiswap-differential.md) | Multi-Swap Differential | Gives the exact 3D leaf difference for k swaps as a linear combination lying inside the lattice Lambda. | T11, T15 |

Each row links to its statement in [`theorems/`](theorems/); every statement links
to its companion proof in [`proofs/`](proofs/).

## Numerical Validation

Every theorem has an automated numerical validator documented at [`validation/README.md`](validation/README.md).
