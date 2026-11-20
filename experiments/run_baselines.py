"""Baseline algorithms comparison experiment.

Usage:
    python experiments/run_baselines.py
"""

from __future__ import annotations

from src.utils.logging_utils import setup_logger


def run() -> None:
    logger = setup_logger("BaselinesExperiment")
    logger.info("Evaluating baseline schedulers (FCFS, RoundRobin, Min-Min, Random)...")
    # TODO (Team Member 2):
    # Run baseline algorithms across standard workloads and save comparison metrics.
    print("[TODO] Implement baseline comparison.")


if __name__ == "__main__":
    run()
