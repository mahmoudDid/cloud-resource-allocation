"""Virtual Machine (VM) resource model.

Assigned to: Team Member 1 (Cloud Environment & Modeling)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class VirtualMachine:
    """Represents a virtual machine / computing node in the cloud datacenter.

    Attributes:
        vm_id: Unique identifier string for the VM.
        cpu_capacity: Total available vCPU cores (> 0).
        ram_capacity: Total available RAM in GB (> 0).
        mips: Processing speed in Million Instructions Per Second (> 0).
        cost_per_hour: Monetary cost of running this VM for one hour ($/hour, >= 0).
        power_idle_w: Static/idle power consumption in Watts (>= 0).
        power_max_w: Peak power consumption at 100% CPU utilization in Watts (>= power_idle_w).
        is_active: Availability flag.
    """

    vm_id: str
    cpu_capacity: float
    ram_capacity: float
    mips: float
    cost_per_hour: float
    power_idle_w: float = 100.0
    power_max_w: float = 250.0
    is_active: bool = True

    def __post_init__(self) -> None:
        """Validate VM fields.
        
        # TODO (Team Member 1): Implement validation:
        # - vm_id must be non-empty string.
        # - cpu_capacity, ram_capacity, mips must be > 0.
        # - cost_per_hour must be >= 0.
        # - power_idle_w >= 0 and power_max_w >= power_idle_w.
        """
        # TODO: Implement validation
        pass

    @property
    def cost_per_second(self) -> float:
        """Compute the running cost per second ($/s)."""
        # TODO (Team Member 1): Return cost_per_hour / 3600.0
        raise NotImplementedError("TODO: Implement VirtualMachine.cost_per_second")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize VM to a dictionary."""
        # TODO (Team Member 1): Implement serialization
        raise NotImplementedError("TODO: Implement VirtualMachine.to_dict()")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "VirtualMachine":
        """Reconstruct a VirtualMachine from a dictionary."""
        # TODO (Team Member 1): Implement deserialization
        raise NotImplementedError("TODO: Implement VirtualMachine.from_dict()")
