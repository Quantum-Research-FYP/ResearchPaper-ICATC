# Evaluation rubric v1.0

## Unit
One unit is one actual compiler-pass invocation on one circuit, paired with the actual before/after snapshots, raw trace, target/compiler context and the exact explanation shown to evaluators. A pass catalogue entry or predicted pass is not an execution record.

## Blinding
Two evaluators independently assess randomized records. They must not see each other's labels, the engine's claimed correctness, aggregate accuracy, or each other's comments. Preserve original independent labels before adjudication.

## Correct
The explanation accurately describes the actual transformation visible in the snapshots/trace and gives a supported reason in the recorded compiler/target context. It makes no unsupported causal claims.

## Partially correct
It identifies the main transformation or a materially related effect, but omits an important detail, is imprecise, or gives incomplete reasoning. A plausible but non-primary cause for a Mapping/Layout choice is Partially correct if the mapping effect is correctly identified but the stated reason is not established as primary.

## Incorrect
It misidentifies the transformation, contradicts the snapshots/trace, or gives a false/unsupported reason that materially misrepresents what happened.

## Mapping/Layout special rule
A plausible but non-primary cause is Partially correct, not Correct. It is Incorrect if the claimed cause materially misrepresents the operation or resulting mapping. Evaluators must cite the observed layout change and recorded compiler configuration; never infer the objective from the pass name alone.

## Non-transforming passes
Analysis/property-collection passes can be Correct even if the circuit is unchanged, provided the explanation accurately describes the analysis/property update and its purpose.

## Not evaluable
If essential snapshots, raw trace or configuration are absent, mark `NOT_EVALUABLE` in a separate data-quality field. Do not force it into one of the three labels. Report these records and reasons separately.

## Outcomes
Strict explanation correctness = Correct / evaluable explanations. Report Partially correct and Incorrect percentages separately. An optional (Correct + Partial) rate must be named separately and must not replace strict correctness.

## Evaluator training
Record expertise, training date/duration, rubric version and calibration exercise. Calibration records used to refine the rubric should be excluded from the final independent score or re-rated under the frozen rubric.
