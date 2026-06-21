"""
pytest configuration for the per-theorem validation suite.

Responsibilities:
  * make the shared math kernel (``validation/core.py``) and this ``tests/``
    directory importable from every test module;
  * re-expose the old runner's command-line knobs (``--depth``, ``--trials``,
    ``--seed``) as pytest options;
  * provide a single session-scoped ``cfg`` fixture (a ``core.Config``) that
    every ``test_tNN`` consumes, so all theorems share one configuration object
    just as they did under the original runner.

Run the whole suite from the repository root with::

    pytest                                  # defaults: depth 6, 400 trials
    pytest --depth 7 --trials 2000          # strengthen the evidence
    pytest tests/test_t17_multiswap_differential.py   # one theorem in isolation

pytest's exit code is non-zero iff any theorem fails, so it doubles as the CI
gate that ``run_validation.py`` used to provide.
"""
from __future__ import annotations

import os
import sys

import pytest

_HERE = os.path.dirname(os.path.abspath(__file__))
# The shared kernel lives in ../validation/core.py relative to this tests/ dir.
_KERNEL_DIR = os.path.abspath(os.path.join(_HERE, "..", "validation"))

for _p in (_KERNEL_DIR, _HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from core import Config  # noqa: E402  (import after sys.path is set up)


def pytest_addoption(parser: "pytest.Parser") -> None:
    parser.addoption(
        "--depth", action="store", default=6, type=int,
        help="full-tree enumeration depth (default 6 -> 1,093 nodes)",
    )
    parser.addoption(
        "--trials", action="store", default=400, type=int,
        help="random trials per stochastic validator (default 400)",
    )
    parser.addoption(
        "--seed", action="store", default=20260610, type=int,
        help="RNG seed for reproducibility",
    )


@pytest.fixture(scope="session")
def cfg(request: "pytest.FixtureRequest") -> Config:
    """The shared validation configuration, built from the CLI options."""
    return Config(
        depth=request.config.getoption("--depth"),
        trials=request.config.getoption("--trials"),
        seed=request.config.getoption("--seed"),
    )
