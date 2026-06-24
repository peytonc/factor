# Per-theorem test suite

Standard pytest suite that has one test file per theorem, each exposing a single dedicated test function. 
A regression now isolates to exactly one failing test instead of a whole cluster.

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
