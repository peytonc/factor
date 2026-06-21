"""T12 — Path B/C Modular Congruence.

After a B<->C fork at a random parent, an identical random suffix on both
branches stays congruent mod 2*a_parent at every descendant depth.
"""
from __future__ import annotations

from core import (
    GENS, alpha_for, apply_path, mat_vec, random_path, swap_kind, vec_sub,
)
from checker import Checker


def _fork_congruence(chk, cfg, fork_pair, salt):
    """Fork at a random parent, follow an identical random suffix on both
    branches, and check congruence at every depth. Shared body for T12/T13
    (kept local to each theorem so the only cross-theorem references are the
    kernel and the Checker)."""
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
        chk.check(all(x % modulus == 0 for x in vec_sub(w, v)),
                  f"children not congruent mod {modulus}")
        for g in random_path(rng, rng.randint(0, 6)):
            v = mat_vec(GENS[g], v)
            w = mat_vec(GENS[g], w)
            chk.check(all(x % modulus == 0 for x in vec_sub(w, v)),
                      f"descendants not congruent mod {modulus}")


def test_t12(cfg):
    chk = Checker("T12", "Path B/C Modular Congruence")
    _fork_congruence(chk, cfg, ("B", "C"), "t12")
    chk.note(f"{cfg.trials} random fork/suffix trials, congruence checked at every depth")
    chk.finalize()
