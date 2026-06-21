"""T15 — Differential Suffix Propagation.

The exact identity v_shadow - v_key = sigma*alpha*(R*delta): exhaustive over all
short prefix/suffix/swap combinations plus deep random trials.
"""
from __future__ import annotations

from itertools import product as iproduct

from core import (
    DELTA, GEN_NAMES, GENS, alpha_for, apply_path, mat_vec, path_matrix,
    random_path, sigma, swap_kind, vec_scale, vec_sub,
)
from checker import Checker

SWAP_PAIRS = (("A", "B"), ("B", "A"), ("B", "C"), ("C", "B"))


def _t15_case(chk, prefix, key_gen, shadow_gen, suffix):
    v_parent = apply_path(prefix)
    kind = swap_kind(key_gen, shadow_gen)
    sgn = sigma(key_gen, shadow_gen)
    alpha = alpha_for(kind, v_parent)
    suffix_mat = path_matrix(suffix)  # R = G_leaf ... G_(d+2)
    v_key = apply_path(suffix, mat_vec(GENS[key_gen], v_parent))
    v_shadow = apply_path(suffix, mat_vec(GENS[shadow_gen], v_parent))
    predicted = vec_scale(sgn * alpha, mat_vec(suffix_mat, DELTA[kind]))
    chk.check(vec_sub(v_shadow, v_key) == predicted,
              f"T15 identity broken: prefix={''.join(prefix)} "
              f"swap=({key_gen},{shadow_gen}) suffix={''.join(suffix)}")


def test_t15(cfg):
    chk = Checker("T15", "Differential Suffix Propagation")
    # Exhaustive sweep over short prefixes/suffixes and all four ordered swaps.
    short = [()] + [p for n in range(1, 4) for p in iproduct(GEN_NAMES, repeat=n)]
    for prefix in short:
        for key_gen, shadow_gen in SWAP_PAIRS:
            for suffix in short:
                _t15_case(chk, prefix, key_gen, shadow_gen, suffix)
    exhaustive = chk.checks
    # Random deep trials.
    rng = cfg.rng("t15")
    for _ in range(cfg.trials):
        prefix = random_path(rng, rng.randint(0, 10))
        key_gen, shadow_gen = rng.choice(SWAP_PAIRS)
        suffix = random_path(rng, rng.randint(0, 10))
        _t15_case(chk, prefix, key_gen, shadow_gen, suffix)
    chk.note(f"{exhaustive} exhaustive short cases + {cfg.trials} random deep trials, all exact")
    chk.finalize()
