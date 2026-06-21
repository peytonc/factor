"""T14 — Multiple Swaps Modular Congruence.

Leaf congruence mod GCD(M_1,...,M_k) for 2-4 random swaps.
"""
from __future__ import annotations

import math

from core import (
    alpha_for, apply_path, make_shadow, random_path, sigma, swap_kind, vec_sub,
)
from checker import Checker


def _swap_data(key, shadow, idxs):
    """Per-swap (idx, kind, sign, alpha, M) read off the KEY path. Shared with
    T17; kept local so the only cross-theorem references are the kernel and the
    Checker."""
    out = []
    for i in idxs:
        kind = swap_kind(key[i], shadow[i])
        sgn = sigma(key[i], shadow[i])
        v_parent = apply_path(key[:i])
        alpha = alpha_for(kind, v_parent)
        out.append((i, kind, sgn, alpha, 2 * alpha))
    return out


def test_t14(cfg):
    chk = Checker("T14", "Multiple Swaps Modular Congruence")
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
        chk.check(all(x % g == 0 for x in diff),
                  f"leaf not congruent mod gcd={g} (key={''.join(key)}, swaps={idxs})")
    chk.note(f"{cfg.trials} random trials, 2-4 swaps each, leaf checked mod GCD(M_1..M_k)")
    chk.finalize()
