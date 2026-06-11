"""
Modular theory cluster (T05-T10).

Everything orbit-related (orbit closure, matrix inverses mod M, backward
reachability, prime-power factorization) is shared kernel code in ``core``.

Independent code per theorem:
  T05 - the stepwise-mod vs reduce-at-the-end equivalence predicate.
  T06 - invertibility assertions + the strong-connectivity criterion
        (forward orbit == backward-reachable set).
  T07 - the axis-alignment biconditional on orbit states.
  T08 - the three closed-form cardinality formulas.
  T09 - CRT product-set comparison for square-free moduli.
  T10 - Hensel fiber counting for prime powers + the general product law.
"""
from __future__ import annotations

from collections import Counter
from itertools import product as iproduct

from core import (
    Config, GEN_NAMES, GENS, IDENTITY, Result, V_ROOT, apply_path,
    backward_reachable, det3, mat_inv_mod, mat_mod, mat_mul, mat_vec, orbit,
    prime_power_factorization, random_path, vec_mod,
)


def validate_t05(cfg: Config) -> Result:
    r = Result("T05", "Modular Algebraic State Transition")
    rng = cfg.rng("t05")
    moduli = cfg.primes + cfg.prime_powers + cfg.squarefree + cfg.mixed_odd
    for _ in range(cfg.trials // 4):
        path = random_path(rng, rng.randint(1, 30))
        v_int = apply_path(path)                      # exact over Z, then reduce
        for m in (rng.choice(moduli), rng.choice(moduli)):
            v_mod = vec_mod(V_ROOT, m)                # reduce at every step
            for g in path:
                v_mod = vec_mod(mat_vec(mat_mod(GENS[g], m), v_mod), m)
            r.check(v_mod == vec_mod(v_int, m),
                    f"homomorphism broken: M={m}, path={''.join(path)}")
    r.note(f"stepwise reduction == reduce-at-end for random paths over {len(moduli)} odd moduli")
    return r


def validate_t06(cfg: Config) -> Result:
    r = Result("T06", "Modular Orbit Graph (Finite State Machine)")
    moduli = cfg.primes + cfg.prime_powers + cfg.squarefree + cfg.mixed_odd
    for m in moduli:
        # Generators are units of GL(3, Z/MZ): det = +-1 and an explicit inverse.
        for name in GEN_NAMES:
            g = GENS[name]
            r.check(abs(det3(g)) == 1, f"det({name}) not a unit")
            ginv = mat_inv_mod(g, m)
            r.check(mat_mod(mat_mul(g, ginv), m) == mat_mod(IDENTITY, m),
                    f"{name}^-1 wrong mod {m}")
        o = orbit(m)
        # Each generator permutes the orbit (image of the orbit is the orbit).
        for name in GEN_NAMES:
            gm = mat_mod(GENS[name], m)
            image = {vec_mod(mat_vec(gm, v), m) for v in o}
            r.check(image == o, f"{name} does not permute Orbit({m})")
        # Strong connectivity: every reachable state can also reach the root.
        bk = backward_reachable(m)
        r.check(o <= bk, f"Orbit({m}) not strongly connected")
    r.note(f"checked invertibility, permutation action, strong connectivity for M in {list(moduli)}")
    return r


def validate_t07(cfg: Config) -> Result:
    r = Result("T07", "Prime Modular Axis Alignment")
    for m in cfg.primes:
        for v in orbit(m):
            zero_leg = v[2] % m == 0
            on_one_axis = (v[0] % m == 0) ^ (v[1] % m == 0)
            r.check(zero_leg == on_one_axis, f"axis biconditional broken mod {m} at {v}")
            r.check(not (v[0] % m == 0 and v[1] % m == 0),
                    f"origin reached mod {m} at {v}")
    return r


def validate_t08(cfg: Config) -> Result:
    r = Result("T08", "Prime Modular Orbit Cardinality")
    for m in cfg.primes:
        o = orbit(m)
        r.check(len(o) == (m * m - 1) // 2, f"|Orbit({m})| != (M^2-1)/2")
        counts = Counter(v[2] % m for v in o)
        r.check(counts.get(0, 0) == m - 1, f"axis count != M-1 mod {m}")
        for k in range(1, m):
            r.check(counts.get(k, 0) == (m - 1) // 2,
                    f"residue {k} count != (M-1)/2 mod {m}")
    return r


def validate_t09(cfg: Config) -> Result:
    r = Result("T09", "Square-Free Modular Orbit Decomposition")
    for m in cfg.squarefree:
        primes = [p for p, k in prime_power_factorization(m)]
        o_m = orbit(m)
        prime_orbits = [orbit(p) for p in primes]
        expected = 1
        for o_p in prime_orbits:
            expected *= len(o_p)
        r.check(len(o_m) == expected, f"|Orbit({m})| != prod |Orbit(p_i)|")
        # Phi is a bijection onto the full Cartesian product (CRT): compare the
        # exact image set against the exact product set.
        image = {tuple(vec_mod(v, p) for p in primes) for v in o_m}
        full_product = set(iproduct(*prime_orbits))
        r.check(image == full_product, f"Phi image != Cartesian product for M={m}")
    return r


def validate_t10(cfg: Config) -> Result:
    r = Result("T10", "Generalized Modular Orbit Decomposition")
    # Hensel lifting law on prime powers: |O_(p^k)| = p^(2(k-1)) * |O_p|, with
    # surjective projection and uniform fiber size p^(2(k-1)).
    for pk in cfg.prime_powers:
        ((p, k),) = prime_power_factorization(pk)
        o_pk = orbit(pk)
        o_p = orbit(p)
        fiber = p ** (2 * (k - 1))
        r.check(len(o_pk) == fiber * len(o_p), f"|Orbit({pk})| != p^(2(k-1)) |Orbit({p})|")
        fibers = Counter(vec_mod(v, p) for v in o_pk)
        r.check(set(fibers) == set(o_p), f"projection Orbit({pk}) -> Orbit({p}) not onto")
        r.check(all(c == fiber for c in fibers.values()),
                f"non-uniform Hensel fibers for {pk}")
    # General odd M: product over maximal prime-power components.
    for m in cfg.mixed_odd:
        comps = [p ** k for p, k in prime_power_factorization(m)]
        o_m = orbit(m)
        comp_orbits = [orbit(q) for q in comps]
        expected = 1
        for o_q in comp_orbits:
            expected *= len(o_q)
        r.check(len(o_m) == expected, f"|Orbit({m})| != prod |Orbit(Q_i)|")
        image = {tuple(vec_mod(v, q) for q in comps) for v in o_m}
        r.check(image == set(iproduct(*comp_orbits)),
                f"Phi image != product of prime-power orbits for M={m}")
    return r
