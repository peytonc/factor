#!/usr/bin/env python3
"""Run the full theorem validation suite.

Usage (from the repository root):

    python validation/run_validation.py [--depth 6] [--trials 400]
                                        [--seed 20260610] [--csv PATH]

Exit code is 0 only if every validator passes (CI friendly).
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core import Config  # noqa: E402
from validators import REGISTRY  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Berggren/PPT theorem validation suite")
    parser.add_argument("--depth", type=int, default=6,
                        help="full-tree enumeration depth (default 6 -> 1,093 nodes)")
    parser.add_argument("--trials", type=int, default=400,
                        help="random trials per stochastic validator (default 400)")
    parser.add_argument("--seed", type=int, default=20260610,
                        help="RNG seed for reproducibility")
    parser.add_argument("--csv", type=str, default=None,
                        help="optional path for a CSV results file")
    args = parser.parse_args()

    cfg = Config(depth=args.depth, trials=args.trials, seed=args.seed)
    print(f"Berggren/PPT theorem validation suite")
    print(f"depth={cfg.depth} (nodes={(3 ** (cfg.depth + 1) - 1) // 2}), "
          f"trials={cfg.trials}, seed={cfg.seed}\n")

    header = f"{'ID':<5}{'Status':<8}{'Checks':>9}{'Failures':>10}  Title"
    print(header)
    print("-" * len(header))

    rows = []
    all_ok = True
    t_start = time.time()
    for validator in REGISTRY:
        t0 = time.time()
        result = validator(cfg)
        elapsed = time.time() - t0
        all_ok = all_ok and result.ok
        print(f"{result.tid:<5}{result.status:<8}{result.checks:>9}{result.failures:>10}"
              f"  {result.title}  [{elapsed:.2f}s]")
        for note in result.notes:
            print(f"      - {note}")
        rows.append((result.tid, result.title, result.status, result.checks,
                     result.failures, " | ".join(result.notes)))

    total_checks = sum(r[3] for r in rows)
    total_failures = sum(r[4] for r in rows)
    print("-" * len(header))
    print(f"TOTAL: {total_checks} checks, {total_failures} failures "
          f"in {time.time() - t_start:.1f}s -> "
          f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    if args.csv:
        with open(args.csv, "w", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["id", "title", "status", "checks", "failures", "notes"])
            writer.writerows(rows)
        print(f"CSV written to {args.csv}")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
