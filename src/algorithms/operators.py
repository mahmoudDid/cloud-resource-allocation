"""Genetic & Evolutionary Algorithm operators.

Assigned to: Team Member 3 (Genetic Algorithm Specialist)
"""

from __future__ import annotations

from typing import List, Tuple
import numpy as np

from src.models.cloud_environment import CloudEnvironment


def tournament_selection(
    population: List[List[int]],
    fitness_values: np.ndarray,
    tournament_size: int,
    rng: np.random.Generator,
) -> int:
    """Tournament Selection operator (Minimization problem: lower fitness wins).

    Returns:
        Index of the selected winner individual in population.
    """
    # TODO (Team Member 3): Implement tournament selection:
    # 1. Randomly choose tournament_size indices from len(population).
    # 2. Return the index with the minimum fitness value.
    raise NotImplementedError("TODO: Implement tournament_selection()")


def roulette_wheel_selection(
    population: List[List[int]],
    fitness_values: np.ndarray,
    rng: np.random.Generator,
) -> int:
    """Fitness-Proportionate (Roulette Wheel) Selection.
    
    For minimization, invert or transform fitnesses (e.g. 1 / (fitness + epsilon)).
    """
    # TODO (Team Member 3): Implement roulette wheel selection.
    raise NotImplementedError("TODO: Implement roulette_wheel_selection()")


def single_point_crossover(
    parent1: List[int],
    parent2: List[int],
    rng: np.random.Generator,
) -> Tuple[List[int], List[int]]:
    """Single-Point Crossover."""
    # TODO (Team Member 3): Implement single-point crossover:
    # Pick a random cut point 1 <= cut < N, swap segments.
    raise NotImplementedError("TODO: Implement single_point_crossover()")


def uniform_crossover(
    parent1: List[int],
    parent2: List[int],
    rng: np.random.Generator,
    swap_prob: float = 0.5,
) -> Tuple[List[int], List[int]]:
    """Uniform Crossover: each gene is swapped with probability swap_prob."""
    # TODO (Team Member 3): Implement uniform crossover.
    raise NotImplementedError("TODO: Implement uniform_crossover()")


def random_reset_mutation(
    chromosome: List[int],
    num_vms: int,
    mutation_rate: float,
    rng: np.random.Generator,
) -> List[int]:
    """Random Reset Mutation: randomly change gene to another VM with probability mutation_rate."""
    # TODO (Team Member 3): Implement random reset mutation.
    raise NotImplementedError("TODO: Implement random_reset_mutation()")


def feasibility_aware_mutation(
    chromosome: List[int],
    env: CloudEnvironment,
    mutation_rate: float,
    rng: np.random.Generator,
) -> List[int]:
    """Feasibility-aware mutation: reassigns gene only to VMs that satisfy the task's capacity requirements."""
    # TODO (Team Member 3): Implement feasibility-aware mutation.
    raise NotImplementedError("TODO: Implement feasibility_aware_mutation()")


def compute_population_diversity(population: List[List[int]]) -> float:
    """Compute average pairwise Hamming distance across population chromosomes."""
    # TODO (Team Member 3): Implement diversity calculation.
    raise NotImplementedError("TODO: Implement compute_population_diversity()")
