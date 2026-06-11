"""
Foundations cluster (T01-T04).

Theorem-specific logic in this module is intentionally thin; the heavy lifting
(tree enumeration, matrix algebra, factor recovery) comes from ``core``.

Independent code per theorem:
  T01 - the factor-recursion table {A,B,C} -> (p', q') and the algebra<->geometry
        cross-check predicate.
  T02 - the closed-form a = 3 + 2d on the all-A branch.
  T03 - the injectivity bookkeeping (seen (p,q) pairs) plus PPT constraints.
  T04 - the strict-growth predicate a_child > a_parent.
"""
from __future__ import annotations

import math

from core import (
    A, B, C, BERGGREN, Config, GEN_NAMES, GENS, GEO_ROOT, Result, V_ROOT,
    apply_path, det3, enumerate_tree, factors_from_v, geo_from_pq, mat_vec,
    random_path,
)

# Factor recursion implied by T01 / used in the T16 proof.
FACTOR_RECURSION = {
    "A": lambda p, q: (p, 2 * p + q),
    "B": lambda p, q: (q, 2 * q + p),
    "C": lambda p, q: (q, 2 * q - p),
}


def validate_t01(cfg: Config) -> Result:
    r = Result("T01", "Linearized Algebraic State Transition")

    # Determinant / orientation claims.
    r.check(det3(A) == 1, "det(A) != 1")
    r.check(det3(B) == -1, "det(B) != -1")
    r.check(det3(C) == 1, "det(C) != 1")

    # Full-tree cross-check: algebraic action (A/B/C on v) must commute with
    # the geometric action (Berggren matrices on (a,b,c)) and with the factor
    # recursion on (p, q), and every state must satisfy the PPT identities.
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

        ok_state = node.v == (p * p, q * q, p * q)
        r.check(ok_state, f"v mismatch at {''.join(node.path)}")
        ok_geo = geo_child == geo_from_pq(p, q)
        r.check(ok_geo, f"geometry mismatch at {''.join(node.path)}")
        a, b, c = geo_child
        r.check(p * p == c - b and q * q == c + b,
                f"p^2=c-b / q^2=c+b broken at {''.join(node.path)}")
        r.check(math.gcd(p, q) == 1 and p % 2 == 1 and q % 2 == 1 and p < q,
                f"factor constraints broken at {''.join(node.path)}")
        # Promotion claims: A preserves p; B and C promote old q to new p.
        if g == "A":
            r.check(p == p_par, "A failed to preserve p")
        else:
            r.check(p == q_par, f"{g} failed to promote q to p")
    return r


def validate_t02(cfg: Config) -> Result:
    r = Result("T02", "Trivial Path (Unique Existence)")
    v = V_ROOT
    n_steps = 2000
    for d in range(n_steps + 1):
        r.check(v[0] == 1, f"p^2 != 1 at A-depth {d}")
        r.check(v[2] == 3 + 2 * d, f"a != 3 + 2d at A-depth {d}")
        v = mat_vec(GENS["A"], v)
    # Spot-check the depth formula d_target = (a_target - 3)/2 for sample odd
    # targets, including a semiprime-style value.
    for a_target in (15, 35, 143, 3 + 2 * 1234):
        d_target = (a_target - 3) // 2
        v = V_ROOT
        for _ in range(d_target):
            v = mat_vec(GENS["A"], v)
        r.check(v == (1, a_target * a_target, a_target),
                f"trivial node wrong for a_target={a_target}")
    r.note(f"all-A branch walked to depth {n_steps}; a hits every odd >= 3 exactly once")
    return r


def validate_t03(cfg: Config) -> Result:
    r = Result("T03", "Non-Trivial Unique Path (Unique Existence)")
    seen = {}
    semiprime_nodes = {}
    for node in enumerate_tree(cfg.depth):
        p, q = factors_from_v(node.v)
        key = (p, q)
        r.check(key not in seen,
                f"(p,q)={key} reached twice: {seen.get(key)} and {''.join(node.path)}")
        seen[key] = "".join(node.path) or "(root)"
        r.check(math.gcd(p, q) == 1, f"gcd(p,q) != 1 at {seen[key]}")
        r.check(p % 2 == 1 and q % 2 == 1, f"parity broken at {seen[key]}")
        m, n = (q + p) // 2, (q - p) // 2
        if node.parent is not None:
            r.check(m > n > 0 and math.gcd(m, n) == 1,
                    f"Euclid parameter constraints broken at {seen[key]}")
        if p > 1:
            semiprime_nodes.setdefault(p * q, []).append(key)
    # Within the enumerated horizon, every odd leg with a non-trivial pair is
    # hit by exactly one (p,q) per pair (uniqueness of the non-trivial node for
    # a semiprime follows from injectivity + the unique factor pair).
    for a_val, pairs in semiprime_nodes.items():
        r.check(len(set(pairs)) == len(pairs), f"duplicate non-trivial pair for a={a_val}")
    r.note(f"{len(seen)} nodes enumerated to depth {cfg.depth}; node -> (p,q) injective; "
           "surjectivity onto all coprime odd pairs is Berggren's classical bijection (structural)")
    return r


def validate_t04(cfg: Config) -> Result:
    r = Result("T04", "Monotonic Growth")
    for node in enumerate_tree(cfg.depth):
        if node.parent is not None:
            r.check(node.v[2] > node.parent.v[2],
                    f"a did not grow at {''.join(node.path)}")
    # Deep random paths (growth must hold far beyond the enumeration horizon).
    rng = cfg.rng("t04")
    for _ in range(50):
        v = V_ROOT
        for g in random_path(rng, 200):
            w = mat_vec(GENS[g], v)
            r.check(w[2] > v[2], "a did not grow on deep random path")
            v = w
    return r
