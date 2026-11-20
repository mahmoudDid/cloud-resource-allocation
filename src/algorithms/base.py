"""Base class for all cloud scheduling algorithms."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from src.models.cloud_environment import CloudEnvironment
from src.simulation.scheduler import SchedulingOutcome


class BaseScheduler(ABC):
    """Abstract base class that all cloud scheduling algorithms must inherit from."""

    name: str = "BaseScheduler"

    @abstractmethod
    def schedule(
        self,
        env: CloudEnvironment,
        rng_seed: Optional[int] = 42,
    ) -> SchedulingOutcome:
        """Execute scheduling on the cloud environment and return a SchedulingOutcome.

        Args:
            env: The CloudEnvironment containing tasks and virtual machines.
            rng_seed: Optional random seed for reproducibility.

        Returns:
            SchedulingOutcome containing the chromosome, execution metrics, and runtime.
        """
        pass
