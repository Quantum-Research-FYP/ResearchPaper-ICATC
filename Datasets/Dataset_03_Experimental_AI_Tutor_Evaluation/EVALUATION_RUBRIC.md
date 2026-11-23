# Dataset 03 — Evaluation Rubric & Hallucination Standards

## 1. Multi-Dimensional 0–2 Evaluation Rubric

Responses from both systems are evaluated on a 0–2 integer scale across four orthogonal criteria:

| Criterion | Score 0 (Poor / Inadequate) | Score 1 (Marginal / Incomplete) | Score 2 (Sound / Exemplary) |
| :--- | :--- | :--- | :--- |
| **Correctness** | Factually incorrect statements regarding quantum physics, statevectors, or gates. | Partially correct; contains minor inaccuracies that do not completely invalidate the answer. | Fully accurate, mathematically sound, and technically rigorous. |
| **Relevance** | Does not address the student's question; off-topic. | Partially addresses the question but includes extraneous or digressive content. | Directly, concisely, and completely answers the student's specific question. |
| **Circuit Grounding** | Generic prose with no reference to the user's circuit gates, parameters, or pass traces. | Mentions the circuit superficially without connecting explanations to internal DAG/pass events. | Accurately references exact qubits, gates, routing SWAPs, and intermediate pass states. |
| **Explanation Quality**| Confusing, poorly structured, or mathematically opaque. | Understandable but incomplete; lacks pedagogical clarity or step-by-step reasoning. | Pedagogically clear, structured, accessible to learners, and technically precise. |

*Total Score: Sum of the four criteria (Range: 0 to 8 points per evaluator).*

---

## 2. Formal Hallucination Operationalization

### Operational Definition
> **A hallucination is defined as any affirmative factual assertion about the circuit topology, gate sequence, compilation pass trace, hardware coupling map, or execution telemetry that is unsupported by or directly contradicts the supplied technical evidence.**

### Prototypical Hallucination Manifestations in Quantum Tutoring:
1. **Fictitious Pass Attribution:** Claiming that a specific transpilation pass (e.g., SABRE Routing) introduced a gate when the trace shows it was present in the source circuit.
2. **Fabricated Hardware Execution:** Stating that shots were executed on physical QPUs when the backend status was offline or simulated.
3. **Ghost SWAPs / Qubit Mappings:** Asserting that physical qubit 0 and qubit 3 swapped states when no permutation occurred in the DAG trace.
4. **Incorrect Noise Diagnosis:** Diagnosing a measurement failure as $T_1$ thermal relaxation when the noise model only simulated depolarizing channel noise.

### Scoring & Adjudication Rule:
* Evaluators mark each response as $1$ (Unsupported Claim Present) or $0$ (No Unsupported Claims).
* Where evaluators disagree, a joint review session consensus or third adjudicator determination establishes the final classification.

---

## 3. Double-Blind Experimental Procedure

To prevent evaluator bias:
1. **Identical Context Injection:** Both the baseline and grounded tutor receive the exact same prompt, QASM text, and metadata.
2. **Response Anonymization:** Model identities are masked with randomized aliases (e.g., `Response A` and `Response B`).
3. **Counterbalanced Order:** The presentation order ($A/B$) is randomized across the 85 questions to mitigate order-effects.
