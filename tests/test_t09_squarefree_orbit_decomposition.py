"""T09 — Square-Free Modular Orbit Decomposition.

|O_M| = prod |O_{p_i}| and the Phi image equals the full Cartesian product set,
for square-free M.
"""
from __future__ import annotations

from itertools import product as iproduct

from core import orbit, prime_power_factorization, vec_mod
from checker import Checker


def test_t09(cfg):
    chk = Checker("T09", "Square-Free Modular Orbit Decomposition")
    for m in cfg.squarefree:
        primes = [p for p, k in prime_power_factorization(m)]
        o_m = orbit(m)
        prime_orbits = [orbit(p) for p in primes]
        expected = 1
        for o_p in prime_orbits:
            expected *= len(o_p)
        chk.check(len(o_m) == expected, f"|Orbit({m})| != prod |Orbit(p_i)|")
        image = {tuple(vec_mod(v, p) for p in primes) for v in o_m}
        full_product = set(iproduct(*prime_orbits))
        chk.check(image == full_product, f"Phi image != Cartesian product for M={m}")
    chk.finalize()
