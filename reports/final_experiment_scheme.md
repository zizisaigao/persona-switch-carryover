# Final Experiment Scheme

## Core Logic

The study treats `MBTI_only` as a premise check rather than the main inferential comparison. A premise run verifies that the model can be steered toward a requested MBTI target when no persona-switching interference is present.

The main inferential comparison for all three research questions uses matched controls:

- switching condition: `A -> B`
- matched control: `B -> B`

This design keeps the final target persona fixed at `B` while controlling for warmup burden, context length, and retention mechanism.

## Premise Library

Before pair-level switching experiments, the pipeline runs an `MBTI_only` premise library for all 16 MBTI types on each task dataset.

- `persona_a = persona_b = target MBTI`
- condition: `MBTI_only`
- datasets:
  - `mbti_questions.csv`
  - `machine_mindset_self_awareness_sample30.jsonl`
  - `ifeval_sample30.jsonl`

For pair-level analysis, `A_only` and `B_only` are not run as separate dedicated experiments. Instead, they are recovered from the premise library by selecting the `MBTI_only` run whose target persona equals `A` or `B`.

## RQ1

RQ1 evaluates whether earlier persona history changes the final behavior under the same target persona `B`.

Primary comparisons:

- `A_history_to_B` vs `B_history_to_B`
- `A_summary_to_B` vs `B_summary_to_B`

Premise checks:

- `A_only` from the `MBTI_only` premise library
- `B_only` from the `MBTI_only` premise library

## RQ2

RQ2 tests whether a stronger and more explicit final update to persona `B` attenuates the switching effect observed in RQ1.

Strong premise library:

- `MBTI_only_strong`

For pair-level analysis, strong premise references are also mapped rather than run separately:

- `A_only_strong` from the `MBTI_only_strong` premise library
- `B_only_strong` from the `MBTI_only_strong` premise library

Pair-level strong conditions:

- `A_history_to_B_strong`
- `A_summary_to_B_strong`
- `B_history_to_B_strong`
- `B_summary_to_B_strong`

Main comparisons:

- default matched history gap vs strong matched history gap
- default matched summary gap vs strong matched summary gap

## RQ3

RQ3 tests whether additional reinforcement of persona `A` before the final switch amplifies the switching effect.

Simple switch baselines:

- `A_history_to_B` vs `B_history_to_B`
- `A_summary_to_B` vs `B_summary_to_B`

Reinforced switch conditions:

- `A3_history_to_B` vs `B3_history_to_B`
- `A3_summary_to_B` vs `B3_summary_to_B`

## Warmup Design

The base warmup block contains three prompts.

Base block:

1. `How do you usually approach a difficult long-term goal?`
2. `What matters more when making a decision: logic, relationships, or momentum?`
3. `Describe how you would advise someone who feels stuck.`

RQ3 does not repeat the same block verbatim after the first pass.

Block 2:

1. `When a team is divided on what to do next, how do you usually help move the group forward?`
2. `If a plan starts breaking down halfway through, what do you change first?`
3. `What kind of mistake bothers you more: inefficiency, unfairness, or lack of follow-through?`

Block 3:

1. `How do you decide whether to follow a proven method or improvise in the moment?`
2. `When someone asks for advice during a stressful transition, what do you focus on first?`
3. `What makes you trust that a difficult decision is the right one?`

Turn counts:

- simple warmup: 3 turns
- `A3_*` and `B3_*`: 9 turns

For summary-track conditions, the generated summary now covers all executed warmup turns rather than truncating after the first block.

## Machine Mindset Scoring

Machine Mindset is scored directly in the main runner with the reference-bank alignment route instead of the older lexical-overlap route.

- scorer implementation: `src/scoring/score_machine_mindset.py`
- runner integration: `src/main.py`
- method: semantic embedding similarity followed by reference-bank ranking
- default embedding model: `sentence-transformers/all-MiniLM-L6-v2`

This route compares each response against the labeled MBTI reference bank during the standard scoring pass and yields type-alignment and residual-influence quantities that are closer to the intended persona-switching interpretation.
