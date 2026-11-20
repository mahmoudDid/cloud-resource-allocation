"""Individual objective functions and metrics normalization.

Assigned to: Team Member 3 (GA Specialist) & Team Member 2 (Metrics Specialist)
"""

from __future__ import annotations

from typing import Dict, List
import numpy as np


def compute_normalized_value(raw_val: float, min_val: float, max_val: float) -> float:
    """Normalize raw objective metric to [0, 1] range via min-max scaling."""
    # TODO (Team Member 3): Implement min-max normalization with zero-division safeguard.
    raise NotImplementedError("TODO: Implement compute_normalized_value()")


def compute_load_imbalance(vm_busy_times: List[float]) -> float:
    """Calculate load imbalance degree across VMs:
    
    Formula:
        DI = (T_max - T_min) / T_avg
    where T is the busy execution time of each VM.
    """
    # TODO (Team Member 2): Implement load imbalance formula.
    raise NotImplementedError("TODO: Implement compute_load_imbalance()")
