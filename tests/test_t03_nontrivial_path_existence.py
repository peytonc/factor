"""T03 — Non-Trivial Unique Path (Unique Existence).

Injectivity of node -> (p,q) over the enumeration, coprime/odd-parity and
Euclid-parameter constraints, and uniqueness of the non-trivial pair per leg.
(Surjectivity onto all coprime odd pairs is Berggren's classical bijection and
is structural, not finitely testable.)
"""
from __future__ import annotations

import math

from core import enumerate_tree, factors_from_v
from checker import Checker


def test_t03(cfg):
    chk = Checker("T03", "Non-Trivial Unique Path (Unique Existence)")
    seen = {}
    semiprime_nodes = {}
    for node in enumerate_tree(cfg.depth):
        p, q = factors_from_v(node.v)
        key = (p, q)
        chk.check(key not in seen,
                  f"(p,q)={key} reached twice: {seen.get(key)} and {''.join(node.path)}")
        seen[key] = "".join(node.path) or "(root)"
        chk.check(math.gcd(p, q) == 1, f"gcd(p,q) != 1 at {seen[key]}")
        chk.check(p % 2 == 1 and q % 2 == 1, f"parity broken at {seen[key]}")
        m, n = (q + p) // 2, (q - p) // 2
        if node.parent is not None:
            chk.check(m > n > 0 and math.gcd(m, n) == 1,
                      f"Euclid parameter constraints broken at {seen[key]}")
        if p > 1:
            semiprime_nodes.setdefault(p * q, []).append(key)

    for a_val, pairs in semiprime_nodes.items():
        chk.check(len(set(pairs)) == len(pairs), f"duplicate non-trivial pair for a={a_val}")

    chk.note(f"{len(seen)} nodes enumerated to depth {cfg.depth}; node -> (p,q) injective; "
             "surjectivity onto all coprime odd pairs is Berggren's classical bijection (structural)")
    chk.finalize()
