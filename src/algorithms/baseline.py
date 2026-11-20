"""Baseline scheduling algorithms for cloud task allocation.

Assigned to: Team Member 2 (Baselines Specialist)
"""

from __future__ import annotations

from typing import List, Optional
import numpy as np

from src.algorithms.base import BaseScheduler
from src.models.cloud_environment import CloudEnvironment
from src.simulation.scheduler import SchedulingOutcome, simulate_schedule


class FCFSScheduler(BaseScheduler):
    """First-Come, First-Served (FCFS) scheduler.
    
    Assigns tasks in order of arrival to the first available VM that can host them.
    """

    name = "FCFS"

    def schedule(self, env: CloudEnvironment, rng_seed: Optional[int] = 42) -> SchedulingOutcome:
        # TODO (Team Member 2): Implement FCFS scheduling logic:
        # 1. Sort tasks by arrival_time.
        # 2. Assign each task to the VM that finishes its current queue earliest (or round robin among feasible VMs).
        # 3. Return simulate_schedule(env, chromosome, scheduler_name="FCFS", runtime_seconds=elapsed).
        raise NotImplementedError("TODO: Implement FCFSScheduler.schedule()")


class RoundRobinScheduler(BaseScheduler):
    """Round Robin (RR) scheduler.
    
    Distributes tasks cyclically across available virtual machines.
    """

    name = "RoundRobin"

    def schedule(self, env: CloudEnvironment, rng_seed: Optional[int] = 42) -> SchedulingOutcome:
        # TODO (Team Member 2): Implement Round-Robin allocation:
        # chromosome[i] = i % num_vms (with feasibility check/fallback).
        raise NotImplementedError("TODO: Implement RoundRobinScheduler.schedule()")


class MinMinScheduler(BaseScheduler):
    """Min-Min heuristic scheduler.
    
    At each step, among all unscheduled tasks, finds the task with the minimum completion time across VMs,
    and assigns it to that VM.
    """

    name = "Min-Min"

    def schedule(self, env: CloudEnvironment, rng_seed: Optional[int] = 42) -> SchedulingOutcome:
        # TODO (Team Member 2): Implement Min-Min heuristic:
        # 1. Initialize ready tasks set and VM ready times.
        # 2. In each iteration, for each unscheduled task, compute completion time on each VM.
        # 3. Find task with global minimum completion time, assign to corresponding VM, update VM ready time.
        raise NotImplementedError("TODO: Implement MinMinScheduler.schedule()")


class RandomScheduler(BaseScheduler):
    """Random Feasible Allocation scheduler.
    
    Assigns each task to a randomly selected feasible VM.
    """

    name = "Random"

    def schedule(self, env: CloudEnvironment, rng_seed: Optional[int] = 42) -> SchedulingOutcome:
        # TODO (Team Member 2): Implement random feasible assignment.
        raise NotImplementedError("TODO: Implement RandomScheduler.schedule()")
