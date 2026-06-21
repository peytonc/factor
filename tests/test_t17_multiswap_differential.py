"""T17 — Multi-Swap Differential.

Exact multi-swap superposition and lattice membership of every term, exhaustive
over all length-5 keys x 2-swap combinations plus deep random trials. Also runs
the literal-text reading of R_m (starting at the swapped generator) head to head
with the corrected reading (consistent with T15's R): the corrected formula is
exact in every case; the literal reading matches in none, confirming the
off-by-one in the original T17 definition line.
"""
from __future__ import annotations

from itertools import combinations, product as iproduct

from core import (
    DELTA, GEN_NAMES, alpha_for, apply_path, make_shadow, mat_vec, path_matrix,
    random_path, sigma, swap_kind, vec_add, vec_scale, vec_sub,
)
from checker import Checker


def _swap_data(key, shadow, idxs):
    """Per-swap (idx, kind, sign, alpha, M) read off the KEY path. Shared with
    T14; kept local so the only cross-theorem references are the kernel and the
    Checker."""
    out = []
    for i in idxs:
        kind = swap_kind(key[i], shadow[i])
        sgn = sigma(key[i], shadow[i])
        v_parent = apply_path(key[:i])
        alpha = alpha_for(kind, v_parent)
        out.append((i, kind, sgn, alpha, 2 * alpha))
    return out


def _t17_predictions(key, shadow, idxs):
    """Return (exact diff, corrected prediction, literal-text prediction, lattice_ok).

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


def test_t17(cfg):
    chk = Checker("T17", "Multi-Swap Differential")
    rng = cfg.rng("t17")
    literal_hits = 0
    total_cases = 0

    # Exhaustive small sweep: every length-5 key path, every 2-swap index pair,
    # every adjacent shadow combination.
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
                chk.check(diff == corrected,
                          f"superposition broken: key={''.join(key)} swaps={idxs}")
                chk.check(lattice_ok, f"lattice term not divisible by M_m: key={''.join(key)}")
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
        chk.check(diff == corrected, f"superposition broken on random trial (n={n}, swaps={idxs})")
        chk.check(lattice_ok, "lattice term not divisible by M_m on random trial")
        if diff == literal:
            literal_hits += 1

    chk.note(f"corrected R_m (= G_n..G_(d_m+2), matching T15) exact in {total_cases}/{total_cases} cases "
             f"({exhaustive_cases} exhaustive + {cfg.trials} random)")
    chk.note(f"literal-text R_m (= G_n..G_(d_m+1), includes swapped step) matched only "
             f"{literal_hits}/{total_cases} cases -> confirms the off-by-one in the T17 definition line")
    # The corrected formula must be exact; the literal reading must match in no case.
    chk.check(literal_hits == 0,
              f"literal-text R_m unexpectedly matched in {literal_hits} cases")
    chk.finalize()
