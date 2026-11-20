"""Deterministic simulation execution engine.

Assigned to: Team Member 1 & Team Member 2
"""

from __future__ import annotations

from typing import Any, Dict, List
import numpy as np

from src.models.cloud_environment import CloudEnvironment


class ExecutionEngine:
    """Calculates task execution times, VM active periods, and makespan deterministically.

    Execution time formula:
        ExecutionTime(task_i, vm_j) = task_i.workload_mi / vm_j.mips
    """

    def __init__(self, env: CloudEnvironment) -> None:
        self.env = env

    def simulate(self, chromosome: List[int]) -> Dict[str, Any]:
        """Simulate task execution according to the given chromosome allocation vector.

        Args:
            chromosome: List of length N where chromosome[i] is the VM index (0..M-1) assigned to task i.

        Returns:
            Dictionary containing:
                - vm_task_lists: Mapping from VM index to list of assigned task indices.
                - task_execution_times: List of float execution times for each task.
                - task_start_times: List of float start times for each task.
                - task_finish_times: List of float finish times for each task.
                - vm_completion_times: List of float completion times for each VM.
                - makespan: Maximum completion time across all VMs: max(vm_completion_times).
                - vm_total_busy_time: Total processing time for each VM.
        """
        # TODO (Team Member 1 / 2): Implement sequential / queued task scheduling on each VM.
        # 1. Group tasks assigned to each VM.
        # 2. Sort tasks on each VM by arrival_time (and priority if applicable).
        # 3. For each task:
        #      exec_time = task.workload_mi / vm.mips
        #      start_time = max(vm_available_time, task.arrival_time)
        #      finish_time = start_time + exec_time
        #      vm_available_time = finish_time
        # 4. Compute makespan = max(finish_time across all tasks).
        raise NotImplementedError("TODO: Implement ExecutionEngine.simulate()")
