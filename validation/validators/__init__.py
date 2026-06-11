"""Registry of theorem validators in catalog order (T01..T17).

Each entry is a callable with the uniform signature ``f(cfg: Config) -> Result``,
so the runner can treat every validation method identically.
"""
from __future__ import annotations

from validators import foundations, modular, differential

REGISTRY = (
    foundations.validate_t01,
    foundations.validate_t02,
    foundations.validate_t03,
    foundations.validate_t04,
    modular.validate_t05,
    modular.validate_t06,
    modular.validate_t07,
    modular.validate_t08,
    modular.validate_t09,
    modular.validate_t10,
    differential.validate_t11,
    differential.validate_t12,
    differential.validate_t13,
    differential.validate_t14,
    differential.validate_t15,
    differential.validate_t16,
    differential.validate_t17,
)
