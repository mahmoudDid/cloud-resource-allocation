"""Ablation study: GA vs MA and local search operator comparison.

Usage:
    python experiments/run_ablation.py
"""

from __future__ import annotations

from src.utils.logging_utils import setup_logger


def run() -> None:
    logger = setup_logger("AblationStudy")
    logger.info("Running ablation study: GA vs MA and operator impact...")
    # TODO (Team Member 4):
    # Compare First Improvement vs Best Improvement, and different local search probabilities.
    print("[TODO] Implement ablation study.")


if __name__ == "__main__":
    run()
