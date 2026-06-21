"""T16 — Geometric Parent Determinism.

The lambda = q/p interval classifier (exact integer comparisons, no floats)
recovers the true generator at every enumerated node; no boundary values occur
off the root.
"""
from __future__ import annotations

from core import enumerate_tree, factors_from_v
from checker import Checker


def test_t16(cfg):
    chk = Checker("T16", "Geometric Parent Determinism")
    for node in enumerate_tree(cfg.depth):
        p, q = factors_from_v(node.v)
        if node.parent is None:
            chk.check(q == 3 * p, "root does not satisfy lambda = 3")
            continue
        # Exact integer interval test for lambda = q/p (no floats).
        chk.check(q != 2 * p and q != 3 * p,
                  f"lambda hit an interval boundary at {''.join(node.path)}")
        if q > 3 * p:
            classified = "A"
        elif q > 2 * p:
            classified = "B"
        else:
            classified = "C"
        chk.check(p < q, f"p < q broken at {''.join(node.path)}")
        chk.check(classified == node.gen,
                  f"lambda classified {classified} but generator was {node.gen} "
                  f"at {''.join(node.path)}")
    chk.finalize()
