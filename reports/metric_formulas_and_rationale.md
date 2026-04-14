# Metric Formulas And Rationale

## Purpose

This document explains the metric system used in the finalized persona-switch pipeline.

It is written for a reader who does not already know the codebase. The goal is to make it possible to understand:

- what is being compared
- what each metric means
- how each metric is computed
- why the metric was constructed that way
- how the metrics are used differently in `RQ1`, `RQ2`, and `RQ3`

The explanation below reflects the current implemented pipeline rather than an earlier draft design.

## High-Level Experimental Logic

The study asks whether earlier persona context continues to influence model outputs after the active system prompt has been updated to a final target persona `B`.

The final pipeline separates the experiment into two conceptual layers:

1. premise checks
2. matched switch-versus-control comparisons

### Premise Checks

The premise checks verify that the model can express a requested MBTI target when there is no switching interference.

These runs are stored in premise libraries:

- `MBTI_only`
- `MBTI_only_strong`

For any ordered persona pair `A -> B`:

- `A_only` is not run separately
- `B_only` is not run separately
- both are recovered by selecting the matching target-persona run from `MBTI_only`

Similarly, in `RQ2`:

- `A_only_strong` and `B_only_strong` are recovered from `MBTI_only_strong`

These premise references are used as interpretive anchors, not as the main inferential contrast.

### Main Inferential Comparison

The main comparison is always a matched comparison between:

- a switch condition: `A -> B`
- a matched control: `B -> B`

This is the core design choice of the finalized pipeline.

The reason is methodological:

- both conditions end with the same target persona `B`
- both conditions use the same retention mechanism
- both conditions carry a similar warmup burden

As a result, differences between them are interpreted as evidence that the earlier persona content itself still matters.

### Retention Mechanisms

The pipeline evaluates two retention mechanisms:

- `history`: the full warmup dialogue is kept
- `summary`: a summary of the warmup dialogue is kept instead of the full dialogue

Therefore, the main `RQ1` comparisons are:

- `A_history_to_B` vs `B_history_to_B`
- `A_summary_to_B` vs `B_summary_to_B`

`RQ2` and `RQ3` extend these same matched comparisons rather than replacing them.

## Notation

To make the formulas easy to read, this document uses the following notation.

### Personas

- `A`: the earlier persona used during warmup
- `B`: the final target persona used at evaluation time

### Conditions

- `A -> B`: a switched condition
- `B -> B`: the matched control condition

More specifically:

- `A_history_to_B`
- `B_history_to_B`
- `A_summary_to_B`
- `B_summary_to_B`

For `RQ2`, the strong-update versions are:

- `A_history_to_B_strong`
- `B_history_to_B_strong`
- `A_summary_to_B_strong`
- `B_summary_to_B_strong`

For `RQ3`, the reinforced-warmup versions are:

- `A3_history_to_B`
- `B3_history_to_B`
- `A3_summary_to_B`
- `B3_summary_to_B`

### Samples And Outputs

For a task with `N` samples:

- `s` indexes a sample, where `s = 1, ..., N`
- `y_s^(cond)` denotes the model response for sample `s` under condition `cond`

### Premise References

- `A_only` means the premise-library run whose target persona is `A`
- `B_only` means the premise-library run whose target persona is `B`
- `A_only_strong` and `B_only_strong` are defined analogously from `MBTI_only_strong`

### Three Common Interpretive Dimensions

Across all three task families, the pipeline tries to measure three things:

1. target-oriented task success
2. consistency with the matched `B -> B` control
3. residual pull toward `A`

The metric names differ by task, but this three-part interpretation stays the same.

## Dataset 1: MBTI Multiple-Choice

### What The Task Represents

This task is the closed-form persona task.

Each sample is a forced-choice question whose options map to MBTI poles, for example:

- one option maps to `E`
- the other maps to `I`

The goal is not ordinary question-answering accuracy. The goal is to see whether the model's aggregate choice pattern aligns with the intended target persona.

### Sample-Level Scoring

For each response, the scorer first extracts the chosen option label:

- `predicted_label_s in {A, B, C, D}`

This is done by reading the first option-like label at the start of the response.

Then the option is mapped to a personality pole using the sample metadata:

- `selected_dimension_s in {E, I, S, N, T, F, J, P}`

For example:

- if option `A` is mapped to `I`
- and the response starts with `A`
- then the sample contributes one vote to `I`

### From Sample-Level Choices To A Final MBTI Type

For each run, the scorer counts how many times each MBTI pole was selected:

- `count(E), count(I), count(S), count(N), count(T), count(F), count(J), count(P)`

Then it constructs a final four-letter profile by majority vote:

```text
final_type =
  majority(E vs I)
  + majority(S vs N)
  + majority(T vs F)
  + majority(J vs P)
```

More explicitly:

```text
final_type =
  concat(
    argmax(count(E), count(I)),
    argmax(count(S), count(N)),
    argmax(count(T), count(F)),
    argmax(count(J), count(P))
  )
```

If a pair ties, the implementation records `X` for that position.

### MBTI Outcome Metrics

#### 1. Final-Type Match

This is the strictest outcome criterion:

```text
OSR_strict = 1(final_type == B)
```

Interpretation:

- `1` means the aggregate response pattern exactly matches the target persona
- `0` means it does not

This metric is easy to interpret but coarse, because near-misses and complete misses are both coded as `0`.

#### 2. Letter Match Rate

To obtain a graded outcome metric, the pipeline also computes the fraction of letters in the final type that match the target persona `B`.

If `final_type = f_1 f_2 f_3 f_4` and `B = b_1 b_2 b_3 b_4`, then:

```text
OSR_letter =
  (1/4) * sum_{k=1..4} 1(f_k == b_k)
```

Interpretation:

- `1.0` means a perfect four-letter match
- `0.75` means three letters match
- `0.5` means two letters match

This metric is used heavily because it preserves information about partial switching success.

### MBTI Matched-Control Consistency

The MBTI `SCS` metric measures how often the switch condition chooses the same option as the matched `B -> B` control on the same sample.

For sample `s`:

```text
agree_s = 1(predicted_label_s^(switch) == predicted_label_s^(matched control))
```

Then:

```text
SCS =
  (1/N) * sum_{s=1..N} agree_s
```

Interpretation:

- high `SCS` means the switched run behaves similarly to the matched `B -> B` control
- low `SCS` means the switched run has drifted away from the matched control

Why this is useful:

- it respects the finalized `A -> B` versus `B -> B` design
- it controls for warmup burden and retention mechanism
- it avoids over-relying on `B_only` as the main comparator

### MBTI Residual-A Influence

The MBTI `RAI` metric measures whether the switched response pattern remains closer to the `A` premise than to the matched `B -> B` control.

First compute agreement with the `A_only` premise:

```text
Agreement_A =
  (1/N) * sum_{s=1..N} 1(predicted_label_s^(switch) == predicted_label_s^(A_only))
```

Then define:

```text
RAI =
  Agreement_A - SCS
```

Interpretation:

- `RAI > 0`: the switched run is closer to `A_only` than to the matched `B -> B` control
- `RAI < 0`: the switched run is closer to the matched `B -> B` control
- `RAI = 0`: the switched run is equally close to both

Why this is useful:

- `SCS` alone only tells us whether the switch differs from the matched control
- `RAI` tells us whether that difference points back toward the earlier persona `A`

## Dataset 2: Machine Mindset

### What The Task Represents

This task is the open-ended persona-related task.

Unlike MBTI multiple-choice, the model produces free-form text. Therefore, the pipeline cannot compare discrete option labels directly.

The finalized scoring route uses a labeled MBTI reference bank and semantic embedding similarity.

### Why A Reference-Bank Scorer Is Used

In an open-ended task, purely lexical overlap is often misleading:

- two answers can express the same persona stance with very different wording
- two answers can share vocabulary while reflecting different persona tendencies

The reference-bank method tries to answer a more relevant question:

- which persona-labeled references is the generated answer most semantically similar to?

### Reference Bank Construction

The labeled source file is:

- `data/processed/machine_mindset_labeled.parquet`

From this file, the pipeline builds a prompt-aligned reference bank.

For each prompt key:

- the `self_awareness` bank stores reference answers for all 16 MBTI types
- the `dimension_pole` bank stores reference answers for the two poles of a single MBTI dimension

Formally, for a prompt `p`, the reference bank is:

```text
R_p = { (label_j, ref_j) }
```

where each `label_j` is either:

- a full MBTI type such as `ISTP`
- or a dimension code such as `T` or `F`

### Semantic Similarity Computation

The scorer embeds both the generated response and each prompt-matched reference answer.

Let:

- `e(y_s)` be the normalized embedding of the generated response
- `e(ref_j)` be the normalized embedding of reference `j`

The similarity is:

```text
sim(y_s, ref_j) = e(y_s) · e(ref_j)
```

Because the vectors are normalized, this is equivalent to cosine similarity.

The current default embedding model is:

- `sentence-transformers/all-MiniLM-L6-v2`

### Self-Awareness Subtask

For the self-awareness subset, the reference bank contains one answer per MBTI type.

#### Predicted Type

The predicted type is the label of the most similar reference:

```text
predicted_type_s =
  argmax_t sim(y_s, ref_t)
```

where `t` ranges over the 16 MBTI types.

#### Target Similarity

The target-oriented semantic score is:

```text
TargetSim_s = sim(y_s, ref_B)
```

This is the most important sample-level open-ended outcome measure.

#### Target Match

The type-level success indicator is:

```text
TypeMatch_s = 1(predicted_type_s == B)
```

This is a stricter, classification-style view of the same underlying similarity structure.

#### Target Rank

The target rank is the position of `B` in the sorted similarity list:

```text
Rank_B,s = rank of B in descending similarity order
```

Lower is better:

- `1` means the answer is most similar to the target persona
- larger values indicate weaker target alignment

#### Residual-A Margin

The residual-A margin is:

```text
RAI_margin_s = sim(y_s, ref_A) - sim(y_s, ref_B)
```

Interpretation:

- `RAI_margin_s > 0`: the answer is more similar to `A` than to `B`
- `RAI_margin_s < 0`: the answer is more similar to `B` than to `A`

### Dimension-Pole Subtask

For a dimension-pole prompt, the task compares only the two relevant codes for one dimension.

For example, if the dimension is `decision`, then the target code may be:

- `T` for a thinking-type target persona
- `F` for a feeling-type target persona

The same logic applies:

```text
predicted_code_s =
  argmax_c sim(y_s, ref_c)
```

```text
TargetCodeSim_s = sim(y_s, ref_target_code)
```

```text
CodeMatch_s = 1(predicted_code_s == target_code)
```

```text
RAI_margin_s = sim(y_s, ref_A_code) - sim(y_s, ref_target_code)
```

### Machine Mindset Aggregate Metrics

#### 1. Mean Target Similarity

For a set of `N` samples:

```text
Primary =
  (1/N) * sum_{s=1..N} TargetSim_s
```

This is the main open-ended target-alignment metric.

Why it is used:

- it is continuous
- it preserves semantic closeness information
- it does not collapse everything into a hard top-1 type decision

#### 2. Type-Match Or Code-Match Rate

For self-awareness:

```text
OSR_type_match_rate =
  (1/N) * sum_{s=1..N} TypeMatch_s
```

For dimension-pole:

```text
OSR_dimension_match_rate =
  (1/N) * sum_{s=1..N} CodeMatch_s
```

This is a stricter auxiliary outcome metric.

#### 3. Matched-Control Consistency

The Machine Mindset `SCS` metric asks whether the switched run and the matched `B -> B` control receive the same top-ranked persona prediction.

For sample `s`:

```text
agree_s =
  1(predicted_label_s^(switch) == predicted_label_s^(matched control))
```

Then:

```text
SCS =
  (1/N) * sum_{s=1..N} agree_s
```

The predicted label may be:

- `predicted_type`
- or `predicted_code`

depending on the subtask.

Interpretation:

- high `SCS` means the switched run is making the same top-level persona decision as the matched `B -> B` control
- low `SCS` means the switch condition has drifted away from that matched target-centered behavior

#### 4. Mean Residual-A Margin

The aggregate residual-A metric is:

```text
RAI =
  (1/N) * sum_{s=1..N} [sim_A,s - sim_B,s]
```

Interpretation:

- positive values mean more residual similarity to `A`
- negative values mean stronger alignment with `B`

## Dataset 3: IFEval

### What The Task Represents

This task is the constrained instruction-following task.

Unlike the other two tasks, its main target is not a persona label. Its core question is whether earlier persona context affects instruction-following performance when the final target persona is held fixed.

### Official-Checker-Only Design

The finalized pipeline now supports only the official Google IFEval metadata route.

Therefore, each IFEval sample must provide:

- `instruction_id_list`
- `kwargs`

No legacy fallback rule-based scoring is used in the active pipeline.

### Sample-Level Official Scoring

For each sample, the official checker evaluates the response under two standards:

- strict
- loose

The current analysis focuses mainly on the strict outputs.

For sample `s`, the scorer returns:

- `instruction_count_s`
- `strict_follow_all_s`
- `strict_checks_passed_s`
- `loose_follow_all_s`
- `loose_checks_passed_s`

#### Strict All

The strict all-instructions indicator is:

```text
StrictAll_s = 1(all required instructions are satisfied under the strict checker)
```

#### Strict Instruction Fraction

The per-sample strict fraction is:

```text
StrictFrac_s =
  strict_checks_passed_s / instruction_count_s
```

This gives partial credit when some but not all instructions are followed.

### IFEval Aggregate Metrics

#### 1. Strict Follow-All Rate

```text
Primary =
  strict_follow_all_rate =
  (1/N) * sum_{s=1..N} StrictAll_s
```

This is the main task-success metric.

It answers:

- how often does the model fully satisfy the instruction bundle?

#### 2. Mean Strict Instruction Fraction

```text
Secondary =
  mean_strict_instruction_fraction =
  (1/N) * sum_{s=1..N} StrictFrac_s
```

This is a softer companion metric.

It answers:

- when the model fails to follow every instruction, how much of the instruction set did it still satisfy?

### Why IFEval Also Uses Lexical Similarity

IFEval does not provide a persona-labeled reference bank, so the pipeline cannot build a persona-alignment scorer analogous to Machine Mindset.

However, the study still needs a way to ask:

- is the switched answer behaving more like the matched `B -> B` answer or more like the `A` premise?

To capture this, the pipeline uses a lexical overlap proxy.

### Lexical F1 Between Two Texts

Define the token set of a text `x` as:

```text
T(x) = set of lowercase alphanumeric tokens in x
```

Given two texts `x` and `z`:

```text
precision(x, z) =
  |T(x) ∩ T(z)| / |T(x)|
```

```text
recall(x, z) =
  |T(x) ∩ T(z)| / |T(z)|
```

```text
LexF1(x, z) =
  2 * precision(x, z) * recall(x, z) / (precision(x, z) + recall(x, z))
```

If one side has no tokens or the denominator is zero, the implementation returns `0`.

### IFEval Matched-Control Consistency

For sample `s`:

```text
SCS_s =
  LexF1(y_s^(switch), y_s^(matched control))
```

Then:

```text
SCS =
  (1/N) * sum_{s=1..N} SCS_s
```

Interpretation:

- high lexical `SCS` means the switched answer looks more like the matched `B -> B` answer
- low lexical `SCS` means it has drifted away at the surface-text level

### IFEval Residual-A Influence

For sample `s`, compute:

```text
LexA_s = LexF1(y_s^(switch), y_s^(A_only))
```

```text
LexB_s = LexF1(y_s^(switch), y_s^(matched control))
```

Then:

```text
RAI =
  (1/N) * sum_{s=1..N} (LexA_s - LexB_s)
```

Interpretation:

- positive `RAI` means the switched answer is lexically closer to `A_only`
- negative `RAI` means it is lexically closer to the matched `B -> B` answer

This is an auxiliary diagnostic, not the main task-success measure.

## Research-Question-Level Comparison Logic

The next step is to explain how these dataset-specific metrics are used differently in `RQ1`, `RQ2`, and `RQ3`.

## RQ1: Detecting A Switching Effect

`RQ1` asks whether earlier persona context affects behavior when the final target persona is fixed at `B`.

For each task, the analysis uses the same three-part structure:

1. target-oriented outcome
2. consistency with the matched `B -> B` control
3. residual pull toward `A`

### RQ1 For MBTI

For each track (`history` or `summary`):

- outcome:
  - `OSR_letter`
- matched consistency:
  - `SCS_item_agreement_with_matched_b_control`
- residual-A:
  - `RAI_item_agreement_gap`

The switch comparison row therefore summarizes:

```text
OSR_letter
SCS
RAI
```

for:

- `A_history_to_B` vs `B_history_to_B`
- or `A_summary_to_B` vs `B_summary_to_B`

### RQ1 For Machine Mindset

For each track:

- outcome:
  - `mean_target_similarity`
- matched consistency:
  - `scs_predicted_agreement_with_matched_b_control`
- residual-A:
  - `mean_rai_margin_a_minus_target`

This tells us:

- whether the switched answers still align semantically with `B`
- whether they behave like the matched `B -> B` control
- whether they remain pulled toward `A`

### RQ1 For IFEval

For each track:

- outcome:
  - `strict_follow_all_rate`
- secondary:
  - `mean_strict_instruction_fraction`
- matched consistency:
  - lexical `SCS`
- residual-A:
  - lexical `RAI`

This gives a task-success measure and a directional surface-text measure at the same time.

## RQ2: Does A Stronger Final Update Reduce The Switching Effect?

`RQ2` compares:

- default matched gap
- versus strong-update matched gap

The basic intuition is:

- if the strong final `B` update is effective
- then the switched run should look more like the matched `B -> B` control
- and less like the `A` premise

### RQ2 For MBTI

For each track:

#### Default Distance To Matched Control

```text
Dist_default = 1 - SCS_default
```

#### Strong Distance To Matched Control

```text
Dist_strong = 1 - SCS_strong
```

#### Default Outcome Gap

```text
GapOSR_default =
  |OSR_default - OSR_control_default|
```

#### Strong Outcome Gap

```text
GapOSR_strong =
  |OSR_strong - OSR_control_strong|
```

#### Default And Strong Residual-A

```text
RAI_default =
  Agreement_A_default - SCS_default
```

```text
RAI_strong =
  Agreement_A_strong - SCS_strong
```

Then the script makes three Boolean judgments:

```text
improved_distance =
  1(Dist_strong < Dist_default)
```

```text
improved_osr_gap =
  1(GapOSR_strong < GapOSR_default)
```

```text
reduced_a_influence =
  1(RAI_strong < RAI_default)
```

Finally:

```text
RQ2_improved =
  1(at least two of the three judgments are true)
```

### RQ2 For Machine Mindset

The same logic is reused with task-appropriate quantities.

#### Distances

```text
Dist_default = 1 - SCS_default
```

```text
Dist_strong = 1 - SCS_strong
```

#### Primary Gaps

```text
GapPrimary_default =
  |Primary_default - Primary_control_default|
```

```text
GapPrimary_strong =
  |Primary_strong - Primary_control_strong|
```

#### Residual-A

```text
RAI_default =
  mean(sim_A - sim_B)_default
```

```text
RAI_strong =
  mean(sim_A - sim_B)_strong
```

Then:

```text
improved_distance =
  1(Dist_strong < Dist_default)
```

```text
improved_primary_gap =
  1(GapPrimary_strong < GapPrimary_default)
```

```text
reduced_a_influence =
  1(RAI_strong < RAI_default)
```

```text
RQ2_improved =
  1(at least two are true)
```

### RQ2 For IFEval

IFEval uses the same structure, but the distance-like comparison is based on the primary outcome gap rather than `1 - lexical SCS`.

#### Primary Gaps

```text
GapPrimary_default =
  |Primary_default - Primary_control_default|
```

```text
GapPrimary_strong =
  |Primary_strong - Primary_control_strong|
```

#### Lexical Matched Consistency

```text
SCS_default =
  mean LexF1(switch_default, matched_control_default)
```

```text
SCS_strong =
  mean LexF1(switch_strong, matched_control_strong)
```

#### Residual-A

```text
RAI_default =
  mean [LexF1(switch_default, A_only) - LexF1(switch_default, matched_control_default)]
```

```text
RAI_strong =
  mean [LexF1(switch_strong, A_only_strong) - LexF1(switch_strong, matched_control_strong)]
```

Then:

```text
improved_primary_gap =
  1(GapPrimary_strong < GapPrimary_default)
```

```text
improved_lexical_scs =
  1(SCS_strong > SCS_default)
```

```text
reduced_a_influence =
  1(RAI_strong < RAI_default)
```

```text
RQ2_improved =
  1(at least two are true)
```

### Why RQ2 Uses Majority Voting

The strong-update hypothesis is broader than any single metric.

If the update really reduces carry-over, one would expect several things to happen at once:

- the switched run becomes more similar to the matched `B -> B` control
- the task-level gap shrinks
- residual pull toward `A` weakens

Using a majority rule makes the decision more robust than relying on one metric alone.

## RQ3: Does Stronger A Reinforcement Increase The Switching Effect?

`RQ3` compares:

- the simple switch condition
- against the reinforced 9-turn switch condition

The idea is the reverse of `RQ2`:

- if stronger reinforcement of `A` makes switching harder
- then the reinforced condition should drift farther from the matched `B -> B` control
- and show more residual-A influence

### RQ3 For MBTI

For each track:

```text
Dist_simple = 1 - SCS_simple
```

```text
Dist_reinf = 1 - SCS_reinf
```

```text
GapOSR_simple =
  |OSR_simple - OSR_control_simple|
```

```text
GapOSR_reinf =
  |OSR_reinf - OSR_control_reinf|
```

```text
RAI_simple =
  Agreement_A_simple - SCS_simple
```

```text
RAI_reinf =
  Agreement_A_reinf - SCS_reinf
```

Then:

```text
weakened_distance =
  1(Dist_reinf > Dist_simple)
```

```text
weakened_osr_gap =
  1(GapOSR_reinf > GapOSR_simple)
```

```text
increased_a_influence =
  1(RAI_reinf > RAI_simple)
```

```text
RQ3_weakened =
  1(at least two are true)
```

### RQ3 For Machine Mindset

The same logic applies:

```text
weakened_distance =
  1((1 - SCS_reinf) > (1 - SCS_simple))
```

```text
weakened_primary_gap =
  1(GapPrimary_reinf > GapPrimary_simple)
```

```text
increased_a_influence =
  1(RAI_reinf > RAI_simple)
```

```text
RQ3_weakened =
  1(at least two are true)
```

### RQ3 For IFEval

For IFEval:

```text
weakened_primary_gap =
  1(GapPrimary_reinf > GapPrimary_simple)
```

```text
weakened_lexical_scs =
  1(SCS_reinf < SCS_simple)
```

```text
increased_a_influence =
  1(RAI_reinf > RAI_simple)
```

```text
RQ3_weakened =
  1(at least two are true)
```

## Why The Metric System Is Structured This Way

The final metric framework tries to balance three needs:

1. task appropriateness
2. cross-task comparability
3. directional interpretability

### Why Not Use One Metric For Everything?

The three tasks are structurally different:

- MBTI uses discrete forced choices
- Machine Mindset uses free-form persona-related responses
- IFEval uses instruction-following constraints

A single metric would either be too crude for some tasks or too artificial for others.

Therefore, the pipeline uses task-specific surface metrics while preserving a shared interpretive logic.

### Why Always Include A Matched-Control Term?

The central methodological concern is to separate:

- the effect of earlier persona content
from
- the effect of warmup burden, context length, and retention mechanism

That is why the main comparison is never just:

- `A -> B` vs `B_only`

Instead, it is:

- `A -> B` vs matched `B -> B`

This makes the inference more defensible.

### Why Always Include A Residual-A Metric?

A switched run can differ from the matched control for many reasons.

Residual-A metrics are intended to answer a more specific question:

- is the deviation pointing back toward the earlier persona `A`?

Without that directional component, a gap from the matched control might reflect generic noise rather than carry-over.

### Why Use Majority Voting In RQ2 And RQ3?

`RQ2` and `RQ3` are ablation-style questions.

They do not ask whether one single number moves in the expected direction. They ask whether the intervention changes the overall switching pattern.

Majority voting across:

- matched-control distance
- task outcome gap
- residual-A influence

provides a more stable answer than any one component alone.

## Practical Reading Guide

When reading result tables, the intended interpretation is:

### For RQ1

Ask three questions:

1. does the switched run still achieve the target-oriented outcome?
2. how far is it from the matched `B -> B` control?
3. is the deviation pulled toward `A`?

### For RQ2

Compare the default and strong versions of the same track:

1. does the strong version move closer to the matched control?
2. does the task-level gap shrink?
3. does residual-A influence drop?

### For RQ3

Compare the simple and reinforced versions of the same track:

1. does the reinforced version move farther from the matched control?
2. does the task-level gap worsen?
3. does residual-A influence increase?

## Current Scope And Limitations

The current metric framework is coherent, but it still has task-specific limitations.

### MBTI

Strengths:

- direct and interpretable
- strong discrete signal

Limitations:

- final-type aggregation compresses item-level nuance
- the `X` tie state is coarse

### Machine Mindset

Strengths:

- uses semantic similarity rather than only lexical overlap
- directly compares responses against MBTI-labeled references

Limitations:

- still depends on the quality and coverage of the reference bank
- semantic similarity is a proxy rather than a ground-truth persona label

### IFEval

Strengths:

- uses an official checker for the main task outcome
- preserves strict instruction-following semantics

Limitations:

- lexical `SCS` and lexical `RAI` are auxiliary diagnostics rather than native instruction metrics
- they capture output similarity, not a direct persona classification

## Summary

The finalized metric system can be summarized as follows.

### MBTI

- outcome: target-type match and letter match rate
- matched consistency: item-level agreement with `B -> B`
- residual-A: agreement with `A_only` minus agreement with `B -> B`

### Machine Mindset

- outcome: mean semantic similarity to the target reference bank
- matched consistency: agreement in predicted top-ranked persona label with `B -> B`
- residual-A: semantic similarity to `A` minus semantic similarity to `B`

### IFEval

- outcome: strict follow-all rate
- secondary: mean strict instruction fraction
- matched consistency: lexical similarity to `B -> B`
- residual-A: lexical similarity to `A_only` minus lexical similarity to `B -> B`

Across all three tasks:

- `RQ1` detects whether a switching effect exists
- `RQ2` tests whether a stronger final update reduces it
- `RQ3` tests whether stronger earlier-persona reinforcement increases it

That common structure is what makes the pipeline interpretable as one coherent study rather than three unrelated scoring schemes.
