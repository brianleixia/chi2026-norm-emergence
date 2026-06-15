# Literature Review — 2026-06-15
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 1

## 1. Hierarchical Heuristic Learning towards Effcient Norm Emergence
- Authors: Tianpei Yang, Jianye Hao, Zhaopeng Meng | Year: 2026 | Venue: arXiv
- Novelty: ⭐⭐
- Claims:
  - Social norms serve as an important mechanism to regulate the behaviors of agents and to facilitate coordination among them in multiagent systems.
  - One important research question is how a norm can rapidly emerge through repeated local interaction within an agent society under different environments when their coordination space becomes large.
  - The authors propose a Hierarchical Heuristic Learning approach to address efficient norm emergence in multiagent systems.

## Synthesis
I notice that the paper content appears to be truncated — only the title and the beginning of the abstract are provided. I'll synthesize what I can from the available information, while being transparent about the limitation.

---

**1. What does the paper address?**

"Hierarchical Heuristic Learning towards Efficient Norm Emergence" focuses on the problem of how social norms — shared behavioral regularities that coordinate multi-agent systems — can emerge efficiently among autonomous agents. Rather than having norms imposed top-down, the paper investigates how agents can collectively develop them through interaction, likely using a hierarchical learning architecture that decomposes the problem into more tractable sub-problems (heuristics at different levels of abstraction). The goal is efficiency: faster convergence to stable, effective norms compared to flat or monolithic learning approaches.

**2. Implications and positioning (in lieu of full text)**

Without the complete paper, specific agreements and disagreements relative to other works cannot be firmly established. However, the work situates itself within a broader conversation in multi-agent systems and computational social simulation that has long been concerned with **efficiency of norm emergence** — a recurring pain point in classical approaches such as learning automata, reinforcement learning-based norm adoption, and evolutionary game-theoretic models, which often suffer from slow convergence or instability in larger populations. By introducing hierarchy, the authors likely follow a well-established machine learning intuition (decomposition speeds learning) and apply it to a coordination problem.

**3. Most urgent open question (given the truncated source)**

Because the paper's full methodology and results are not visible, the most urgent open question I can identify from the framing alone is: **How do hierarchical heuristics scale — and remain robust — as the number of agents and the complexity of the environment grow?** Specifically, it is unclear how the learned norms generalize across populations of different sizes, how they handle heterogeneous agents with conflicting preferences, and whether the hierarchical structure introduces its own coordination costs or brittleness when sub-heuristics misalign.

---

If you can share the
