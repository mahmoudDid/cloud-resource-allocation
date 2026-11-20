"""Synthetic workload generator.

Assigned to: Team Member 1 (Cloud Environment & Modeling)
"""

from __future__ import annotations

from typing import List, Optional
import numpy as np

from src.models.cloud_environment import CloudEnvironment
from src.models.task import Task
from src.models.virtual_machine import VirtualMachine


class WorkloadGenerator:
    """Generates synthetic tasks and heterogeneous VMs according to statistical distributions."""

    def __init__(self, seed: Optional[int] = 42) -> None:
        self.rng = np.random.default_rng(seed)

    def generate_tasks(
        self,
        num_tasks: int,
        distribution: str = "uniform",
        arrival_pattern: str = "batch",
        seed: Optional[int] = None,
    ) -> List[Task]:
        """Generate a synthetic list of tasks.

        Args:
            num_tasks: Number of tasks to generate (e.g., 50, 100, 500, 1000).
            distribution: 'uniform', 'normal', 'exponential', or 'mixed'.
            arrival_pattern: 'batch' (arrival_time=0) or 'poisson' (dynamic arrivals).
            seed: Optional seed override.

        Returns:
            List of Task instances.
        """
        # TODO (Team Member 1): Implement task generation with realistic cloud parameters:
        # - CPU: 1 to 8 vCPU cores
        # - RAM: 1 to 32 GB
        # - Workload: 1,000 to 100,000 MI
        # - Priority: 1 (low) to 5 (high)
        # - Deadlines: arrival_time + factor * (workload_mi / avg_mips)
        raise NotImplementedError("TODO: Implement WorkloadGenerator.generate_tasks()")

    def generate_vms(
        self,
        num_vms: int,
        profile: str = "heterogeneous",
        seed: Optional[int] = None,
    ) -> List[VirtualMachine]:
        """Generate heterogeneous virtual machines (e.g., standard, compute-optimized, memory-optimized).

        Args:
            num_vms: Number of VMs to generate (e.g., 5, 10, 20, 50).
            profile: 'heterogeneous', 'compute_heavy', 'memory_heavy', or 'homogeneous'.

        Returns:
            List of VirtualMachine instances.
        """
        # TODO (Team Member 1): Implement VM generation:
        # Define 4-5 realistic VM tiers (e.g. Small: 2 cores, 4GB, 1000 MIPS, $0.05/hr;
        # Large: 8 cores, 32GB, 4000 MIPS, $0.20/hr, etc.)
        raise NotImplementedError("TODO: Implement WorkloadGenerator.generate_vms()")

    def create_environment(
        self,
        num_tasks: int = 100,
        num_vms: int = 10,
        distribution: str = "mixed",
    ) -> CloudEnvironment:
        """Create a complete CloudEnvironment."""
        # TODO (Team Member 1): Call generate_tasks and generate_vms and return CloudEnvironment
        raise NotImplementedError("TODO: Implement WorkloadGenerator.create_environment()")
