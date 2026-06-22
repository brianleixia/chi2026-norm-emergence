# Literature Review — 2026-06-22
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 1

## 1. Hierarchical Heuristic Learning towards Effcient Norm Emergence
- Authors: Tianpei Yang, Jianye Hao, Zhaopeng Meng | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
Based on the single paper provided, a multi-paper synthesis isn't possible, but here's a synthesis of the paper's internal contributions and the open questions it raises:

**1. Internal contributions and consensus within the paper**

The paper addresses the problem of efficient norm emergence in multi-agent systems, where agents must coordinate their behaviors through shared social conventions without centralized control. It agrees with the broader field that norm emergence is a critical mechanism for multi-agent coordination and that naive learning approaches (e.g., flat Q-learning or simple reinforcement over action choices) scale poorly as the number of possible behaviors grows. The authors propose a hierarchical heuristic learning framework that decomposes the norm-learning problem into structured sub-problems, allowing agents to learn conventions more efficiently by abstracting behavior into higher-level decision layers. The empirical results suggest this hierarchy accelerates convergence to shared norms compared to baseline approaches, and the paper positions efficiency—both in learning speed and scalability—as a central design goal for norm emergence research.

**2. Tensions and open issues within the framework**

While the paper demonstrates benefits over flat-learning baselines, it does not thoroughly explore how the proposed hierarchy interacts with environmental complexity, partial observability, or heterogeneous agent populations. The heuristic structure that accelerates learning in tested scenarios may itself become a bottleneck or require hand-engineering when the underlying action space does not naturally decompose along the assumed hierarchy. There is also an implicit tension between the efficiency gains reported and the generalizability of the approach: faster convergence in a specific experimental setup does not necessarily translate to robustness when agents have conflicting incentives, when norms must evolve over time, or when the population is non-stationary. The paper's evaluation does not fully settle whether hierarchical decomposition is the right inductive bias in general, or merely convenient for the chosen domains.

**3. Most urgent open question**

The most pressing open question raised by this work is: **how can norm emergence mechanisms be designed to be both efficient and adaptive across diverse multi-agent environments without relying on domain-specific hierarchical structure?** In other words,
