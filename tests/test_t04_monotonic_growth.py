"""T04 — Monotonic Growth.

Strict growth of the odd leg a across every enumerated edge and on deep
(length-200) random paths.
"""
from __future__ import annotations

from core import GENS, V_ROOT, enumerate_tree, mat_vec, random_path
from checker import Checker


def test_t04(cfg):
    chk = Checker("T04", "Monotonic Growth")
    for node in enumerate_tree(cfg.depth):
        if node.parent is not None:
            chk.check(node.v[2] > node.parent.v[2],
                      f"a did not grow at {''.join(node.path)}")

    rng = cfg.rng("t04")
    for _ in range(50):
        v = V_ROOT
        for g in random_path(rng, 200):
            w = mat_vec(GENS[g], v)
            chk.check(w[2] > v[2], "a did not grow on deep random path")
            v = w

    chk.finalize()
