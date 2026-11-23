# Collection and evaluation protocol

## Evidence status
This package contains schemas, a rubric, evaluation forms and 347 blank reconciliation slots. It does not contain the historical 347 raw pass invocations, before/after snapshots, exact generated explanations or independent ratings. The slots are not claimed to be actual executions. The 332/347 (95.7%) result is not independently verified by this package.

## Evidence required per invocation
Circuit ID; unique record ID; pass ID/name; compiler and version; backend/target, basis and topology; raw pass trace; before and after circuit snapshots and hashes; gate count/depth under a documented convention; layouts before/after when relevant; actual transformation; exact generated explanation; engine/prompt version and timestamp; provenance.

## Reconstructing the 347
1. Recover original 30-circuit source, pass-manager logs, snapshots and explanation outputs.
2. Extract one row per actual pass invocation (not one row per unique pass type).
3. Give each invocation a unique record ID; repeated use of a pass gets separate records.
4. Reconcile count to 347; document missing, duplicate, failed and non-transforming passes.
5. If original records are unavailable, rerun with pinned versions/configuration and label as reproduced, not historical original records.
6. Do not invent rows to force the total to 347.

## Independent evaluation
Use two evaluators with relevant quantum computing/compiler expertise. Record qualifications and rubric training. Randomize and blind the records. Each evaluator independently labels all evaluable explanations. Calculate Cohen's kappa on paired pre-adjudication labels. Then resolve disagreements using a third qualified adjudicator or documented consensus. Preserve both original labels and the final label.

## Reporting
Report raw invocations recovered; records with complete evidence; not-evaluable records and reasons; number independently rated by both; evaluator expertise/training; evaluator cross-tabulation; Cohen's kappa; disagreements and adjudication method; final Correct/Partial/Incorrect counts and percentages; strict correctness denominator.

## IDs
`pass_id` identifies a pass type. `record_id` identifies one invocation on a circuit. Do not reuse a pass ID as an execution ID.
