"""
Every theorem validator in ``validators/`` is assembled from the primitives in
this module.  Nothing here encodes the *statement* of any particular theorem.
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import Dict, Iterator, List, Optional, Sequence, Tuple

Vec = Tuple[int, int, int]
Mat = Tuple[Tuple[int, int, int], Tuple[int, int, int], Tuple[int, int, int]]

# --------------------------------------------------------------------------
# Constants (single source: glossary.md at the repository root)
# --------------------------------------------------------------------------

A: Mat = ((1, 0, 0), (4, 1, 4), (2, 0, 1))
B: Mat = ((0, 1, 0), (1, 4, 4), (0, 2, 1))
C: Mat = ((0, 1, 0), (1, 4, -4), (0, 2, -1))
GENS: Dict[str, Mat] = {"A": A, "B": B, "C": C}
GEN_NAMES: Tuple[str, ...] = ("A", "B", "C")

BERGGREN: Dict[str, Mat] = {
    "A": ((1, -2, 2), (2, -1, 2), (2, -2, 3)),
    "B": ((1, 2, 2), (2, 1, 2), (2, 2, 3)),
    "C": ((-1, 2, 2), (-2, 1, 2), (-2, 2, 3)),
}

V_ROOT: Vec = (1, 9, 3)      # [p^2, q^2, a] at the root node (p, q) = (1, 3)
GEO_ROOT: Vec = (3, 4, 5)    # (a, b, c) at the root node

# T11 sibling-divergence vectors and their halves (T17)
DELTA: Dict[str, Vec] = {"a": (0, 8, 2), "b": (2, 6, 4)}
E_HALF: Dict[str, Vec] = {"a": (0, 4, 1), "b": (1, 3, 2)}

IDENTITY: Mat = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

# --------------------------------------------------------------------------
# Exact 3x3 integer linear algebra
# --------------------------------------------------------------------------

def mat_vec(m: Mat, v: Sequence[int]) -> Vec:
    return tuple(m[i][0] * v[0] + m[i][1] * v[1] + m[i][2] * v[2] for i in range(3))  # type: ignore


def mat_mul(x: Mat, y: Mat) -> Mat:
    return tuple(
        tuple(sum(x[i][k] * y[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore


def vec_add(u: Sequence[int], v: Sequence[int]) -> Vec:
    return (u[0] + v[0], u[1] + v[1], u[2] + v[2])


def vec_sub(u: Sequence[int], v: Sequence[int]) -> Vec:
    return (u[0] - v[0], u[1] - v[1], u[2] - v[2])


def vec_scale(k: int, v: Sequence[int]) -> Vec:
    return (k * v[0], k * v[1], k * v[2])


def vec_mod(v: Sequence[int], m: int) -> Vec:
    return (v[0] % m, v[1] % m, v[2] % m)


def mat_mod(mat: Mat, m: int) -> Mat:
    return tuple(tuple(x % m for x in row) for row in mat)  # type: ignore


def det3(m: Mat) -> int:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def adjugate3(m: Mat) -> Mat:
    c = [[0] * 3 for _ in range(3)]
    idx = ((1, 2), (0, 2), (0, 1))
    for i in range(3):
        for j in range(3):
            r0, r1 = idx[i]
            c0, c1 = idx[j]
            minor = m[r0][c0] * m[r1][c1] - m[r0][c1] * m[r1][c0]
            c[j][i] = ((-1) ** (i + j)) * minor  # transpose of cofactors
    return tuple(tuple(row) for row in c)  # type: ignore


def mat_inv_mod(m: Mat, mod: int) -> Mat:
    """Inverse of m in GL(3, Z/modZ).  Requires gcd(det(m), mod) == 1."""
    d = det3(m) % mod
    dinv = pow(d, -1, mod)
    adj = adjugate3(m)
    return tuple(tuple((dinv * x) % mod for x in row) for row in adj)  # type: ignore


# --------------------------------------------------------------------------
# Paths and tree enumeration
# --------------------------------------------------------------------------

def apply_path(path: Sequence[str], v: Vec = V_ROOT) -> Vec:
    """Apply generators in chronological (traversal) order."""
    for g in path:
        v = mat_vec(GENS[g], v)
    return v


def path_matrix(path: Sequence[str]) -> Mat:
    """Matrix product of a path, accumulated right-to-left:
    for path (g1, ..., gn) returns G_n * ... * G_1  (glossary convention)."""
    p = IDENTITY
    for g in path:
        p = mat_mul(GENS[g], p)
    return p


@dataclass
class Node:
    path: Tuple[str, ...]
    v: Vec
    parent: Optional["Node"]
    gen: Optional[str]  # generator that produced this node (None at root)

    @property
    def depth(self) -> int:
        return len(self.path)


def enumerate_tree(depth: int) -> Iterator[Node]:
    """Yield every node of the Berggren factor-state tree to the given depth,
    in breadth-first order (parents always precede children).
    Node count to depth d is (3**(d+1) - 1) // 2  (1,093 nodes at d = 6)."""
    root = Node((), V_ROOT, None, None)
    yield root
    frontier = [root]
    for _ in range(depth):
        nxt: List[Node] = []
        for nd in frontier:
            for g in GEN_NAMES:
                child = Node(nd.path + (g,), mat_vec(GENS[g], nd.v), nd, g)
                nxt.append(child)
                yield child
        frontier = nxt


# --------------------------------------------------------------------------
# Factor recovery and PPT geometry
# --------------------------------------------------------------------------

def factors_from_v(v: Vec) -> Tuple[int, int]:
    """Recover (p, q) from v = [p^2, q^2, a]; raises if v is not a valid state."""
    p = math.isqrt(v[0])
    q = math.isqrt(v[1])
    if p * p != v[0] or q * q != v[1] or p * q != v[2]:
        raise ValueError(f"invalid state vector {v}")
    return p, q


def geo_from_pq(p: int, q: int) -> Vec:
    """(a, b, c) from the factor pair, via the glossary identities."""
    return (p * q, (q * q - p * p) // 2, (p * p + q * q) // 2)


def parent_legs(v_parent: Vec) -> Tuple[int, int]:
    """(a_parent, b_parent) of a node, per the glossary definitions."""
    return v_parent[2], (v_parent[1] - v_parent[0]) // 2


# --------------------------------------------------------------------------
# Swap / differential helpers (T12-T15, T17)
# --------------------------------------------------------------------------

def swap_kind(g1: str, g2: str) -> str:
    """'a' for a B<->C swap, 'b' for an A<->B swap (matches delta_a / delta_b)."""
    pair = {g1, g2}
    if pair == {"B", "C"}:
        return "a"
    if pair == {"A", "B"}:
        return "b"
    raise ValueError(f"non-adjacent swap {g1}<->{g2}")


def sigma(key_gen: str, shadow_gen: str) -> int:
    """Directional swap sign per the glossary: +1 if the shadow generator is B
    (i.e. (C -> B) or (A -> B)), -1 if the key generator is B."""
    swap_kind(key_gen, shadow_gen)  # validates adjacency
    return 1 if shadow_gen == "B" else -1


def alpha_for(kind: str, v_parent: Vec) -> int:
    a_par, b_par = parent_legs(v_parent)
    return a_par if kind == "a" else b_par


def adjacent_partner(gen: str, rng: random.Random) -> str:
    """A valid adjacent swap partner: A->B, C->B, B->(A or C, randomly)."""
    if gen == "B":
        return rng.choice(("A", "C"))
    return "B"


def make_shadow(key: Sequence[str], idxs: Sequence[int], rng: random.Random) -> Tuple[str, ...]:
    shadow = list(key)
    for i in idxs:
        shadow[i] = adjacent_partner(key[i], rng)
    return tuple(shadow)


def random_path(rng: random.Random, n: int) -> Tuple[str, ...]:
    return tuple(rng.choice(GEN_NAMES) for _ in range(n))


# --------------------------------------------------------------------------
# Modular-orbit machinery (T05-T10)
# --------------------------------------------------------------------------

_ORBIT_CACHE: Dict[int, frozenset] = {}


def orbit(modulus: int) -> frozenset:
    """Orbit(M): closure of v_root mod M under forward application of A, B, C."""
    if modulus in _ORBIT_CACHE:
        return _ORBIT_CACHE[modulus]
    gens = [mat_mod(GENS[g], modulus) for g in GEN_NAMES]
    start = vec_mod(V_ROOT, modulus)
    seen = {start}
    stack = [start]
    while stack:
        v = stack.pop()
        for gm in gens:
            w = vec_mod(mat_vec(gm, v), modulus)
            if w not in seen:
                seen.add(w)
                stack.append(w)
    result = frozenset(seen)
    _ORBIT_CACHE[modulus] = result
    return result


def backward_reachable(modulus: int) -> frozenset:
    """States that can reach v_root (mod M) along forward edges; computed as the
    closure of the root under the inverse generators."""
    invs = [mat_inv_mod(GENS[g], modulus) for g in GEN_NAMES]
    start = vec_mod(V_ROOT, modulus)
    seen = {start}
    stack = [start]
    while stack:
        v = stack.pop()
        for gm in invs:
            w = vec_mod(mat_vec(gm, v), modulus)
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return frozenset(seen)


def prime_power_factorization(n: int) -> List[Tuple[int, int]]:
    """[(p, k), ...] with n = prod p**k, by trial division (n is small here)."""
    out: List[Tuple[int, int]] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            k = 0
            while n % d == 0:
                n //= d
                k += 1
            out.append((d, k))
        d += 1
    if n > 1:
        out.append((n, 1))
    return out


# --------------------------------------------------------------------------
# Uniform result type
# --------------------------------------------------------------------------

@dataclass
class Result:
    tid: str
    title: str
    checks: int = 0
    failures: int = 0
    notes: List[str] = field(default_factory=list)
    _max_recorded: int = 5

    def check(self, cond: bool, msg: str = "") -> bool:
        self.checks += 1
        if not cond:
            self.failures += 1
            if msg and len(self.notes) < self._max_recorded:
                self.notes.append("FAIL: " + msg)
        return cond

    def note(self, msg: str) -> None:
        self.notes.append(msg)

    @property
    def ok(self) -> bool:
        return self.checks > 0 and self.failures == 0

    @property
    def status(self) -> str:
        return "PASS" if self.ok else "FAIL"


@dataclass
class Config:
    """Knobs shared by all validators (kept on one object so the runner can
    pass a single value to every validation method)."""
    depth: int = 6                    # full-tree enumeration depth (1,093 nodes)
    trials: int = 400                 # random trials per stochastic validator
    seed: int = 20260610              # fixed seed -> reproducible runs
    primes: Tuple[int, ...] = (3, 5, 7, 11, 13)
    prime_powers: Tuple[int, ...] = (9, 25, 27, 49, 121)
    squarefree: Tuple[int, ...] = (15, 21, 33, 35, 105)
    mixed_odd: Tuple[int, ...] = (45, 63, 75, 99)

    def rng(self, salt: str) -> random.Random:
        return random.Random(f"{self.seed}:{salt}")
