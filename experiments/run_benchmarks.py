"""Standalone script to execute the multi-seed comparative benchmark."""

from __future__ import annotations

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluation.experiments import ExperimentRunner
from src.evaluation.statistics import (
    compute_descriptive_stats,
    run_friedman_test,
    run_pairwise_wilcoxon,
)
from src.utils.config_loader import EXPERIMENT_CONFIG_PATH, load_config, load_yaml_config
from src.utils.logging_utils import get_logger

logger = get_logger("run_benchmarks")


def execute_benchmarks(
    results_dir: Path | None = None,
    num_seeds: int | None = None,
) -> dict:
    """Run multi-seed comparative benchmark across distributions and weight profiles."""
    cfg = load_config()
    exp_cfg = load_yaml_config(EXPERIMENT_CONFIG_PATH)["comparative_benchmark"]
    runner = ExperimentRunner(cfg)

    seeds = int(num_seeds if num_seeds is not None else exp_cfg["num_seeds"])
    out_base = Path(results_dir or (PROJECT_ROOT / "results"))
    (out_base / "raw").mkdir(parents=True, exist_ok=True)
    (out_base / "processed").mkdir(parents=True, exist_ok=True)
    (out_base / "tables").mkdir(parents=True, exist_ok=True)

    logger.info(
        f"Running comparative benchmark: tasks={exp_cfg['task_count']}, "
        f"vms={exp_cfg['vm_count']}, seeds={seeds}"
    )
    comp_df, conv_df = runner.run_comparative_benchmark(
        num_tasks=int(exp_cfg["task_count"]),
        num_vms=int(exp_cfg["vm_count"]),
        distributions=exp_cfg["distributions"],
        weight_profiles=exp_cfg["weight_profiles"],
        num_seeds=seeds,
        base_seed=int(exp_cfg["base_seed"]),
    )

    comp_df.to_csv(out_base / "raw" / "comparative_raw.csv", index=False)
    conv_df.to_csv(out_base / "raw" / "comparative_convergence.csv", index=False)

    # Summary statistics table across all metrics for Balanced Mixed workload & all conditions
    summary_all = compute_descriptive_stats(
        comp_df, ["distribution", "weight_profile", "algorithm"], metric_col="fitness"
    )
    summary_all.to_csv(out_base / "tables" / "comparative_fitness_summary.csv", index=False)

    bal_mixed = comp_df[
        (comp_df["weight_profile"] == "balanced") & (comp_df["distribution"] == "mixed")
    ]
    metric_tables = []
    for met in (
        "fitness",
        "makespan",
        "total_cost",
        "avg_response_time",
        "resource_utilization",
        "time_weighted_cpu_utilization",
        "time_weighted_ram_utilization",
        "load_balance_jain",
        "sla_violation_rate",
        "runtime_sec",
    ):
        metric_tables.append(compute_descriptive_stats(bal_mixed, ["algorithm"], metric_col=met))
    import pandas as pd

    full_metrics_table = pd.concat(metric_tables, ignore_index=True)
    full_metrics_table.to_csv(out_base / "tables" / "balanced_mixed_metrics_summary.csv", index=False)

    friedman_res = run_friedman_test(bal_mixed, metric_col="fitness")
    wilcoxon_df = run_pairwise_wilcoxon(bal_mixed, reference_algo="MA", metric_col="fitness")
    wilcoxon_ga_df = run_pairwise_wilcoxon(bal_mixed, reference_algo="GA", metric_col="fitness")

    with (out_base / "processed" / "friedman_balanced_mixed.json").open("w", encoding="utf-8") as fh:
        json.dump(friedman_res, fh, indent=2)
    wilcoxon_df.to_csv(out_base / "tables" / "wilcoxon_ma_vs_peers.csv", index=False)
    wilcoxon_ga_df.to_csv(out_base / "tables" / "wilcoxon_ga_vs_peers.csv", index=False)

    # Weight profile trade-off summary
    profile_summary = (
        comp_df[comp_df["distribution"] == "mixed"]
        .groupby(["weight_profile", "algorithm"])[
            ["fitness", "makespan", "total_cost", "avg_response_time", "load_balance_jain", "sla_violation_rate"]
        ]
        .mean()
        .reset_index()
    )
    profile_summary.to_csv(out_base / "tables" / "weight_profile_tradeoffs.csv", index=False)

    logger.info("Comparative benchmark complete.")
    return {
        "comp_df": comp_df,
        "conv_df": conv_df,
        "friedman": friedman_res,
        "wilcoxon_ma": wilcoxon_df,
        "summary": full_metrics_table,
    }


if __name__ == "__main__":
    execute_benchmarks()
