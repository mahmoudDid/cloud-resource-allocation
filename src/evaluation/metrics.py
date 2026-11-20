"""Performance evaluation metrics for cloud resource allocation.

Assigned to: Team Member 2 (Metrics & Baselines Specialist)
"""

from __future__ import annotations

from typing import Any, Dict, List
import numpy as np

from src.models.cloud_environment import CloudEnvironment


class MetricsCalculator:
    """Calculates all standard cloud scheduling evaluation metrics:
    
    1. Makespan: max(T_finish_i for all i)
    2. Total Cost: sum(busy_time_j * cost_per_second_j for all VMs)
    3. Average Response Time: mean(T_finish_i - arrival_time_i for all tasks)
    4. CPU Utilization: mean(cpu_demand_j / cpu_capacity_j)
    5. RAM Utilization: mean(ram_demand_j / ram_capacity_j)
    6. Load Imbalance Degree: (T_max - T_min) / T_avg
    7. SLA Violation Rate: fraction of tasks completing after their deadline
    """

    def __init__(self, env: CloudEnvironment) -> None:
        self.env = env

    def calculate_makespan(self, task_finish_times: List[float]) -> float:
        """Compute makespan: the total completion time of the entire task batch."""
        # TODO (Team Member 2): Return max(task_finish_times)
        raise NotImplementedError("TODO: Implement calculate_makespan")

    def calculate_total_cost(self, vm_busy_times: List[float]) -> float:
        """Compute total monetary cost incurred across all VMs."""
        # TODO (Team Member 2): Compute sum(busy_times[j] * vm[j].cost_per_second)
        raise NotImplementedError("TODO: Implement calculate_total_cost")

    def calculate_avg_response_time(
        self,
        task_finish_times: List[float],
        task_arrival_times: List[float],
    ) -> float:
        """Compute average turnaround / response time per task."""
        # TODO (Team Member 2): Compute mean(finish - arrival)
        raise NotImplementedError("TODO: Implement calculate_avg_response_time")

    def calculate_sla_violation_rate(
        self,
        task_finish_times: List[float],
        task_deadlines: List[Optional[float]],
    ) -> float:
        """Compute percentage of tasks that missed their SLA deadline."""
        # TODO (Team Member 2): Compute violations / total_tasks_with_deadlines
        raise NotImplementedError("TODO: Implement calculate_sla_violation_rate")

    def calculate_all_metrics(
        self,
        chromosome: List[int],
        sim_results: Dict[str, Any],
    ) -> Dict[str, float]:
        """Compute full dictionary of metrics for the given schedule."""
        # TODO (Team Member 2): Combine all metric calculations into a structured dict.
        raise NotImplementedError("TODO: Implement calculate_all_metrics")
