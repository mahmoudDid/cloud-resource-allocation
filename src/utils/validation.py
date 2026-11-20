"""Validation helper functions."""

from typing import Any


def validate_positive(val: Any, name: str) -> float:
    """Ensure val is a positive float."""
    f = float(val)
    if f <= 0:
        raise ValueError(f"{name} must be strictly positive (> 0), got {val}")
    return f


def validate_non_negative(val: Any, name: str) -> float:
    """Ensure val is a non-negative float."""
    f = float(val)
    if f < 0:
        raise ValueError(f"{name} must be non-negative (>= 0), got {val}")
    return f
