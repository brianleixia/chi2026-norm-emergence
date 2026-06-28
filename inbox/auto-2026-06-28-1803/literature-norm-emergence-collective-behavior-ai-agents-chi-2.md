# Literature Review — 2026-06-28
**Query:** norm emergence collective behavior AI agents CHI 2026
**Papers reviewed:** 1

## 1. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents
- Authors: Christian Schroeder de Witt, Krawiecka, Klaudia, Krawczuk, Igor | Year: 2025 | Venue: arXiv (Cornell University)
- Novelty: ⭐⭐
- Claims:
  - AI agents are beginning to interact with each other directly and across internet platforms and physical environments, creating security challenges beyond traditional cybersecurity and AI safety frameworks.
  - Free-form protocols are essential for AI's task generalization but enable new threats like secret collusion and coordinated swarm attacks.
  - Network effects can rapidly spread privacy breaches across interconnected agent systems.

## Synthesis
I notice you've asked me to synthesize findings across 1 paper, but a true synthesis requires comparing multiple sources to identify agreements, disagreements, and gaps. With only one paper, I can offer a structured summary, but the "agreement/disagreement" framing doesn't fully apply. Here's what I can offer:

---

**1. What the paper establishes (consensus landscape)**

The paper by Hammond et al. situates multi-agent security as a distinct and urgent subfield, arguing that traditional cybersecurity and single-agent AI safety frameworks are insufficient when AI agents interact with each other across digital and physical environments. It surfaces an emerging consensus that the *interaction layer* between agents—rather than individual agents themselves—creates novel attack surfaces. The paper frames core challenges around emergent behaviors from agent-to-agent communication, the lack of secure protocols for inter-agent trust, and the absence of standardized defenses for multi-agent systems. Implicitly, it agrees with the broader AI safety community that current deployment is outpacing formal security guarantees, while pushing that conversation into the multi-agent regime specifically.

---

**2. Tensions within the paper itself (and implicit disagreements with adjacent fields)**

The paper acknowledges a tension between *capability-focused* multi-agent research (which treats emergent interaction as a feature to be scaled) and *security-focused* research (which treats it as a risk to be constrained). It implicitly disagrees with single-agent safety frameworks that assume a human or fixed system as the trust boundary—since in multi-agent settings, trust must be dynamically negotiated. The paper also flags unresolved disagreement on whether defenses should be *protocol-level* (standardized inter-agent communication standards), *agent-level* (each agent sandboxed and verified), or *system-level* (monitoring emergent behavior across the swarm). The absence of a clear winner among these approaches is itself a point of friction.

---

**3. Most urgent open question**

The paper implicitly identifies the central gap as: **How do we establish trustworthy interaction between AI agents without a central
