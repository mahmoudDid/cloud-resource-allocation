"""Publication-quality plots using Matplotlib and Seaborn.

Assigned to: Team Member 5 (Visualization & Reporting Specialist)
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


class Visualizer:
    """Generates all academic comparison plots and saves them to results/figures/."""

    def __init__(self, output_dir: str = "results/figures") -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        sns.set_theme(style="whitegrid", font_scale=1.1)

    def plot_convergence(
        self,
        history_dict: Dict[str, List[float]],
        title: str = "Convergence History (Fitness vs Generation)",
        filename: str = "fig_09_convergence_comparison.png",
    ) -> str:
        """Plot convergence curves comparing GA and MA across generations."""
        # TODO (Team Member 5): Implement convergence plot.
        raise NotImplementedError("TODO: Implement Visualizer.plot_convergence")

    def plot_makespan_comparison(
        self,
        data: Dict[str, List[float]],
        filename: str = "fig_01_makespan_comparison.png",
    ) -> str:
        """Plot makespan comparison bar chart or box plot across algorithms."""
        # TODO (Team Member 5): Implement makespan comparison plot.
        raise NotImplementedError("TODO: Implement Visualizer.plot_makespan_comparison")

    def plot_cost_comparison(
        self,
        data: Dict[str, List[float]],
        filename: str = "fig_02_cost_comparison.png",
    ) -> str:
        """Plot monetary cost comparison across algorithms."""
        # TODO (Team Member 5): Implement cost comparison plot.
        raise NotImplementedError("TODO: Implement Visualizer.plot_cost_comparison")

    def plot_utilization_breakdown(
        self,
        cpu_utils: Dict[str, float],
        ram_utils: Dict[str, float],
        filename: str = "fig_04_resource_utilization.png",
    ) -> str:
        """Plot CPU vs RAM utilization comparison."""
        # TODO (Team Member 5): Implement utilization plot.
        raise NotImplementedError("TODO: Implement Visualizer.plot_utilization_breakdown")
