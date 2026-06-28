# Literature Review — 2026-06-28
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 1

## 1. Hierarchical Heuristic Learning towards Effcient Norm Emergence
- Authors: Tianpei Yang, Jianye Hao, Zhaopeng Meng | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - [Could not extract]

## Synthesis
# Research Synthesis: Hierarchical Heuristic Learning for Norm Emergence

**1. Points of Agreement**

The paper operates on a shared foundational premise within multi-agent systems research: social norms are essential mechanisms for regulating agent behavior and enabling coordination, particularly as agents must increasingly operate in open, heterogeneous environments where no central authority dictates rules. The work implicitly agrees with the broader literature that norm emergence—the process by which norms spontaneously arise from local agent interactions rather than top-down imposition—is a critical and challenging problem. Furthermore, the hierarchical decomposition of decision-making (separating strategy from action selection) reflects a consensus that complex agent behaviors benefit from modular, layered architectures rather than monolithic policies, especially when balancing multiple objectives like norm compliance and task performance.

**2. Points of Disagreement**

The text is truncated, so direct disagreements with other works cannot be fully assessed. However, the paper's emphasis on **hierarchical heuristic learning** implicitly positions itself against alternative approaches in the norm emergence literature—namely, pure reinforcement learning methods, evolutionary game-theoretic models, and social learning-based frameworks. While those approaches typically rely on agents learning norms through repeated interaction, payoff signaling, or imitation, this work argues that such flat learning structures are inefficient in complex environments. The disagreement is methodological: the authors contend that explicit hierarchical decomposition outperforms end-to-end learning for norm emergence, contrasting with work that treats norm adoption as an emergent property of homogeneous learning dynamics.

**3. Most Urgent Open Question**

The most pressing unresolved question is: **How can we scale hierarchical heuristic learning for norm emergence to large, open multi-agent systems with heterogeneous agents, dynamic populations, and conflicting or evolving norms?** The paper hints at efficiency gains through hierarchical decomposition, but critical questions remain about convergence guarantees when agents have divergent values, how norms adapt when environments or agent populations shift over time, and whether learned hierarchical heuristics can generalize across contexts or overfit to specific interaction patterns. Addressing these questions is essential before norm emergence mechanisms can be reliably deployed in real-world systems
