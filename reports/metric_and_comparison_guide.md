# Metric And Comparison Guide

## Overview

The current pipeline separates premise checks from inferential comparisons.

- `MBTI_only` and `MBTI_only_strong` are premise libraries.
- `A_only`, `B_only`, `A_only_strong`, and `B_only_strong` are analysis-side reference labels mapped from those premise libraries.
- The main inferential comparison for all three research questions is always a matched comparison between an `A -> B` switch condition and a `B -> B` control condition with the same retention mechanism.

This keeps the final target persona fixed at `B` while controlling for warmup burden and context packaging.

## Premise Checks

Premise checks are not the main hypothesis tests. They verify that the model can be steered toward a requested MBTI target when no persona-switching interference is present.

- `RQ1` premise library: `MBTI_only`
- `RQ2` premise library: `MBTI_only_strong`
- `RQ3` reuses the `RQ1` premise library

For pair-level analysis:

- `A_only` is mapped from the `MBTI_only` run whose target persona equals `A`
- `B_only` is mapped from the `MBTI_only` run whose target persona equals `B`
- `A_only_strong` is mapped from the `MBTI_only_strong` run whose target persona equals `A`
- `B_only_strong` is mapped from the `MBTI_only_strong` run whose target persona equals `B`

## Main Comparison Structure

### RQ1

RQ1 asks whether earlier persona context changes final behavior under the same target persona `B`.

Matched comparisons:

- `A_history_to_B` vs `B_history_to_B`
- `A_summary_to_B` vs `B_summary_to_B`

### RQ2

RQ2 asks whether a stronger and more explicit final update to persona `B` attenuates the matched switching effect seen in RQ1.

Matched comparisons:

- default history gap: `A_history_to_B` vs `B_history_to_B`
- strong history gap: `A_history_to_B_strong` vs `B_history_to_B_strong`
- default summary gap: `A_summary_to_B` vs `B_summary_to_B`
- strong summary gap: `A_summary_to_B_strong` vs `B_summary_to_B_strong`

### RQ3

RQ3 asks whether stronger pre-switch reinforcement of persona `A` amplifies the matched switching effect.

Matched comparisons:

- simple history gap: `A_history_to_B` vs `B_history_to_B`
- reinforced history gap: `A3_history_to_B` vs `B3_history_to_B`
- simple summary gap: `A_summary_to_B` vs `B_summary_to_B`
- reinforced summary gap: `A3_summary_to_B` vs `B3_summary_to_B`

## Dataset-Specific Metrics

The three datasets use a consistent logic but task-appropriate surface metrics.

### Shared Logic

Each task family uses the same three-part interpretation:

1. target-oriented outcome
2. consistency with the matched `B -> B` control
3. residual pull toward the `A` premise

The exact metric names differ by task because the tasks are structurally different.

### MBTI Multiple-Choice

MBTI is treated as the closed-form target-persona task.

Primary quantities:

- `final_type`
- `osr_letter_match_rate`
- `osr_final_type_match_target_b`

Matched-control consistency:

- `scs_item_agreement_with_matched_b_control`
- `distance_to_matched_b_control = 1 - scs`

Residual `A` influence:

- `agreement_with_a_premise`
- `rai_item_agreement_gap = agreement_with_a_premise - scs`

Interpretation:

- larger `osr_letter_match_rate` means the final MBTI profile is closer to target `B`
- larger `scs_item_agreement_with_matched_b_control` means the switched run behaves more like the matched `B -> B` control
- larger `rai_item_agreement_gap` means more residual pull toward `A`

### Machine Mindset

Machine Mindset is treated as the open-ended persona-alignment task.

The active scoring path is the reference-bank alignment scorer with semantic embedding similarity and ranking, and this scoring is now produced directly by the main experiment runner rather than through a separate post-hoc pass.

Primary quantities:

- `mean_target_similarity`
- `osr_type_match_rate` or `osr_dimension_match_rate`

Matched-control consistency:

- `scs_predicted_agreement_with_matched_b_control`
- `distance_to_matched_b_control = 1 - scs`

Residual `A` influence:

- `mean_rai_margin_a_minus_target`
- `rai_item_agreement_gap = agreement_with_a_premise - scs`

Interpretation:

- larger `mean_target_similarity` means the response is semantically closer to the target `B` reference bank
- larger `scs_predicted_agreement_with_matched_b_control` means the switched run receives the same top-ranked persona prediction as the matched `B -> B` control
- larger `mean_rai_margin_a_minus_target` means more residual similarity to `A` than to target `B`

### IFEval

IFEval is treated as the constrained instruction-following task.

Primary quantities:

- `strict_follow_all_rate`

Secondary quantities:

- `mean_strict_instruction_fraction`

Matched-control consistency:

- `scs_lexical_similarity_to_matched_b_control`

Residual `A` influence:

- `rai_lexical_gap = lexical_similarity_to_a_premise - lexical_similarity_to_matched_b_control`

Interpretation:

- the primary outcome measures instruction-following success under the official Google IFEval checker
- lexical `SCS` measures how similar the switched answer is to the matched `B -> B` answer
- lexical `RAI` measures whether the switched answer stays closer to `A` than to the matched `B -> B` control

## RQ1 Pair Routing

Pair routing for downstream full runs is intentionally simple.

- only `mbti_mcq` rows are used
- only `A -> B` switch rows are considered
- a row is `successful` if `final_type_switch == target_persona_b`
- otherwise it is `failed`

The routing script applies this rule separately to:

- `A_history_to_B`
- `A_summary_to_B`

As a result:

- pairs with `A -> B` rows that end at `B` are routed as `successful`
- pairs with `A -> B` rows that do not end at `B` are routed as `failed`

This routing is deliberately narrower than the main reporting metrics. It is used only to decide whether a pair enters `RQ2` or `RQ3`.

## RQ2 Decision Logic

RQ2 compares default matched gaps against strong-update matched gaps.

For each task family, the script records whether strong updating:

1. reduces distance to the matched `B -> B` control
2. improves the task-specific primary gap against the matched `B -> B` control
3. reduces residual `A` influence

`rq2_improved` is `true` when at least two of these three checks improve.

## RQ3 Decision Logic

RQ3 compares simple matched gaps against 9-turn reinforced matched gaps.

For each task family, the script records whether reinforcement:

1. increases distance to the matched `B -> B` control
2. worsens the task-specific primary gap against the matched `B -> B` control
3. increases residual `A` influence

`rq3_weakened` is `true` when at least two of these three checks worsen.

## Current Consistency Status

The current scripts now follow one aligned comparison logic across `RQ1`, `RQ2`, and `RQ3`:

- premise checks are always library-based references
- main inference is always matched `A -> B` vs `B -> B`
- each task family reports a target-oriented metric, a matched-control consistency metric, and an `A`-residual metric

The metric names differ by task, but the comparison logic is the same.
