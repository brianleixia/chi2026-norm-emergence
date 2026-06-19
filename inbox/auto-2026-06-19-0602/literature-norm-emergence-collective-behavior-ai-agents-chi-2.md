# Literature Review — 2026-06-19
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 2

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly and across internet platforms and physical environments.
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks.
  - Network effects can rapidly spread privacy breaches across multi-agent systems.

## 2. Integrated Design and Governance of Agentic AI Systems through Adaptive Information Modulation
- Authors: Qiliang Chen, Sepehr Ilami, Nunzio Lorè | Year: 2024 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐⭐
- Claims:
  - Modern engineered systems increasingly involve complex sociotechnical environments where multiple agents, including humans and agentic AI powered by large language models, must navigate social dilemmas that pit individual interests against collective welfare.
  - As engineered systems evolve toward multi-agent architectures with autonomous LLM-based agents, traditional governance approaches are insufficient.
  - Agentic AI systems powered by large language models require integrated design and governance through adaptive information modulation to address collective action problems.

## Synthesis
# Synthesis of Two Papers on Multi-Agent AI Systems

## 1. Points of Agreement

Both papers converge on the recognition that the emergence of multi-agent AI systems—particularly those involving large language models and agentic AI—creates fundamentally new challenges that exceed the scope of traditional cybersecurity and AI safety frameworks. They share an understanding that as AI agents begin to interact with each other, with humans, and across both digital and physical environments, the security and governance landscape must be reconceptualized to account for emergent behaviors, inter-agent trust dynamics, and cascading failures that cannot be predicted from analyzing individual agents in isolation. Both works emphasize that system-level properties (resilience, alignment, controllability) become at least as important as the properties of any single agent, and both implicitly call for interdisciplinary approaches bridging technical security, governance theory, and systems engineering.

## 2. Points of Disagreement

The papers diverge meaningfully in their primary framing and proposed solutions. The first paper ("Open Challenges in Multi-Agent Security") adopts a predominantly **threat-centric and adversarial** lens, foregrounding risks such as agent hijacking, prompt injection across agent boundaries, collusion attacks, and the absence of robust authentication between autonomous agents. Its open-challenges framing suggests the field is still in a problem-identification phase, and it implicitly advocates for defensive mechanisms, standardized protocols, and threat modeling. The second paper ("Integrated Design and Governance through Adaptive Information") takes a more **constructive and holistic** stance, proposing an integrated design-governance framework in which adaptive information structures enable coordination, accountability, and alignment throughout the system lifecycle. It assumes that governance and technical architecture can—and should—be co-designed rather than treated sequentially, whereas the first paper treats security as a problem to be solved within an already-deployed ecosystem.

## 3. Most Urgent Open Question

The most pressing unresolved question bridging both works is: **Can we develop formal verification and runtime assurance methods that scale to systems of interacting agentic AIs operating in
