"""Cloud Environment container model.

Assigned to: Team Member 1 (Cloud Environment & Modeling)
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional
from src.models.task import Task
from src.models.virtual_machine import VirtualMachine


class CloudEnvironment:
    """Encapsulates the state and catalog of Tasks and VirtualMachines."""

    def __init__(
        self,
        tasks: Optional[List[Task]] = None,
        vms: Optional[List[VirtualMachine]] = None,
    ) -> None:
        """Initialize the cloud environment with tasks and VMs.
        
        # TODO (Team Member 1): Store tasks and VMs lists, index them by ID for fast lookup.
        """
        self.tasks: List[Task] = tasks or []
        self.vms: List[VirtualMachine] = vms or []
        # TODO: Implement indexing and initialization

    @property
    def num_tasks(self) -> int:
        """Number of tasks in the environment."""
        return len(self.tasks)

    @property
    def num_vms(self) -> int:
        """Number of VMs in the environment."""
        return len(self.vms)

    def add_task(self, task: Task) -> None:
        """Add a task to the environment."""
        # TODO (Team Member 1): Implement add_task
        raise NotImplementedError("TODO: Implement CloudEnvironment.add_task()")

    def add_vm(self, vm: VirtualMachine) -> None:
        """Add a VM to the environment."""
        # TODO (Team Member 1): Implement add_vm
        raise NotImplementedError("TODO: Implement CloudEnvironment.add_vm()")

    def get_task(self, task_id: str) -> Optional[Task]:
        """Retrieve task by ID."""
        # TODO (Team Member 1): Implement get_task
        raise NotImplementedError("TODO: Implement CloudEnvironment.get_task()")

    def get_vm(self, vm_id: str) -> Optional[VirtualMachine]:
        """Retrieve VM by ID."""
        # TODO (Team Member 1): Implement get_vm
        raise NotImplementedError("TODO: Implement CloudEnvironment.get_vm()")

    def validate(self) -> bool:
        """Validate environment consistency and feasibility.
        
        Check that:
        1. num_tasks > 0 and num_vms > 0.
        2. Every task can fit into at least one VM (cpu_req <= vm.cpu_capacity and ram_req <= vm.ram_capacity).
        """
        # TODO (Team Member 1): Implement validation
        raise NotImplementedError("TODO: Implement CloudEnvironment.validate()")
