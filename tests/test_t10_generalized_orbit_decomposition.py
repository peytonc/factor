"""T10 — Generalized Modular Orbit Decomposition.

|O_{p^k}| = p^{2(k-1)}*|O_p| with surjective projection and uniform Hensel
fibers; the product law over maximal prime-power components for general odd M.
"""
from __future__ import annotations

from collections import Counter
from itertools import product as iproduct

from core import orbit, prime_power_factorization, vec_mod
from checker import Checker


def test_t10(cfg):
    chk = Checker("T10", "Generalized Modular Orbit Decomposition")
    for pk in cfg.prime_powers:
        ((p, k),) = prime_power_factorization(pk)
        o_pk = orbit(pk)
        o_p = orbit(p)
        fiber = p ** (2 * (k - 1))
        chk.check(len(o_pk) == fiber * len(o_p), f"|Orbit({pk})| != p^(2(k-1)) |Orbit({p})|")
        fibers = Counter(vec_mod(v, p) for v in o_pk)
        chk.check(set(fibers) == set(o_p), f"projection Orbit({pk}) -> Orbit({p}) not onto")
        chk.check(all(c == fiber for c in fibers.values()),
                  f"non-uniform Hensel fibers for {pk}")

    for m in cfg.mixed_odd:
        comps = [p ** k for p, k in prime_power_factorization(m)]
        o_m = orbit(m)
        comp_orbits = [orbit(q) for q in comps]
        expected = 1
        for o_q in comp_orbits:
            expected *= len(o_q)
        chk.check(len(o_m) == expected, f"|Orbit({m})| != prod |Orbit(Q_i)|")
        image = {tuple(vec_mod(v, q) for q in comps) for v in o_m}
        chk.check(image == set(iproduct(*comp_orbits)),
                  f"Phi image != product of prime-power orbits for M={m}")
    chk.finalize()
