# RQ2 and RQ3 Implementation Plan

## Scope Rule

This plan follows the user's refined research-question definitions, not the revised GitHub-only framing in `RQ_UPDATE_2026-04-03.md`.

The active scope is:

- `RQ1`: MBTI multiple-choice + Machine Mindset + IFEval
- `RQ2`: MBTI multiple-choice + Machine Mindset + IFEval
- `RQ3`: MBTI multiple-choice + Machine Mindset + IFEval

This document covers only the implementation plan for `RQ2` and `RQ3`.

## Refined Research Questions

### RQ1

Under the same final target persona `B`, does system prompt history (`B_only` vs `A -> B`) affect model behavior on:

- closed-form multiple-choice items
- open-ended persona-related responses
- constrained instruction-following tasks

### RQ2

For persona pairs classified as failed switches in `RQ1`, does strengthening and making the `B` update prompt more explicit improve switch effectiveness?

### RQ3

For persona pairs classified as successful switches in `RQ1`, does additional warm-up or reinforcement of persona `A` (for example `A -> A -> B` or `A -> A -> A -> B`) weaken the originally successful switch?

## Reuse Strategy

The project already has useful infrastructure that should be preserved:

- unified sample loading in `src/utils/io.py`
- persona and condition config structure in `configs/`
- warm-up and switch execution in `src/runner/`
- reusable run outputs in `outputs/raw_generations/` and `outputs/scored/`
- MBTI scoring in `src/scoring/score_mbti.py`
- Machine Mindset alignment scoring in `src/scoring/machine_mindset_alignment.py`
- IFEval scoring in `src/scoring/score_ifeval.py`

The preferred strategy is to extend the current runner with the smallest possible changes instead of building separate pipelines for each research question.

## Shared Design Principles

### Final-target baseline

For both `RQ2` and `RQ3`, the primary baseline should remain `B_only`.

All switch conditions should be interpreted relative to the same final target persona `B`.

### Existing metrics to preserve

For MBTI multiple-choice:

- `OSR`
- `SCS`
- `RAI`

For Machine Mindset:

- target-persona alignment
- `SCS`-like agreement with `B_only`
- `RAI`-like residual influence from earlier persona history

For IFEval:

- instruction-following rate
- pass-rate style summaries
- deltas relative to `B_only`

### Pair-selection rule

`RQ2` and `RQ3` should not automatically run on every persona pair.

The intended workflow is:

1. run `RQ1`
2. classify persona pairs as failed or successful switches
3. send failed pairs into `RQ2`
4. send successful pairs into `RQ3`

## RQ2 Goal

`RQ2` focuses only on persona pairs that were failed switches in `RQ1`.

The key variable is the strength and explicitness of the final update to persona `B`.

## RQ2 Experimental Design

### Reuse-first rule

`RQ2` should reuse the default-side runs from `RQ1` whenever those runs are compatible in:

- model
- persona pair
- dataset
- sample IDs
- condition semantics

The reusable default condition grid is:

- `B_only_default`
- `A_history_to_B_default`
- `A_summary_to_B_default`
- `B_history_to_B_default`
- `B_summary_to_B_default`

### New strong-prompt grid

`RQ2` only needs to add the strong-prompt side:

- `B_only_strong`
- `A_history_to_B_strong`
- `A_summary_to_B_strong`
- `B_history_to_B_strong`
- `B_summary_to_B_strong`

This gives a five-condition strong grid plus a reusable five-condition default grid.

### Dataset coverage

`RQ2` should be run on all three datasets:

- MBTI multiple-choice
- Machine Mindset
- IFEval

The strong-switch intervention should therefore be added in a dataset-agnostic way at the message-construction layer.

## RQ2 Prompting Changes

### Current state

The current persona prompt is very light-weight:

- `You are Persona: <TYPE>.`

That is sufficient for basic persona conditioning, but too weak for `RQ2`.

### Planned extension

Add a configurable switch-strength layer in message construction.

Recommended two-level scheme:

- `default`
  - keep the current persona prompt behavior
- `strong`
  - explicitly restate that the active persona is now `B`
  - explicitly instruct the model to treat earlier persona content as historical context only
  - explicitly forbid continuing the prior persona style
  - explicitly instruct the model not to blend or preserve persona `A`

### Strong switch template

The exact wording can be refined, but the intended behavior is:

- active persona is now `B`
- prior conversation may mention a different persona
- prior persona should not control the current response
- respond only from the perspective of `B`
- do not continue or blend persona `A`

## RQ2 Code Changes

### Config changes

Add five strong variants in `configs/experiments.yaml` while leaving the existing default conditions untouched.

Recommended metadata fields:

- `switch_strength: default | strong`
- `retain_mechanism: none | history | summary`

### Message-building changes

Extend `src/runner/build_messages.py` so the final evaluation prompt can include:

- the normal persona system prompt
- an optional stronger reset instruction block for the strong conditions

This should be done in one place so MBTI, Machine Mindset, and IFEval stay aligned.

### Analysis changes

Extend the downstream aggregation so each strong condition can be compared against:

- the matching reusable default condition
- the matching `B_only` baseline
- the same retention mechanism under `default` vs `strong`

## RQ2 Metrics

### MBTI

For each condition:

- final predicted MBTI type
- `OSR` relative to target `B`
- `SCS` relative to `B_only`
- `RAI`

For improvement:

- compare `default` vs `strong`
- report whether stronger switch instructions move scores closer to `B_only`

### Machine Mindset

For each condition:

- target-persona alignment
- agreement with `B_only`
- `RAI`-like margin against persona `A`

For improvement:

- compare `default` vs `strong`
- report whether the strong prompt reduces deviation from `B_only`

### IFEval

For each condition:

- instruction-following pass rate
- mean instruction satisfaction fraction
- delta relative to `B_only`

For improvement:

- compare `default` vs `strong`
- report whether stronger switch instructions reduce the gap from `B_only`

## RQ2 Outputs

Recommended output structure:

- raw generations per run in `outputs/raw_generations/`
- scored run files in `outputs/scored/`
- summary tables in `outputs/tables/`
- one RQ2 report file that explicitly compares:
  - reusable default five-condition runs vs new strong five-condition runs
  - history vs summary
  - effects across all three datasets
  - only the persona pairs that were flagged as failed switches in `RQ1`

## RQ3 Goal

`RQ3` focuses only on persona pairs that were successful switches in `RQ1`.

The key variable is whether extra reinforcement of persona `A` before the final switch to `B` can weaken a switch that previously looked successful.

## RQ3 Experimental Design

### Reuse-first rule

`RQ3` should also reuse earlier results whenever possible.

The first reuse targets are:

- `B_only`
- simple `A -> B` switch conditions already produced in `RQ1`

These can serve as the baseline and simple-switch comparison when the same:

- model
- persona pair
- dataset
- sample IDs

are available.

Only the genuinely new reinforcement conditions should need additional execution.

### Reinforcement conditions

Recommended minimum set:

- `B_only`
- `A_to_B`
- `A_to_A_to_B`
- `A_to_A_to_A_to_B`

All conditions must end in the same final target persona `B`.

In practice:

- `B_only` should be reused from earlier runs whenever possible
- `A_to_B` should be mapped to the existing simple switch condition when possible
- only `A_to_A_to_B` and `A_to_A_to_A_to_B` necessarily require new execution if equivalent runs do not already exist

Current implementation-friendly condition names:

- history track
  - `A_history_to_B`
  - `A2_history_to_B`
  - `A3_history_to_B`
- summary track
  - `A_summary_to_B`
  - `A2_summary_to_B`
  - `A3_summary_to_B`

### Reinforcement interpretation

The preferred interpretation is:

- `A_to_B`
  - one standard `A` warm-up stage, then switch to `B`
- `A_to_A_to_B`
  - reinforce `A` twice before switching to `B`
- `A_to_A_to_A_to_B`
  - reinforce `A` three times before switching to `B`

This keeps the final target persona fixed and tests whether repeated reinforcement of `A` erodes a previously successful switch.

### Dataset coverage

`RQ3` should also cover all three datasets:

- MBTI multiple-choice
- Machine Mindset
- IFEval

Each dataset should reuse the same fixed prompt or sample IDs across all reinforcement levels.

## RQ3 Code Changes

### Config changes

Add new reinforcement-aware conditions in `configs/experiments.yaml`.

Recommended metadata fields:

- `reinforcement_persona: A`
- `reinforcement_repeats: 1 | 2 | 3`
- `retain_mechanism: history | summary | none`

### Execution changes

The current runner already supports warm-up before evaluation.
The smallest clean extension is to let a condition specify how many consecutive `A` reinforcement stages to run before the final switch to `B`.

This avoids designing a completely new execution stack.

### Warm-up generalization

The current runner supports one warm-up persona plus optional override.
`RQ3` needs a generalized reinforcement count such as:

- `1 x A`
- `2 x A`
- `3 x A`

The smallest clean extension is to allow a condition to specify repeated `A` reinforcement loops before the final switch.

The implemented config field should be:

- `reinforcement_repeats`

This field repeats the full warm-up prompt block before the final evaluation under persona `B`.

## RQ3 Metrics

### MBTI

For each reinforcement level:

- item-level agreement with `B_only`
- `OSR`
- `SCS`
- `RAI`

### Machine Mindset

For each reinforcement level:

- target-persona alignment
- agreement with `B_only`
- `RAI`-like residual influence

### IFEval

For each reinforcement level:

- strict pass rate
- loose pass rate when available
- mean instruction satisfaction fraction
- delta relative to `B_only`

### Interpretation

If stronger reinforcement of `A` causes the response to move farther away from `B_only`, that suggests the originally successful switch is fragile.

If `A_to_A_to_A_to_B` stays similar to `A_to_B`, that suggests the successful switch is robust even under additional `A` reinforcement.

## RQ3 Outputs

Recommended outputs:

- scored JSONL per reinforcement level
- summary CSV across reinforcement levels
- one compact RQ3 report that compares:
  - reusable simple-switch baselines vs newly added reinforced-`A` runs
  - `A_to_B` vs `A_to_A_to_B` vs `A_to_A_to_A_to_B`
  - all three datasets

## Recommended Implementation Order

1. Lock the user's refined RQ framing as the active project framing.
2. Finish `RQ2` first because it requires smaller changes than `RQ3`.
3. Reuse as many `RQ1` outputs as possible before launching any new runs.
4. Reuse the same dataset sampling and run-output conventions for both questions.
5. After `RQ2` is stable, extend the runner with repeated-`A` reinforcement conditions for `RQ3`.
6. Only after the reinforcement logic is correct, add the final RQ3 summaries.

Current status:

- `RQ2` execution and analysis layers are in place
- `RQ3` should now focus on the repeated-`A` conditions and the corresponding reuse-aware analysis step

## Known Prerequisites

Before actual execution:

- the required Python environment must be ready
- the selected model provider must be available
- Machine Mindset scoring must have access to the labeled reference bank used by the existing alignment scorer
- the sampled prompt files must remain fixed across compared conditions
- reusable prior-run outputs must be discoverable and consistent enough to compare against new runs

## Decision Points Before Running

Before execution begins, the following choices should be confirmed:

- which decision rule will classify failed vs successful switches in `RQ1`
- whether the available `RQ1` outputs are clean enough to serve as the reusable default side for `RQ2`
- whether `RQ3` should include both history-based and summary-based reinforcement variants
- whether the available earlier runs are clean enough to serve as the reusable simple-switch baselines for `RQ3`

## Script Naming Alignment

To better match the refined three-RQ structure without changing script contents, the script filenames should prefer task-oriented names instead of outdated RQ numbers.

Recommended renames:

- `scripts/analyze_rq23.py` -> `scripts/analyze_rq1_triplet_switch.py`
- `scripts/run_rq2_full.ps1` -> `scripts/run_machine_mindset_five_condition_grid.ps1`
- `scripts/summarize_ifeval_switch.py` -> `scripts/summarize_ifeval_five_condition_grid.py`

These renames improve discoverability while keeping the current file contents intact.
