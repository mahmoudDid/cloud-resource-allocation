# External Public Cluster Trace Directory

Place preprocessed CSV extracts from public cloud cluster traces here if available:

- **Google Cluster Usage Trace (`task_events`)**: expected columns include `task_id`, `cpu_request`, `memory_request`, `duration_sec` (or `workload_mi`), `timestamp`, and `priority`.
- **Alibaba Cluster Trace (`batch_task`)**: expected columns include `task_name`, `plan_cpu`, `plan_mem`, `start_time`, and `end_time`.

Use `TraceDatasetLoader.load_google_cluster_csv(...)` or `TraceDatasetLoader.load_alibaba_cluster_csv(...)` in `src/simulation/dataset_loader.py` to convert these traces into `CloudEnvironment` instances.

> **Important Note:** All primary experimental results shipped in `results/` were produced using the documented synthetic `WorkloadGenerator` (`data/synthetic/`), not fabricated real-world traces.
