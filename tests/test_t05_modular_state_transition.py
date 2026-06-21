"""T05 — Modular Algebraic State Transition.

Stepwise reduction mod M equals reduce-at-the-end, across odd prime,
prime-power, square-free, and mixed moduli.
"""
from __future__ import annotations

from core import GENS, V_ROOT, apply_path, mat_mod, mat_vec, random_path, vec_mod
from checker import Checker


def test_t05(cfg):
    chk = Checker("T05", "Modular Algebraic State Transition")
    rng = cfg.rng("t05")
    moduli = cfg.primes + cfg.prime_powers + cfg.squarefree + cfg.mixed_odd
    for _ in range(cfg.trials // 4):
        path = random_path(rng, rng.randint(1, 30))
        v_int = apply_path(path)                      # exact over Z, then reduce
        for m in (rng.choice(moduli), rng.choice(moduli)):
            v_mod = vec_mod(V_ROOT, m)                # reduce at every step
            for g in path:
                v_mod = vec_mod(mat_vec(mat_mod(GENS[g], m), v_mod), m)
            chk.check(v_mod == vec_mod(v_int, m),
                      f"homomorphism broken: M={m}, path={''.join(path)}")
    chk.note(f"stepwise reduction == reduce-at-end for random paths over {len(moduli)} odd moduli")
    chk.finalize()
