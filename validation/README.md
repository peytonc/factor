# Theorem Validation Suite

Automated numerical validation for every theorem in the catalog (T01–T17).
Standard library only — no third-party dependencies.

```bash
# from the repository root
python validation/run_validation.py                 # defaults: depth 6, 400 trials
python validation/run_validation.py --depth 7 --trials 2000 --csv results.csv
```

The runner prints a per-theorem table (checks, failures, notes) and exits
non-zero if anything fails, so it doubles as a CI gate
(see `.github/workflows/validate.yml`).

## Architecture: shared kernel vs. independent logic

The suite is deliberately split into two layers so that each theorem's
validator encodes **only the statement-specific predicate**, while everything
mechanical is written once and reused by all validation methods.

**Shared kernel — `core.py`.** Generator matrices (factor-state `A/B/C` and
geometric `Berggren_A/B/C`), root vectors, the `delta`/`e` divergence
constants, exact 3×3 integer linear algebra (`mat_vec`, `mat_mul`, `det3`,
adjugate inverses mod M), path application and right-to-left path products,
breadth-first tree enumeration with parent/generator tracking, factor recovery
from `v = [p², q², a]`, PPT geometry helpers, modular-orbit machinery (cached
orbit closure, backward reachability via inverse generators, prime-power
factorization), swap helpers (adjacent partners, `sigma`, `alpha`, shadow-path
construction), a seeded RNG factory, and the uniform `Result`/`Config` types.

**Independent logic — `validators/`.** Three cluster modules mirroring
`docs/dependency-graph.md`, each contributing only thin predicates:

| Cluster | Theorems | Statement-specific code | Kernel reused |
| :-- | :-- | :-- | :-- |
| `foundations.py` | T01–T04 | factor-recursion table, `a = 3 + 2d` closed form, `(p,q)` injectivity bookkeeping, strict-growth predicate | tree enumeration, matrix algebra, factor recovery, geometry |
| `modular.py` | T05–T10 | homomorphism equivalence, strong-connectivity criterion, axis biconditional, the three cardinality formulas, CRT product-set comparison, Hensel fiber counting | orbit closure, modular inverses, backward reachability, factorization |
| `differential.py` | T11–T17 | sibling-difference identities, per-depth congruences, GCD leaf congruence, exact single- and multi-swap formulas, the λ interval classifier | swap helpers, suffix products, path application, tree enumeration, RNG |

Of roughly 700 lines of validator code, about 330 (the kernel) are shared by
all seventeen methods; the per-theorem logic averages ~25 lines. T05, T12–T15,
and T17 are almost pure kernel composition; T08–T10 carry the most independent
code (counting formulas); T16's λ classifier is fully independent but rides on
the shared enumerator.

## What each validator checks

- **T01** — full-tree commutation between the algebraic action (A/B/C on `v`),
  the geometric action (Berggren matrices on `(a,b,c)`), and the factor
  recursion on `(p,q)`; PPT identities `p² = c−b`, `q² = c+b`; determinants;
  the p-preservation/promotion claims.
- **T02** — `a = 3 + 2d` on the all-A branch to depth 2,000, plus the
  `d_target = (a_target − 3)/2` formula on sample targets.
- **T03** — injectivity of node → `(p,q)` over the full enumeration, coprime
  and odd-parity constraints, Euclid-parameter constraints.
- **T04** — strict growth of `a` over every enumerated edge and on deep
  (length-200) random paths.
- **T05** — stepwise reduction mod M equals reduce-at-the-end, across odd
  prime, prime-power, square-free, and mixed moduli.
- **T06** — generators are units of `GL(3, Z/MZ)` with explicit inverses,
  permute the orbit, and the orbit is strongly connected (forward orbit ⊆
  backward-reachable set of the root).
- **T07** — `v[2] ≡ 0 ⇔ exactly one of v[0], v[1] ≡ 0` on the full prime
  orbit; origin unreachable.
- **T08** — `|Orbit(M)| = (M²−1)/2`, axis count `M−1`, each non-zero residue
  class `(M−1)/2`.
- **T09** — `|O_M| = Π|O_{p_i}|` and the Φ image equals the **full** Cartesian
  product set, for square-free M.
- **T10** — `|O_{p^k}| = p^{2(k−1)}·|O_p|` with surjective projection and
  uniform Hensel fibers; the product law over maximal prime-power components
  for general odd M.
- **T11** — exact `v_B − v_C = a·delta_a` and `v_B − v_A = b·delta_b` over the
  full enumerated tree.
- **T12/T13** — fork congruence mod `2·a_parent` / `2·b_parent` checked at
  **every** descendant depth on random fork/suffix trials.
- **T14** — leaf congruence mod `GCD(M_1,…,M_k)` for 2–4 random swaps.
- **T15** — the exact identity `v_shadow − v_key = σ·α·(R·δ)`: exhaustive over
  all short prefix/suffix/swap combinations plus deep random trials.
- **T16** — the λ = q/p interval classifier (exact integer comparisons, no
  floats) recovers the true generator at every enumerated node; no boundary
  values occur off the root.
- **T17** — the exact multi-swap superposition and lattice membership of every
  term, exhaustive over all length-5 keys × 2-swap combinations plus deep
  random trials. The validator also evaluates the **literal** text reading of
  `R_m` (starting at `G_(d_m+1)`, i.e. including the swapped generator) head to
  head with the corrected reading (`G_(d_m+2)`, consistent with T15's `R`):
  the corrected formula is exact in every case; the literal reading matches in
  none, confirming the off-by-one in the original definition line.

## Scope and honesty notes

Numerical validation is evidence, not proof. Three claims are inherently
beyond finite testing and are checked only in their finite consequences:
T03's *surjectivity* onto all coprime odd pairs (Berggren's classical
bijection — injectivity and constraints are checked exhaustively to the
configured depth), T06's strong connectivity for *all* odd M (verified for the
19 configured moduli up to 121), and T09's group-theoretic argument
(Goursat/PSL surjectivity — its consequence, orbit = full product, is checked
exactly). Everything else in the catalog is an exact finite identity at each
tested instance and is checked as such.

All randomness is seeded (`--seed`, default 20260610), so runs are
reproducible; raising `--trials` and `--depth` strengthens the evidence at the
cost of runtime.
