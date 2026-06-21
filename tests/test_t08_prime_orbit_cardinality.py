"""T08 — Prime Modular Orbit Cardinality.

|Orbit(M)| = (M^2-1)/2, axis count M-1, and each non-zero residue class
(M-1)/2.
"""
from __future__ import annotations

from collections import Counter

from core import orbit
from checker import Checker


def test_t08(cfg):
    chk = Checker("T08", "Prime Modular Orbit Cardinality")
    for m in cfg.primes:
        o = orbit(m)
        chk.check(len(o) == (m * m - 1) // 2, f"|Orbit({m})| != (M^2-1)/2")
        counts = Counter(v[2] % m for v in o)
        chk.check(counts.get(0, 0) == m - 1, f"axis count != M-1 mod {m}")
        for k in range(1, m):
            chk.check(counts.get(k, 0) == (m - 1) // 2,
                      f"residue {k} count != (M-1)/2 mod {m}")
    chk.finalize()
