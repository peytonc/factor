"""
Shared test helper: ``Checker``
===============================

Each theorem test runs *many* sub-checks (often thousands of exact-integer
identities over an enumerated tree or random trials). A bare ``assert`` would
abort at the first mismatch and hide how many cases actually pass. ``Checker``
preserves the original suite's behaviour — count every sub-check, keep going on
failure, then report an aggregate — while still letting each theorem live in its
own ``test_tNN`` function so a regression is isolated to a single failing test.

Usage inside a test::

    def test_t04(cfg):
        chk = Checker("T04", "Monotonic Growth")
        for node in enumerate_tree(cfg.depth):
            chk.check(node.v[2] > node.parent.v[2], "a did not grow ...")
        chk.finalize()        # raises AssertionError iff any sub-check failed

This mirrors the old ``core.Result.check`` API one-for-one, so porting a
``validate_tNN(cfg) -> Result`` body into a ``test_tNN`` is a near-mechanical
swap of ``r`` for ``chk`` plus a trailing ``chk.finalize()``.
"""
from __future__ import annotations

from typing import List


class Checker:
    """Aggregates the outcome of many sub-checks for a single theorem.

    ``finalize`` turns the aggregate into a normal pytest assertion: it passes
    silently when every sub-check held, and raises a single ``AssertionError``
    summarising the failures (with up to ``max_recorded`` example messages)
    otherwise.
    """

    def __init__(self, tid: str, title: str, max_recorded: int = 10) -> None:
        self.tid = tid
        self.title = title
        self.checks = 0
        self.failures = 0
        self.messages: List[str] = []
        self.notes: List[str] = []
        self._max = max_recorded

    def check(self, cond: bool, msg: str = "") -> bool:
        """Record one sub-check. Returns the (bool) condition so callers may
        branch on it, exactly like the original ``Result.check``."""
        self.checks += 1
        if not cond:
            self.failures += 1
            if msg and len(self.messages) < self._max:
                self.messages.append(msg)
        return bool(cond)

    def note(self, msg: str) -> None:
        """Attach an informational note (shown only on failure / via -s logging)."""
        self.notes.append(msg)

    def finalize(self) -> None:
        """Assert that the theorem held across every recorded sub-check."""
        assert self.checks > 0, f"{self.tid} ({self.title}): no checks were executed"
        if self.failures:
            detail = "\n  ".join(self.messages) or "(no example messages captured)"
            extra = ""
            if self.failures > len(self.messages):
                extra = f"\n  ... and {self.failures - len(self.messages)} more"
            raise AssertionError(
                f"{self.tid} ({self.title}): "
                f"{self.failures}/{self.checks} sub-checks FAILED\n  {detail}{extra}"
            )
