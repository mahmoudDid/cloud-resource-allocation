"""Main entry point for Cloud Resource Allocation using GA and MA.

Project for AI310 & CS361: Fall Semester 2026–2027.
Usage:
    python main.py --help
    python main.py --algorithm GA --tasks 100 --vms 10
    python main.py --algorithm MA --tasks 100 --vms 10
    python main.py --compare --tasks 100 --vms 10
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.utils.logging_utils import setup_logger


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Cloud Resource Allocation: Genetic Algorithm & Memetic Algorithm",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--algorithm",
        type=str,
        default="GA",
        choices=["GA", "MA", "FCFS", "RoundRobin", "Min-Min", "Random", "ALL"],
        help="Scheduling algorithm to execute.",
    )
    parser.add_argument("--tasks", type=int, default=100, help="Number of tasks.")
    parser.add_argument("--vms", type=int, default=10, help="Number of virtual machines.")
    parser.add_argument("--distribution", type=str, default="mixed", help="Workload distribution.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility.")
    parser.add_argument("--config", type=str, default="config/default_config.yaml", help="Path to config YAML.")
    return parser.parse_args()


def main() -> None:
    """Main CLI execution routine."""
    logger = setup_logger("CloudScheduler")
    args = parse_arguments()
    logger.info(f"Starting Cloud Resource Allocation (Algorithm: {args.algorithm}, Tasks: {args.tasks}, VMs: {args.vms})")

    # TODO (Team Integration):
    # 1. Load config from args.config using load_yaml_config.
    # 2. Instantiate WorkloadGenerator and create CloudEnvironment.
    # 3. Instantiate selected scheduler (GA, MA, FCFS, etc.).
    # 4. Execute scheduling: outcome = scheduler.schedule(env, rng_seed=args.seed).
    # 5. Print formatted summary table of outcome metrics.
    # 6. Save visualization plots if requested.
    print(f"\n[INFO] Project Skeleton Loaded Successfully.")
    print(f"Target Algorithm: {args.algorithm}")
    print(f"Tasks: {args.tasks}, VMs: {args.vms}, Seed: {args.seed}")
    print("\n[TODO] Team members: Implement your assigned modules in src/ and run tests with: pytest")


if __name__ == "__main__":
    main()
