# Literature Review — 2026-06-26
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 1

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks.
  - Network effects can rapidly spread privacy breaches across multi-agent systems.
  - AI agents are beginning to interact with each other directly and across internet platforms and physical environments, creating security challenges beyond traditional cybersecurity and AI safety frameworks.

## Synthesis
# Research Synthesis: Multi-Agent Security

The paper "Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents" frames an emerging problem space that traditional cybersecurity and AI safety frameworks were not designed to address. As AI agents begin to interact directly with each other across internet platforms and physical environments, a new class of security challenges emerges—one that requires reconceptualizing threats, defenses, and trust assumptions in systems composed of multiple autonomous actors rather than singular agents operating against fixed environments.

## 1. Points of Agreement

With only a single paper in this synthesis, the "agreement" dimension instead reflects the foundational consensus the work establishes. The paper agrees with established AI safety and security literature that existing frameworks—built around isolated models, static adversaries, and human-machine boundaries—are insufficient for the emerging reality of agent-to-agent interaction. There is alignment on the premise that adversarial dynamics, emergent behaviors, and compromised trust between automated systems represent qualitatively new risks that cannot be reduced to conventional software vulnerabilities or single-agent alignment problems.

## 2. Points of Disagreement

Disagreement cannot be assessed from a single source. However, the paper implicitly identifies tensions worth flagging: it pushes back against framings that treat multi-agent risks as merely extensions of single-agent safety, suggesting that the field's prevailing AI safety discourse has underweighted systemic interaction risks. This positions the work in contrast to approaches that prioritize model-level alignment or content filtering as sufficient safeguards, instead arguing for new abstractions tailored to populations of interacting agents.

## 3. Most Urgent Open Question

The most urgent open question raised is: **how do we design, analyze, and certify security properties for systems composed of many interacting AI agents when no single entity controls the full system?** This encompasses the need for threat models specific to inter-agent communication, trust establishment between autonomous actors from different principals, containment and sandboxing in dynamic multi-agent environments, and formal or empirical methods for predicting emergent adversarial behavior. Until this foundational question is addressed, deploying interacting
