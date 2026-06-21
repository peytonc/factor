"""T07 — Prime Modular Axis Alignment.

v[2] == 0  <=>  exactly one of v[0], v[1] == 0, on the full prime orbit; the
origin is unreachable.
"""
from __future__ import annotations

from core import orbit
from checker import Checker


def test_t07(cfg):
    chk = Checker("T07", "Prime Modular Axis Alignment")
    for m in cfg.primes:
        for v in orbit(m):
            zero_leg = v[2] % m == 0
            on_one_axis = (v[0] % m == 0) ^ (v[1] % m == 0)
            chk.check(zero_leg == on_one_axis, f"axis biconditional broken mod {m} at {v}")
            chk.check(not (v[0] % m == 0 and v[1] % m == 0),
                      f"origin reached mod {m} at {v}")
    chk.finalize()
