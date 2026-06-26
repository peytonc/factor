"""
pytest configuration for the per-theorem test suite.

Responsibilities:
  * make the shared math kernel (``tests/core.py``) and this ``tests/``
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
"""
from __future__ import annotations

import pytest

from core import Config


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
    """The shared test configuration, built from the CLI options."""
    return Config(
        depth=request.config.getoption("--depth"),
        trials=request.config.getoption("--trials"),
        seed=request.config.getoption("--seed"),
    )
