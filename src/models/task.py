"""Cloud workload Task model.

Assigned to: Team Member 1 (Cloud Environment & Modeling)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


VALID_TASK_CATEGORIES = frozenset(
    {
        "cpu_intensive",
        "memory_intensive",
        "balanced",
        "io_batch",
        "latency_sensitive",
    }
)


@dataclass(frozen=True)
class Task:
    """Represents an independent cloud computing task to be scheduled onto a VM.

    Attributes:
        task_id: Unique string identifier for the task.
        cpu_req: CPU demand in vCPU cores or normalized CPU units (> 0).
        ram_req: Memory demand in GB (> 0).
        workload_mi: Computational length in Million Instructions (> 0).
        priority: Scheduling priority (integer >= 1; higher means higher priority).
        arrival_time: Arrival timestamp in seconds (>= 0.0; 0.0 for static batch).
        deadline: Optional absolute completion deadline in seconds (>= arrival_time).
        category: Workload classification tag.
    """

    task_id: str
    cpu_req: float
    ram_req: float
    workload_mi: float
    priority: int = 1
    arrival_time: float = 0.0
    deadline: Optional[float] = None
    category: str = "balanced"

    def __post_init__(self) -> None:
        """Validate task fields.
        
        # TODO (Team Member 1): Implement input validation:
        # - task_id must be non-empty string.
        # - cpu_req, ram_req, workload_mi must be > 0.
        # - priority must be >= 1.
        # - arrival_time must be >= 0.
        # - deadline (if set) must be >= arrival_time.
        # - category must be a valid category from VALID_TASK_CATEGORIES.
        """
        # TODO: Implement validation
        pass

    def to_dict(self) -> Dict[str, Any]:
        """Serialize Task to a dictionary."""
        # TODO (Team Member 1): Implement serialization
        raise NotImplementedError("TODO: Implement Task.to_dict()")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        """Reconstruct a Task from a dictionary."""
        # TODO (Team Member 1): Implement deserialization
        raise NotImplementedError("TODO: Implement Task.from_dict()")
