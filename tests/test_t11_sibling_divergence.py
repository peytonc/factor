"""T11 — Sibling Divergence.

Exact v_B - v_C = a*delta_a and v_B - v_A = b*delta_b over the full enumerated
tree.
"""
from __future__ import annotations

from core import (
    DELTA, GENS, enumerate_tree, mat_vec, parent_legs, vec_scale, vec_sub,
)
from checker import Checker


def test_t11(cfg):
    chk = Checker("T11", "Sibling Divergence")
    for node in enumerate_tree(cfg.depth - 1):
        a_par, b_par = parent_legs(node.v)
        v_a = mat_vec(GENS["A"], node.v)
        v_b = mat_vec(GENS["B"], node.v)
        v_c = mat_vec(GENS["C"], node.v)
        chk.check(vec_sub(v_b, v_c) == vec_scale(a_par, DELTA["a"]),
                  f"v_B - v_C != a*delta_a at {''.join(node.path)}")
        chk.check(vec_sub(v_b, v_a) == vec_scale(b_par, DELTA["b"]),
                  f"v_B - v_A != b*delta_b at {''.join(node.path)}")
    chk.finalize()
