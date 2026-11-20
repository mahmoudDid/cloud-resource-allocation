# Cloud Resource Allocation Using Genetic Algorithm (GA) and Memetic Algorithm (MA)

[![Course](https://img.shields.io/badge/Course-AI310%20%7C%20CS361-blue)](.)
[![Semester](https://img.shields.io/badge/Semester-Fall%202026--2027-success)](.)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue)](.)
[![Status](https://img.shields.io/badge/Repository-Team%20Starter%20Skeleton-orange)](.)

---

## 📌 Project Overview | نظرة عامة على المشروع

This repository serves as the **official team scaffolding and starter blueprint** for the course project:
**"Cloud Resource Allocation Using Genetic Algorithm (GA) and Memetic Algorithm (MA)"**.

The repository contains the complete modular architecture, type-annotated interfaces, data contracts, simulation models, configuration files, and evaluation harnesses. All operational methods contain structured `# TODO` docstrings ready for team members to implement their assigned sections.

---

## 👥 Team Workload Distribution | توزيع مهام الفريق

To ensure balanced contribution across team members, the architecture is divided into 5 specialized roles:

| Member / Role | Focus Area | Key Files & Modules to Implement |
| :--- | :--- | :--- |
| **Member 1: Modeling & Simulation** | Cloud Modeling & Data | `src/models/task.py`<br>`src/models/virtual_machine.py`<br>`src/models/cloud_environment.py`<br>`src/simulation/workload_generator.py`<br>`src/simulation/dataset_loader.py` |
| **Member 2: Baselines & Metrics** | Heuristics & Evaluation | `src/simulation/execution_engine.py`<br>`src/algorithms/baseline.py`<br>`src/evaluation/metrics.py`<br>`experiments/run_baselines.py` |
| **Member 3: Genetic Algorithm (GA)** | Metaheuristic Search | `src/optimization/constraints.py`<br>`src/optimization/fitness.py`<br>`src/algorithms/operators.py`<br>`src/algorithms/genetic_algorithm.py`<br>`src/algorithms/nsga2.py` |
| **Member 4: Memetic Algorithm (MA)** | Local Search & Hybrids | `src/optimization/local_search.py`<br>`src/algorithms/memetic_algorithm.py`<br>`experiments/run_ablation.py` |
| **Member 5: Experiments & Visuals** | Benchmarking & Visualization | `src/evaluation/statistics.py`<br>`src/evaluation/experiments.py`<br>`src/visualization/plots.py`<br>`src/visualization/dashboard.py`<br>`experiments/run_experiments.py`<br>`main.py` |

---

## 📁 Repository Directory Structure | هيكل المجلدات

```text
cloud-resource-allocation/
│
├── config/                          # Configuration files
│   ├── default_config.yaml          # Default GA/MA/Simulation hyper-parameters
│   └── experiment_config.yaml       # Multi-seed experimental matrix settings
│
├── docs/                            # Academic & Technical Documentation
│   ├── system_architecture.md       # Modular design and component interactions
│   ├── mathematical_model.md        # Formal optimization equations & constraints
│   ├── algorithms.md                # Operator designs (GA, MA, Local Search)
│   └── experimental_methodology.md  # Benchmarking protocols & statistical tests
│
├── data/                            # Datasets directory
│   ├── raw/                         # Public cloud traces (Google / Alibaba)
│   └── synthetic/                   # Generated synthetic workloads (.csv)
│
├── experiments/                     # Experiment execution scripts
│   ├── run_experiments.py          # Full benchmark suite across task/VM sizes
│   ├── run_baselines.py            # Baseline heuristics (FCFS, RR, Min-Min)
│   └── run_ablation.py             # GA vs MA ablation & local search operators
│
├── results/                         # Generated artifacts
│   ├── figures/                     # Publication plots (PNG/PDF)
│   ├── tables/                      # Result summary CSVs and LaTeX tables
│   ├── raw/                         # Raw per-seed experiment logs
│   └── processed/                   # Aggregated statistical data
│
├── src/                             # Core Python Source Code
│   ├── models/                      # Domain entities (Task, VM, Environment)
│   ├── simulation/                  # Execution engine, workload generators
│   ├── optimization/                # Fitness evaluator, constraints, local search
│   ├── algorithms/                  # Schedulers (Baselines, GA, MA, NSGA-II)
│   ├── evaluation/                  # Performance metrics and hypothesis tests
│   ├── visualization/               # Matplotlib & Seaborn academic visualizers
│   └── utils/                       # Config loaders, logging, random seeds
│
├── tests/                           # Pytest test suite (10 test modules)
├── notebooks/                       # Interactive exploration notebooks
├── main.py                          # CLI runner for quick runs & demos
├── requirements.txt                 # Python dependencies
├── pytest.ini                       # Pytest configuration
└── README.md                        # Project documentation (this file)
```

---

## 🚀 Getting Started | تعليمات البدء

### 1. Clone the Repository
```bash
git clone https://github.com/mahmoudDid/cloud-resource-allocation.git
cd cloud-resource-allocation
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Project Setup
Run the test runner to ensure discovery works:
```bash
pytest
```

---

## 🛠️ Development & Contribution Workflow

1. **Branching**: Each team member must work on their dedicated feature branch:
   ```bash
   git checkout -b feature/member1-models
   git checkout -b feature/member2-baselines
   git checkout -b feature/member3-ga
   git checkout -b feature/member4-ma-localsearch
   git checkout -b feature/member5-evaluation-plots
   ```
2. **Implementation**: Fill in the `# TODO` sections in your assigned files.
3. **Testing**: Write unit tests in `tests/` for your module and verify with `pytest`.
4. **Commit & Push**:
   ```bash
   git add .
   git commit -m "feat: implement genetic algorithm operators"
   git push origin feature/your-branch-name
   ```
5. **Pull Request**: Open a PR to merge into `main` after team review.

---

## 📚 References & Mathematical Formulation

Detailed mathematical formulations, fitness definitions, and algorithmic designs are documented in [`docs/`](docs/):
- [System Architecture](docs/system_architecture.md)
- [Mathematical Optimization Model](docs/mathematical_model.md)
- [Algorithms Specification](docs/algorithms.md)
- [Experimental Methodology](docs/experimental_methodology.md)
