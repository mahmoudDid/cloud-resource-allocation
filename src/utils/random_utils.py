"""Random generator reproducibility helper."""

from typing import Optional
import numpy as np


def create_rng(seed: Optional[int] = 42) -> np.random.Generator:
    """Create a reproducible NumPy random generator."""
    return np.random.default_rng(seed)
