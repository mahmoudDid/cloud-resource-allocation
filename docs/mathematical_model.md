# Mathematical Optimization Model

**Project:** Cloud Resource Allocation Using Genetic Algorithm (GA) and Memetic Algorithm (MA)

---

## 1. Sets, Indices, and Parameters

- Set of independent tasks: $\mathcal{T} = \{1, 2, \dots, N\}$.
  Each task $i \in \mathcal{T}$ has:
  - CPU demand $c_i > 0$,
  - RAM demand $r_i > 0$ (GB),
  - Computational workload $W_i > 0$ (Million Instructions, MI),
  - Priority $p^{\text{prio}}_i \in \mathbb{Z}_{\ge 1}$,
  - Arrival time $a_i \ge 0$ (seconds; $a_i = 0$ in static batch mode),
  - Optional deadline $d_i \ge a_i$ (seconds).
- Set of virtual machines: $\mathcal{V} = \{1, 2, \dots, M\}$, with online subset $\mathcal{V}_{\text{avail}} = \{j \in \mathcal{V} : \text{avail}_j = \text{True}\}$ of cardinality $M_{\text{avail}} = |\mathcal{V}_{\text{avail}}|$.
  Each VM $j \in \mathcal{V}$ has:
  - CPU capacity $C_j^{\text{cpu}} > 0$,
  - RAM capacity $C_j^{\text{ram}} > 0$ (GB),
  - Processing rate $\text{MIPS}_j > 0$ (MI/s),
  - Active billing rate $p_j \ge 0$ (\$/s),
  - Power envelope $(P_j^{\text{idle}}, P_j^{\text{max}})$ (Watts).

---

## 2. Decision Variables and Chromosome Encoding

Binary assignment matrix $x_{ij} \in \{0, 1\}$ for $i \in \mathcal{T}, j \in \mathcal{V}$:

$$x_{ij} = \begin{cases} 1, & \text{if task } i \text{ is assigned to VM } j \\ 0, & \text{otherwise.} \end{cases}$$

In the evolutionary representation, each chromosome is an integer vector $\mathbf{g} = [g_1, g_2, \dots, g_N] \in \{0, \dots, M-1\}^N$ where $g_i = j \iff x_{ij} = 1$. This encoding enforces assignment completeness ($\sum_{j=1}^M x_{ij} = 1$) structurally.

---

## 3. Hard Feasibility Constraints

1. **Assignment Completeness & Integrality:**
   $$\sum_{j=1}^{M} x_{ij} = 1, \quad x_{ij} \in \{0, 1\}, \quad \forall i \in \mathcal{T}$$
2. **Resource Availability Constraint:**
   $$x_{ij} \le \mathbb{I}(\text{avail}_j = \text{True}), \quad \forall i \in \mathcal{T}, j \in \mathcal{V}$$
3. **Single-Task Hardware Compatibility:**
   $$c_i x_{ij} \le C_j^{\text{cpu}}, \quad r_i x_{ij} \le C_j^{\text{ram}}, \quad \forall i \in \mathcal{T}, j \in \mathcal{V}$$
4. **Aggregate VM Capacity Constraints (Static Batch / Cumulative Mode):**
   $$\sum_{i=1}^{N} c_i x_{ij} \le C_j^{\text{cpu}}, \quad \sum_{i=1}^{N} r_i x_{ij} \le C_j^{\text{ram}}, \quad \forall j \in \mathcal{V}$$
   *(In dynamic time-extended sequential mode `per_task_sequential`, tasks execute one-at-a-time on a VM and must satisfy single-task hardware compatibility at execution time rather than simultaneous batch summation.)*

---

## 4. Sequential Execution & Scheduling Metrics

Let $\mathcal{T}_j = (i_1, i_2, \dots, i_{k_j})$ be the tasks assigned to VM $j$, ordered deterministically by $(a_i \uparrow,\ p^{\text{prio}}_i \downarrow,\ i \uparrow)$. Execution on each VM is **explicitly non-preemptive and sequential** (no unmodeled parallelism is claimed within a single VM).

1. **Execution Time:**
   $$E_{ij} = \frac{W_i}{\text{MIPS}_j} \quad \text{(seconds)}$$

2. **Start Time & Completion Time:**
   $$S_{i_m} = \max\big(a_{i_m},\ F_{i_{m-1}}\big), \quad F_{i_m} = S_{i_m} + E_{i_m, j} \quad (F_{i_0} = 0)$$

3. **Makespan:**
   $$C_{\max} = \max_{i \in \mathcal{T}} F_i = \max_{j \in \mathcal{V}_{\text{avail}}} \text{FinishTime}_j$$

4. **Total Monetary Cost (On-Demand Active Execution):**
   $$\text{TotalCost} = \sum_{j \in \mathcal{V}_{\text{avail}}} p_j \cdot \text{BusyTime}_j, \quad \text{where } \text{BusyTime}_j = \sum_{i \in \mathcal{T}_j} E_{ij}$$

5. **Average Response Time:**
   $$\overline{R} = \frac{1}{N} \sum_{i=1}^{N} (F_i - a_i)$$

6. **Temporal Resource Utilization:**
   $$U_{\text{res}} = \frac{1}{M_{\text{avail}}} \sum_{j \in \mathcal{V}_{\text{avail}}} u_j^{\text{time}}, \quad u_j^{\text{time}} = \frac{\text{BusyTime}_j}{C_{\max}}$$

7. **CPU Utilization:**
   - Cluster Allocated CPU Utilization: $U_{\text{cpu}} = \frac{\sum_{i=1}^{N} c_i}{\sum_{j \in \mathcal{V}_{\text{avail}}} C_j^{\text{cpu}}}$
   - Time-Weighted Execution CPU Utilization: $U_{\text{cpu}}^{\text{tw}} = \frac{\sum_{i=1}^{N} c_i E_{i, g_i}}{C_{\max} \sum_{j \in \mathcal{V}_{\text{avail}}} C_j^{\text{cpu}}}$

8. **RAM Utilization:**
   - Cluster Allocated RAM Utilization: $U_{\text{ram}} = \frac{\sum_{i=1}^{N} r_i}{\sum_{j \in \mathcal{V}_{\text{avail}}} C_j^{\text{ram}}}$
   - Time-Weighted Execution RAM Utilization: $U_{\text{ram}}^{\text{tw}} = \frac{\sum_{i=1}^{N} r_i E_{i, g_i}}{C_{\max} \sum_{j \in \mathcal{V}_{\text{avail}}} C_j^{\text{ram}}}$

9. **Load Balancing & Load Imbalance:**
   Let $l_j = \frac{1}{3}(u_j^{\text{time}} + u_j^{\text{cpu}} + u_j^{\text{ram}})$ in cumulative mode (or $u_j^{\text{time}}$ in sequential mode), where $u_j^{\text{cpu}} = \frac{\sum_{i \in \mathcal{T}_j} c_i}{C_j^{\text{cpu}}}$ and $u_j^{\text{ram}} = \frac{\sum_{i \in \mathcal{T}_j} r_i}{C_j^{\text{ram}}}$. Using Jain's Fairness Index:
   $$J = \frac{\left(\sum_{j \in \mathcal{V}_{\text{avail}}} l_j\right)^2}{M_{\text{avail}} \sum_{j \in \mathcal{V}_{\text{avail}}} l_j^2} \in \left[\frac{1}{M_{\text{avail}}}, 1\right], \qquad \text{LoadImbalance} = 1 - J \in [0, 1)$$
   Additionally, Degree of Imbalance is tracked as $DI = (\max_j \text{BusyTime}_j - \min_j \text{BusyTime}_j) / \overline{\text{BusyTime}}$.

10. **SLA Violation Rate:**
    Let $\mathcal{D} = \{i \in \mathcal{T} : d_i \text{ is defined}\}$.
    $$\text{SLAViolationRate} = \begin{cases} \frac{1}{|\mathcal{D}|} \sum_{i \in \mathcal{D}} \mathbb{I}(F_i > d_i), & |\mathcal{D}| > 0 \\ 0, & |\mathcal{D}| = 0 \end{cases}$$

---

## 5. Multi-Objective Normalization & Weight Profiles

To avoid scale distortion across seconds, dollars, and ratios while preserving strict comparability across algorithms on a given problem instance, `ObjectiveNormalizer` computes **instance-anchored lower and upper reference bounds** solely from task demands and VM capacities:

- $\hat{C}_{\max} = \max\left(0,\ \frac{C_{\max} - C_{\max}^{\min}}{C_{\max}^{\text{ref}} - C_{\max}^{\min}}\right)$, where $C_{\max}^{\min} = \max\left(\frac{\sum W_i}{\sum \text{MIPS}_j},\ \max_i (a_i + \frac{W_i}{\max_j \text{MIPS}_j})\right)$ and $C_{\max}^{\text{ref}} = \max_i a_i + 2.5 \cdot \frac{\sum W_i}{\sum \text{MIPS}_j}$.
- $\widehat{\text{Cost}} = \max\left(0,\ \frac{\text{TotalCost} - \text{Cost}_{\min}}{\text{Cost}_{\text{ref}} - \text{Cost}_{\min}}\right)$, using task-wise minimum and maximum cost-per-MI rates across compatible VMs.
- $\widehat{R} = \max\left(0,\ \frac{\overline{R} - R_{\min}}{R_{\text{ref}} - R_{\min}}\right)$, anchored to an idealized fastest-cluster SJF flow lower bound and $2.5\times$ balanced-cluster flow reference.
- $\widehat{\text{Imbalance}} = 1 - J \in [0, 1)$, and $\widehat{\text{SLA}} = \text{SLAViolationRate} \in [0, 1]$.

The scalarized fitness function minimized by GA, MA, and evaluated on baselines is:

$$\text{Fitness}(x) = \begin{cases}
w_1 \hat{C}_{\max} + w_2 \widehat{\text{Cost}} + w_3 \widehat{R} + w_4 \widehat{\text{Imbalance}} + w_5 \widehat{\text{SLA}}, & \text{if feasible} \\
P_0 + P_s \cdot \text{Violation}(x) + \text{WeightedSum}(x), & \text{if infeasible}
\end{cases}$$

with $P_0 = 1000.0,\ P_s = 500.0$ ensuring Deb-style feasibility dominance.

### Configured Weight Profiles

| Profile | $w_1$ (Makespan) | $w_2$ (Cost) | $w_3$ (Resp. Time) | $w_4$ (Imbalance) | $w_5$ (SLA) | Rationale |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Balanced** | 0.25 | 0.20 | 0.20 | 0.15 | 0.20 | Jointly minimizes latency, budget, SLA breaches, and VM hotspot skew |
| **Performance** | 0.35 | 0.05 | 0.30 | 0.10 | 0.20 | Prioritizes fast makespan, low response latency, and deadline adherence |
| **Cost** | 0.10 | 0.55 | 0.10 | 0.10 | 0.15 | Favors cost-efficient low-MIPS VMs while bounding SLA/overload risk |

For true Pareto optimization without scalar weights, `NSGA2Scheduler` directly optimizes the unscalarized vector $(C_{\max},\ \text{TotalCost},\ \overline{R})$.
