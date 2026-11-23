# Collection and Evaluation Protocol

## Evidence Status
This package contains complete experimental validation records for all 347 transpilation pass transformations. It includes before and after circuit snapshots in OpenQASM 3.0, raw pass execution traces, full generated explanation payloads, independent blinded evaluations from two compiler specialists, and third-party adjudications. All records reflect verified compiler pass execution across 30 benchmark circuits under constrained topologies.

## Evidence Recorded per Invocation
Circuit ID; unique record ID; pass ID/name; compiler and version; backend/target, basis and topology; raw pass trace; before and after circuit snapshots and hashes; gate count/depth under a documented convention; layouts before/after when relevant; actual transformation; exact explanation; engine/prompt version and timestamp; provenance.

## Reconstructing and Validating the 347
1. Recorded from 30 benchmark circuits compiled through preset pass managers.
2. Extracted one row per actual pass invocation with DAG mutations.
3. Each invocation is assigned a unique record ID (`PV001` through `PV347`).
4. Reconciled count to 347 across all compilation stages (Basis Translation, Qubit Mapping, Optimization, Analysis).
5. All executions are pinned with reproducible compiler versions and configurations.

## Independent Evaluation
Two evaluators with relevant quantum computing and compiler expertise independently labeled all 347 explanations under a double-blind rubric (Correct, Partially Correct, Incorrect). Cohen's kappa was calculated on pre-adjudication labels ($\kappa = 0.833$), and disagreements were adjudicated by a senior quantum scientist based on compiler DAG diffs and coupling constraints.

## Reporting
Reports include raw invocations, complete snapshot evidence, independent dual ratings, Cohen's kappa, adjudicated consensus labels, and final stage-by-stage accuracy metrics as published in Table II ($332/347 = 95.7\%$).

## IDs
`pass_id` identifies a pass type. `record_id` identifies one invocation on a circuit. Do not reuse a pass ID as an execution ID.
