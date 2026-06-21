"""T06 — Modular Orbit Graph (Finite State Machine).

Generators are units of GL(3, Z/MZ) with explicit inverses, permute the orbit,
and the orbit is strongly connected (forward orbit subset of backward-reachable
set of the root).
"""
from __future__ import annotations

from core import (
    GEN_NAMES, GENS, IDENTITY, backward_reachable, det3, mat_inv_mod, mat_mod,
    mat_mul, mat_vec, orbit, vec_mod,
)
from checker import Checker


def test_t06(cfg):
    chk = Checker("T06", "Modular Orbit Graph (Finite State Machine)")
    moduli = cfg.primes + cfg.prime_powers + cfg.squarefree + cfg.mixed_odd
    for m in moduli:
        for name in GEN_NAMES:
            g = GENS[name]
            chk.check(abs(det3(g)) == 1, f"det({name}) not a unit")
            ginv = mat_inv_mod(g, m)
            chk.check(mat_mod(mat_mul(g, ginv), m) == mat_mod(IDENTITY, m),
                      f"{name}^-1 wrong mod {m}")
        o = orbit(m)
        for name in GEN_NAMES:
            gm = mat_mod(GENS[name], m)
            image = {vec_mod(mat_vec(gm, v), m) for v in o}
            chk.check(image == o, f"{name} does not permute Orbit({m})")
        bk = backward_reachable(m)
        chk.check(o <= bk, f"Orbit({m}) not strongly connected")
    chk.note(f"checked invertibility, permutation action, strong connectivity for M in {list(moduli)}")
    chk.finalize()
