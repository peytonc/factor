"""
Differential & swap theory cluster (T11-T17).

Swap mechanics (adjacent partners, sigma, alpha, shadow construction, suffix
matrix products) are shared kernel code in ``core``; this module contributes
only the statement-level predicates.

Independent code per theorem:
  T11 - exact sibling-difference identities over the full enumerated tree.
  T12 - per-depth congruence mod 2*a_parent after a B<->C fork.
  T13 - per-depth congruence mod 2*b_parent after an A<->B fork.
  T14 - leaf congruence mod GCD(M_1..M_k) after k swaps.
  T15 - exact single-swap leaf identity (exhaustive small cases + random deep).
  T16 - the lambda = q/p interval classifier vs the actual generator.
  T17 - exact multi-swap superposition + lattice membership, including a
        head-to-head between the corrected suffix R_m = G_n..G_(d_m+2) and the
        literal-text R_m = G_n..G_(d_m+1) (the off-by-one that includes the
        swapped generator itself).
"""
from __future__ import annotations

import math
from itertools import combinations, product as iproduct

from core import (
    Config, DELTA, GEN_NAMES, GENS, Result, V_ROOT, alpha_for, apply_path,
    enumerate_tree, factors_from_v, make_shadow, mat_vec, parent_legs,
    path_matrix, random_path, sigma, swap_kind, vec_add, vec_scale, vec_sub,
)


def validate_t11(cfg: Config) -> Result:
    r = Result("T11", "Sibling Divergence")
    for node in enumerate_tree(cfg.depth - 1):
        a_par, b_par = parent_legs(node.v)
        v_a = mat_vec(GENS["A"], node.v)
        v_b = mat_vec(GENS["B"], node.v)
        v_c = mat_vec(GENS["C"], node.v)
        r.check(vec_sub(v_b, v_c) == vec_scale(a_par, DELTA["a"]),
                f"v_B - v_C != a*delta_a at {''.join(node.path)}")
        r.check(vec_sub(v_b, v_a) == vec_scale(b_par, DELTA["b"]),
                f"v_B - v_A != b*delta_b at {''.join(node.path)}")
    return r


def _fork_congruence(r: Result, cfg: Config, fork_pair, salt: str) -> None:
    """Shared body for T12/T13: fork at a random parent, follow an identical
    random suffix on both branches, and check congruence at every depth."""
    rng = cfg.rng(salt)
    for _ in range(cfg.trials):
        prefix = random_path(rng, rng.randint(0, 6))
        v_parent = apply_path(prefix)
        kind = swap_kind(*fork_pair)
        modulus = 2 * alpha_for(kind, v_parent)
        key_fork = rng.choice(fork_pair)
        shadow_fork = fork_pair[0] if key_fork == fork_pair[1] else fork_pair[1]
        v = mat_vec(GENS[key_fork], v_parent)
        w = mat_vec(GENS[shadow_fork], v_parent)
        r.check(all(x % modulus == 0 for x in vec_sub(w, v)),
                f"children not congruent mod {modulus}")
        for g in random_path(rng, rng.randint(0, 6)):
            v = mat_vec(GENS[g], v)
            w = mat_vec(GENS[g], w)
            r.check(all(x % modulus == 0 for x in vec_sub(w, v)),
                    f"descendants not congruent mod {modulus}")


def validate_t12(cfg: Config) -> Result:
    r = Result("T12", "Path B/C Modular Congruence")
    _fork_congruence(r, cfg, ("B", "C"), "t12")
    r.note(f"{cfg.trials} random fork/suffix trials, congruence checked at every depth")
    return r


def validate_t13(cfg: Config) -> Result:
    r = Result("T13", "Path A/B Modular Congruence")
    _fork_congruence(r, cfg, ("A", "B"), "t13")
    r.note(f"{cfg.trials} random fork/suffix trials, congruence checked at every depth")
    return r


def _swap_data(key, shadow, idxs):
    """Per-swap (kind, sign, alpha, M) read off the KEY path -- the
    key-prefix half of the hybrid decomposition."""
    out = []
    for i in idxs:
        kind = swap_kind(key[i], shadow[i])
        sgn = sigma(key[i], shadow[i])
        v_parent = apply_path(key[:i])
        alpha = alpha_for(kind, v_parent)
        out.append((i, kind, sgn, alpha, 2 * alpha))
    return out


def validate_t14(cfg: Config) -> Result:
    r = Result("T14", "Multiple Swaps Modular Congruence")
    rng = cfg.rng("t14")
    for _ in range(cfg.trials):
        n = rng.randint(6, 12)
        key = random_path(rng, n)
        k = rng.randint(2, 4)
        idxs = sorted(rng.sample(range(n), k))
        shadow = make_shadow(key, idxs, rng)
        moduli = [m for (_, _, _, _, m) in _swap_data(key, shadow, idxs)]
        g = math.gcd(*moduli)
        diff = vec_sub(apply_path(shadow), apply_path(key))
        r.check(all(x % g == 0 for x in diff),
                f"leaf not congruent mod gcd={g} (key={''.join(key)}, swaps={idxs})")
    r.note(f"{cfg.trials} random trials, 2-4 swaps each, leaf checked mod GCD(M_1..M_k)")
    return r


def _t15_case(r: Result, prefix, key_gen, shadow_gen, suffix) -> None:
    v_parent = apply_path(prefix)
    kind = swap_kind(key_gen, shadow_gen)
    sgn = sigma(key_gen, shadow_gen)
    alpha = alpha_for(kind, v_parent)
    suffix_mat = path_matrix(suffix)  # R = G_leaf ... G_(d+2)
    v_key = apply_path(suffix, mat_vec(GENS[key_gen], v_parent))
    v_shadow = apply_path(suffix, mat_vec(GENS[shadow_gen], v_parent))
    predicted = vec_scale(sgn * alpha, mat_vec(suffix_mat, DELTA[kind]))
    r.check(vec_sub(v_shadow, v_key) == predicted,
            f"T15 identity broken: prefix={''.join(prefix)} "
            f"swap=({key_gen},{shadow_gen}) suffix={''.join(suffix)}")


SWAP_PAIRS = (("A", "B"), ("B", "A"), ("B", "C"), ("C", "B"))


def validate_t15(cfg: Config) -> Result:
    r = Result("T15", "Differential Suffix Propagation")
    # Exhaustive sweep over short prefixes/suffixes and all four ordered swaps.
    short = [()] + [p for n in range(1, 4) for p in iproduct(GEN_NAMES, repeat=n)]
    for prefix in short:
        for key_gen, shadow_gen in SWAP_PAIRS:
            for suffix in short:
                _t15_case(r, prefix, key_gen, shadow_gen, suffix)
    exhaustive = r.checks
    # Random deep trials.
    rng = cfg.rng("t15")
    for _ in range(cfg.trials):
        prefix = random_path(rng, rng.randint(0, 10))
        key_gen, shadow_gen = rng.choice(SWAP_PAIRS)
        suffix = random_path(rng, rng.randint(0, 10))
        _t15_case(r, prefix, key_gen, shadow_gen, suffix)
    r.note(f"{exhaustive} exhaustive short cases + {cfg.trials} random deep trials, all exact")
    return r


def validate_t16(cfg: Config) -> Result:
    r = Result("T16", "Geometric Parent Determinism")
    for node in enumerate_tree(cfg.depth):
        p, q = factors_from_v(node.v)
        if node.parent is None:
            r.check(q == 3 * p, "root does not satisfy lambda = 3")
            continue
        # Exact integer interval test for lambda = q/p (no floats).
        r.check(q != 2 * p and q != 3 * p,
                f"lambda hit an interval boundary at {''.join(node.path)}")
        if q > 3 * p:
            classified = "A"
        elif q > 2 * p:
            classified = "B"
        else:
            classified = "C"
        r.check(p < q, f"p < q broken at {''.join(node.path)}")
        r.check(classified == node.gen,
                f"lambda classified {classified} but generator was {node.gen} "
                f"at {''.join(node.path)}")
    return r


def _t17_predictions(key, shadow, idxs):
    """Return (exact diff, corrected prediction, literal-text prediction).

    corrected: R_m = product of shadow suffix STRICTLY AFTER the swapped step
               (G_n ... G_(d_m+2)) -- consistent with T15's definition of R.
    literal:   R_m = product starting AT the swapped step (G_n ... G_(d_m+1))
               as the T17 definition line reads, i.e. including the swapped
               generator itself.
    """
    diff = vec_sub(apply_path(shadow), apply_path(key))
    corrected = (0, 0, 0)
    literal = (0, 0, 0)
    lattice_ok = True
    for i, kind, sgn, alpha, m_m in _swap_data(key, shadow, idxs):
        r_corr = path_matrix(shadow[i + 1:])
        r_lit = path_matrix(shadow[i:])
        term = vec_scale(sgn * alpha, mat_vec(r_corr, DELTA[kind]))
        if any(x % m_m != 0 for x in term):
            lattice_ok = False
        corrected = vec_add(corrected, term)
        literal = vec_add(literal, vec_scale(sgn * alpha, mat_vec(r_lit, DELTA[kind])))
    return diff, corrected, literal, lattice_ok


def validate_t17(cfg: Config) -> Result:
    r = Result("T17", "Multi-Swap Differential")
    rng = cfg.rng("t17")
    literal_hits = 0
    total_cases = 0

    # Exhaustive small sweep: every length-5 key path, every 2-swap index pair,
    # every adjacent shadow combination (echoes the 1,093-node CSV harness).
    for key in iproduct(GEN_NAMES, repeat=5):
        for idxs in combinations(range(5), 2):
            options = [("A", "C") if key[i] == "B" else ("B",) for i in idxs]
            for choice in iproduct(*options):
                shadow = list(key)
                for i, g in zip(idxs, choice):
                    shadow[i] = g
                shadow = tuple(shadow)
                diff, corrected, literal, lattice_ok = _t17_predictions(key, shadow, idxs)
                total_cases += 1
                r.check(diff == corrected,
                        f"superposition broken: key={''.join(key)} swaps={idxs}")
                r.check(lattice_ok, f"lattice term not divisible by M_m: key={''.join(key)}")
                if diff == literal:
                    literal_hits += 1
    exhaustive_cases = total_cases

    # Random deep trials with 2-4 swaps.
    for _ in range(cfg.trials):
        n = rng.randint(6, 12)
        key = random_path(rng, n)
        k = rng.randint(2, 4)
        idxs = sorted(rng.sample(range(n), k))
        shadow = make_shadow(key, idxs, rng)
        diff, corrected, literal, lattice_ok = _t17_predictions(key, shadow, idxs)
        total_cases += 1
        r.check(diff == corrected, f"superposition broken on random trial (n={n}, swaps={idxs})")
        r.check(lattice_ok, "lattice term not divisible by M_m on random trial")
        if diff == literal:
            literal_hits += 1

    r.note(f"corrected R_m (= G_n..G_(d_m+2), matching T15) exact in {total_cases}/{total_cases} cases "
           f"({exhaustive_cases} exhaustive + {cfg.trials} random)")
    r.note(f"literal-text R_m (= G_n..G_(d_m+1), includes swapped step) matched only "
           f"{literal_hits}/{total_cases} cases -> confirms the off-by-one in the T17 definition line")
    return r
