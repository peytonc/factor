"""T02 — Trivial Path (Unique Existence).

a = 3 + 2d on the all-A branch, and the depth formula d_target = (a_target-3)/2.
"""
from __future__ import annotations

from core import GENS, V_ROOT, mat_vec
from checker import Checker


def test_t02(cfg):
    chk = Checker("T02", "Trivial Path (Unique Existence)")
    v = V_ROOT
    n_steps = 2000
    for d in range(n_steps + 1):
        chk.check(v[0] == 1, f"p^2 != 1 at A-depth {d}")
        chk.check(v[2] == 3 + 2 * d, f"a != 3 + 2d at A-depth {d}")
        v = mat_vec(GENS["A"], v)

    for a_target in (15, 35, 143, 3 + 2 * 1234):
        d_target = (a_target - 3) // 2
        v = V_ROOT
        for _ in range(d_target):
            v = mat_vec(GENS["A"], v)
        chk.check(v == (1, a_target * a_target, a_target),
                  f"trivial node wrong for a_target={a_target}")

    chk.note(f"all-A branch walked to depth {n_steps}; a hits every odd >= 3 exactly once")
    chk.finalize()
