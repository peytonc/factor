# Per-theorem test suite

This directory replaces the old single-runner validation mechanism
(`validation/validators/` + `validation/run_validation.py`) with a standard
pytest suite that has **one test file per theorem** (`test_t01_*.py` …
`test_t17_*.py`), each exposing a single dedicated test function
(`test_t01` … `test_t17`). A regression now isolates to exactly one failing
test instead of a whole cluster.

## Layout

```
factor/
├── pytest.ini                 # rootdir config (testpaths = tests)
├── validation/
│   └── core.py                # shared math kernel — KEPT UNCHANGED (reference #1)
└── tests/
    ├── conftest.py            # sys.path wiring + --depth/--trials/--seed + cfg fixture
    ├── checker.py             # shared test harness: Checker (reference #2)
    ├── test_t01_linearized_state_transition.py
    ├── test_t02_trivial_path_existence.py
    ├── …
    └── test_t17_multiswap_differential.py
```

Shared functionality lives in exactly **two** reference pieces, as required:

1. **`validation/core.py`** — the existing math kernel (generator matrices,
   exact 3×3 integer linear algebra, tree enumeration, orbit machinery, swap
   helpers, `Config`). Reused as-is; it remains the single source of the
   constants from `glossary.md`.
2. **`tests/checker.py`** — the `Checker` class, which replaces the old
   `core.Result`. It lets each theorem run thousands of exact sub-checks,
   counts them all, keeps going on failure, and then `finalize()` turns the
   aggregate into one pytest assertion with an informative summary.

The two small helpers that were genuinely shared between theorems in the old
`differential.py` (`_fork_congruence` for T12/T13, `_swap_data` for T14/T17)
are short and are kept local to each theorem file, so the only cross-theorem
imports are the kernel and the `Checker`. Single-theorem helpers
(`_t15_case`, `_t17_predictions`, the T01 factor recursion, `SWAP_PAIRS`) live
beside the theorem that uses them.

## Running

From the repository root:

```bash
pytest                                   # defaults: depth 6, 400 trials
pytest -v                                # one line per theorem
pytest --depth 7 --trials 2000           # strengthen the evidence
pytest --seed 12345                       # different reproducible RNG stream
pytest tests/test_t17_multiswap_differential.py   # a single theorem in isolation
pytest -k "t05 or t09"                    # a subset
```

pytest's exit code is non-zero iff any theorem fails, so it is a drop-in CI
gate for the old `run_validation.py` (see `.github/workflows/validate.yml`).

## Behavioural parity with the old runner

At the default configuration (`depth=6, trials=400, seed=20260610`) every test
executes the identical set of sub-checks as the corresponding
`validate_tNN`. The one intentional difference is **T17**: the original runner
only *reported* that the literal-text reading of `R_m` matched in 0 cases (an
honesty note); the refactored `test_t17` additionally **asserts**
`literal_hits == 0`, turning that documented off-by-one finding into an
enforced check (hence one extra sub-check vs the old count).

## Superseded files

The following are replaced by this suite and can be deleted from the repo:

- `validation/validators/__init__.py`
- `validation/validators/foundations.py`
- `validation/validators/modular.py`
- `validation/validators/differential.py`
- `validation/run_validation.py`

`validation/core.py` is **retained** — it is the shared kernel the tests import.
