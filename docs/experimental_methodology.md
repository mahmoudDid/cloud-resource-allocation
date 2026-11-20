# Experimental Methodology

**Project:** Cloud Resource Allocation Using Genetic Algorithm (GA) and Memetic Algorithm (MA)

---

## 1. Fair Comparison Protocol

To guarantee scientific validity and eliminate confounding factors:
1. **Identical Problem Instances:** For any tuple `(distribution, num_tasks, num_vms, seed)`, a single `CloudEnvironment` is generated and passed unchanged to every baseline, GA, and MA solver.
2. **Isolated RNG Streams:** Each solver receives its own `np.random.Generator` initialized deterministically, preventing RNG state leakage between algorithms.
3. **Identical Objective Scale:** `ObjectiveNormalizer` anchors normalization bounds purely on problem-instance properties, ensuring fitness values are strictly comparable across algorithms.
4. **Equal Population & Generation Budgets:** GA and MA use identical population sizes and generation counts; MA's extra neighbor evaluations and wall-clock local search overhead are transparently measured and reported.

---

## 2. Experimental Suites

1. **Comparative Benchmark (`comparative_benchmark`):**
   - 20 independent random seeds (`100..119`),
   - 100 tasks, 10 heterogeneous VMs,
   - 4 workload distributions (`mixed`, `uniform`, `normal`, `exponential`),
   - 3 objective weight profiles (`balanced`, `performance`, `cost`).
2. **Scalability Matrix (`scalability_matrix`):**
   - 5 independent seeds across full $4 \times 4$ grid: $N \in \{50, 100, 500, 1000\}$ tasks $\times\ M \in \{5, 10, 20, 50\}$ VMs (total 16 cluster scales $\times$ 5 seeds $\times$ 6 algorithms = 480 runs).
   - Tracks fitness, makespan, cost, runtime, peak memory (KB), and feasibility rate.
3. **Robustness & Stress Testing (`robustness_scenarios`):**
   - 15 independent seeds across 6 stress regimes: `baseline_load` ($\rho=0.70$), `resource_scarcity` ($\rho=0.92$), `high_cpu_demand`, `high_ram_demand`, `vm_failure_degraded` (20% VMs offline), and `dynamic_arrivals` (Poisson arrivals under rolling-epoch execution), plus `impossible_overloaded` ($\rho=1.25$) to confirm zero silent constraint violations.
4. **Ablation Study (`ablation_study`):**
   - 15 seeds comparing `GA_NoElitism`, `GA_WithElitism`, `GA_Roulette_SinglePt`, `MA_NoLocalSearch`, `MA_FirstImprovement`, and `MA_BestImprovement`.
5. **Hyperparameter Sensitivity & True Pareto Analysis:**
   - 5-seed grid sweep over GA `(population_size, crossover_rate, mutation_rate)` and MA `(ls_strategy, ls_probability, ls_max_iterations)`.
   - NSGA-II Pareto front extraction vs. weighted-sum profiles and heuristic baselines.

---

## 3. Statistical Analysis Protocol

- **Descriptive Metrics:** Mean, median, sample standard deviation, minimum (best), maximum (worst), IQR, and 95% Student-$t$ confidence intervals across independent seeds.
- **Omnibus Multi-Algorithm Test:** Non-parametric **Friedman test** blocked by seed/instance ($\alpha = 0.05$), reporting $\chi^2$, $p$-value, and mean ranks.
- **Post-Hoc Pairwise Comparisons:** Paired two-sided **Wilcoxon signed-rank tests** with **Holm-Bonferroni** family-wise error correction, matched-pairs rank correlation $r$, and **Vargha-Delaney $\hat{A}_{12}$** stochastic superiority effect sizes.

---

## 4. Synthetic Workloads vs. Public Trace Import

Synthetic benchmarks use documented statistical generators (`WorkloadGenerator`) and are never labeled as real-world traces. In addition, `TraceDatasetLoader` provides verified preprocessing pipelines for Google Cluster Trace (`task_events`) and Alibaba Cluster Trace (`batch_task`) CSV formats, explicitly documenting host-capacity normalization assumptions (`reference_host_cpu=32`, `reference_host_ram_gb=128`, `reference_mips=6000`).
