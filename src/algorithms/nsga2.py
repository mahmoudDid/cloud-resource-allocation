"""Non-dominated Sorting Genetic Algorithm II (NSGA-II) for Pareto Multi-Objective Optimization.

Assigned to: Team Member 3 / Advanced Track
"""

from __future__ import annotations

from typing import List, Optional
import numpy as np

from src.algorithms.base import BaseScheduler
from src.models.cloud_environment import CloudEnvironment
from src.simulation.scheduler import SchedulingOutcome


class NSGA2Scheduler(BaseScheduler):
    """NSGA-II for multi-objective cloud scheduling (Pareto Front)."""

    name = "NSGA-II"

    def __init__(
        self,
        population_size: int = 60,
        generations: int = 50,
        crossover_rate: float = 0.90,
        mutation_rate: float = 0.05,
    ) -> None:
        self.population_size = population_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def schedule(
        self,
        env: CloudEnvironment,
        rng_seed: Optional[int] = 42,
    ) -> SchedulingOutcome:
        """Run NSGA-II to discover the non-dominated Pareto front."""
        # TODO (Advanced): Implement fast non-dominated sorting and crowding distance calculation.
        raise NotImplementedError("TODO: Implement NSGA2Scheduler.schedule()")
