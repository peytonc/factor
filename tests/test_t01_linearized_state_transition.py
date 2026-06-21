"""T01 — Linearized Algebraic State Transition.

Full-tree cross-check that the algebraic action (A/B/C on v) commutes with the
geometric Berggren action on (a,b,c) and with the (p,q) factor recursion, plus
the PPT identities, determinants, and the p-preserve/promote claims.
"""
from __future__ import annotations

import math

from core import (
    A, B, C, BERGGREN, GENS, GEO_ROOT, enumerate_tree, det3, geo_from_pq,
    mat_vec,
)
from checker import Checker

# Factor recursion implied by T01 (also used by the T16 proof).
FACTOR_RECURSION = {
    "A": lambda p, q: (p, 2 * p + q),
    "B": lambda p, q: (q, 2 * q + p),
    "C": lambda p, q: (q, 2 * q - p),
}


def test_t01(cfg):
    chk = Checker("T01", "Linearized Algebraic State Transition")

    # Determinant / orientation claims.
    chk.check(det3(A) == 1, "det(A) != 1")
    chk.check(det3(B) == -1, "det(B) != -1")
    chk.check(det3(C) == 1, "det(C) != 1")

    geo = {(): GEO_ROOT}
    pq = {(): (1, 3)}
    for node in enumerate_tree(cfg.depth):
        if node.parent is None:
            continue
        g = node.gen
        parent_path = node.parent.path
        geo_child = mat_vec(BERGGREN[g], geo[parent_path])
        geo[node.path] = geo_child
        p_par, q_par = pq[parent_path]
        p, q = FACTOR_RECURSION[g](p_par, q_par)
        pq[node.path] = (p, q)

        chk.check(node.v == (p * p, q * q, p * q),
                  f"v mismatch at {''.join(node.path)}")
        chk.check(geo_child == geo_from_pq(p, q),
                  f"geometry mismatch at {''.join(node.path)}")
        a, b, c = geo_child
        chk.check(p * p == c - b and q * q == c + b,
                  f"p^2=c-b / q^2=c+b broken at {''.join(node.path)}")
        chk.check(math.gcd(p, q) == 1 and p % 2 == 1 and q % 2 == 1 and p < q,
                  f"factor constraints broken at {''.join(node.path)}")
        if g == "A":
            chk.check(p == p_par, "A failed to preserve p")
        else:
            chk.check(p == q_par, f"{g} failed to promote q to p")

    chk.finalize()
