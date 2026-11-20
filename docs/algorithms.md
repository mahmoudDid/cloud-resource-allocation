# Algorithms Specification

**Project:** Cloud Resource Allocation Using Genetic Algorithm (GA) and Memetic Algorithm (MA)

---

## 1. Baseline Scheduling Algorithms

1. **First-Come, First-Served (`FCFS`):** Processes tasks in ascending arrival order (tie-breaking by task index) and maps each task to the feasible online VM that becomes free earliest. *Limitation:* Greedy local clock choices ignore downstream workload length, heterogeneous cost-per-MI efficiency, and bin-packing fragmentation.
2. **Round Robin (`RoundRobin`):** Cycles sequentially across online VMs, picking the next VM satisfying CPU/RAM constraints. *Limitation:* Uniform cyclic rotation ignores VM MIPS heterogeneity, causing fast VMs to sit idle while slow VMs accumulate deep queues and high SLA violations.
3. **Min-Min (`Min-Min`, Braun et al., 2001):** At every step, computes minimum completion time $CT_{ij}$ across all unscheduled tasks and feasible VMs, dispatching $(i^*, j^*) = \arg\min CT_{ij}$. *Limitation:* Strongly minimizes makespan/execution of short tasks early, but leaves long/heavy tasks for last and overloads fast expensive VMs without accounting for monetary cost or fairness.
4. **Random Feasible (`RandomFeasible`):** Generates a valid random task-to-VM packing via randomized task permutation and stochastic feasible placement + repair. Serves as an unbiased feasible lower-bar benchmark.

---

## 2. Genetic Algorithm (`GeneticAlgorithmScheduler`)

Implemented strictly from scratch in `src/algorithms/genetic_algorithm.py` and `src/algorithms/operators.py`:

- **Encoding:** Integer vector $\mathbf{g} \in \{0,\dots,M-1\}^N$.
- **Feasible Initialization:** Constructs diverse feasible individuals using stochastic constructive packing and constraint repair.
- **Selection:**
  - *Tournament Selection:* $k$-way deterministic tournament ($k=3$ default).
  - *Roulette Wheel Selection:* Linearly inverted shifted fitness weights in $[0.05, 1.05]$ to avoid premature super-individual domination.
- **Crossover:**
  - *Uniform Crossover:* Independent per-gene swap with probability $0.5$.
  - *Single-Point Crossover:* Random slice exchange at cut index $c \in [1, N-1]$.
- **Mutation:**
  - *Feasibility-Aware Mutation:* Migrates mutated genes to VMs with remaining CPU/RAM headroom, falling back to feasibility-preserving 2-task swaps when capacity is tight.
  - *Random Reset Mutation:* Reassigns mutated genes to random compatible online VMs (repaired if infeasible).
- **Elitism & Diversity Guard:** Preserves top `elitism_count` chromosomes directly and monitors normalized population Hamming diversity; triggers temporary mutation boost and random feasible immigration if stagnation reaches `stagnation_limit`.

---

## 3. Memetic Algorithm (`MemeticAlgorithmScheduler`)

Genuine **Lamarckian Memetic Algorithm** combining the evolutionary loop with problem-specific neighborhood refinement (`src/optimization/local_search.py`):

- **Neighborhood Operators (all feasibility-preserving):**
  1. **Bottleneck Rebalance (`rebalance`):** Targets VMs with highest finish times and tests relocations onto lightly loaded feasible VMs.
  2. **Task Relocation (`relocate`):** Moves tasks across compatible feasible VMs.
  3. **Task Swap (`swap`):** Exchanges VM assignments of two tasks across distinct VMs while checking exact CPU/RAM capacity invariants in $O(1)$.
- **Local Search Strategies:**
  1. **First Improvement (`first_improvement`):** Iterates through shuffled candidate moves and immediately accepts the first strictly improving move, allowing deeper sequential descent steps per evaluation budget.
  2. **Best Improvement (`best_improvement`):** Evaluates a bounded neighborhood slice per iteration and commits the steepest-descent move.
- **Budgeting & Telemetry:** Controlled via `ls_strategy`, `ls_probability`, `ls_frequency`, `ls_selection_scope`, `ls_top_k`, `ls_max_iterations`, and `ls_max_evals`. Records exact local search calls, improvements, success rate, fitness deltas, and wall-clock overhead.

---

## 4. True Multi-Objective Optimizer (`NSGA2Scheduler`)

Implemented from scratch in `src/algorithms/nsga2.py` following Deb et al. (2002):
- Fast non-dominated sorting ($O(K \cdot P^2)$),
- Crowding distance diversity preservation,
- Constrained-dominance binary tournament selection,
- Simultaneous optimization of `(makespan, total_cost, avg_response_time)` returning the full non-dominated Pareto front alongside a Utopia-normalized knee-point solution.
