# Project Status Summary

Last updated: 2026-04-12

This document summarizes the current project state based on the latest corrected setup. It intentionally reflects only the final agreed workflow and the latest valid progress, not earlier intermediate or superseded states.

## 1. Final Experiment Design

### 1.1 Core datasets

All formal runs use:

- `MBTI multiple-choice`: `data/processed/mbti_questions.csv`
- `Machine Mindset sample30`: `data/processed/machine_mindset_self_awareness_sample30.jsonl`
- `IFEval sample30`: `data/processed/ifeval_sample30.jsonl`

Formal per-condition sample sizes are:

- `MBTI = 93`
- `Machine Mindset = 30`
- `IFEval = 30`

### 1.2 Premise libraries

Two premise libraries are used:

- `MBTI_only`
- `MBTI_only_strong`

These are premise/reference runs only. They are not the main comparison axis.

`A_only`, `B_only`, `A_only_strong`, and `B_only_strong` are analysis-side mapped references derived from these libraries. They are not separate run conditions.

### 1.3 RQ1 / RQ2 / RQ3 logic

`RQ1`

- main comparisons:
  - `A_history_to_B` vs `B_history_to_B`
  - `A_summary_to_B` vs `B_summary_to_B`

`RQ2`

- main comparisons:
  - `A_history_to_B_strong` vs `B_history_to_B_strong`
  - `A_summary_to_B_strong` vs `B_summary_to_B_strong`
- interpretation:
  - compare default matched gap vs strong matched gap

`RQ3`

- only `3-turn` baseline vs `9-turn` reinforcement
- main comparisons:
  - `A3_history_to_B` vs `B3_history_to_B`
  - `A3_summary_to_B` vs `B3_summary_to_B`

### 1.4 Scoring routes

`MBTI`

- scorer: `src/scoring/score_mbti.py`

`Machine Mindset`

- scorer: `src/scoring/score_machine_mindset.py`
- route: `reference-bank alignment + embedding ranking`
- default embedding model: `sentence-transformers/all-MiniLM-L6-v2`
- old lexical scorer has been removed from the active mainline

`IFEval`

- scorer: `src/scoring/score_ifeval.py`
- route: official checker only
- fallback rule-based route has been removed

## 2. Repository / Code State

### 2.1 Important code and docs already aligned

Key files already updated to the latest design:

- `README.md`
- `reports/final_run_workflow.md`
- `reports/final_experiment_scheme.md`
- `reports/metric_and_comparison_guide.md`
- `reports/metric_formulas_and_rationale.md`
- `src/main.py`
- `src/scoring/score_machine_mindset.py`
- `src/scoring/score_ifeval.py`
- `src/utils/io.py`
- `scripts/analysis/rq1_analyze_matched_switch.py`
- `scripts/analysis/rq1_route_pairs.py`
- `scripts/analysis/rq2_analyze_strong_update.py`
- `scripts/analysis/rq3_analyze_warmup_reinforcement.py`

### 2.2 Batch runner fixes

The critical sample-size bug for `RQ2/RQ3` has been fixed.

Files updated:

- `src/runner/batch_run.py`
- `configs/experiments.yaml`
- `scripts/run_rq2_strong_premise_rerun_13.py`
- `scripts/run_rq2_rq3_selected_60_batch.py`

Final fix details:

- `batch_run.py` now supports `max_samples_override`
- `experiments.yaml` now uses:
  - `budget.max_samples_per_run: 9999`
- batch scripts explicitly override per dataset:
  - `MBTI = 93`
  - `Machine Mindset = 30`
  - `IFEval = 30`

This means the formal batch pipeline now really runs `93 + 30 + 30`, not `10 + 10 + 10`.

### 2.3 Recovery / cleanup utilities added

Added:

- `scripts/rq2_rq3_selected_60_plan.py`
- `scripts/cleanup_invalid_rq2_rq3_runs.py`
- `scripts/run_rq2_strong_premise_rerun_13.py`
- `scripts/run_rq2_strong_premise_rerun_13.ps1`
- `scripts/run_rq2_rq3_recovery.ps1`

These support:

- reusable pair/premise plan constants
- precise cleanup of invalid partial `RQ2/RQ3` records
- single-process strong-premise reruns
- single-process `RQ2/RQ3` reruns with model reuse

## 3. Completed Results

### 3.1 RQ1 completed

`RQ1` has been completed for all `240` directed pairs.

Both one-way 120-pair batches are complete.

Representative outputs include:

- `outputs/tables/rq1_oneway120_full_run_overall_by_task_track.csv`
- `outputs/tables/rq1_oneway120_full_run_pair_routing.csv`
- `outputs/tables/rq1_oneway120_full_run_report.md`

### 3.2 RQ1 premise (`MBTI_only`)

`RQ1` premise library is valid and clean on `MBTI mcq`.

All 16 MBTI personas:

- are parseable
- aggregate to valid four-letter profiles

Results:

- `12 / 16` exact self-match
- `4 / 16` one-letter-off

Those four are:

- `ESFP -> ENFP`
- `ESTP -> ENTP`
- `ISFP -> INFP`
- `INTP -> INTJ`

### 3.3 RQ1 filtered pair groups

After removing any pair containing the 4 premise-inconsistent MBTI types above, the retained pool has:

- `132` directed pairs

Group counts:

- `Both Failed`: `16`
- `Both Successful`: `26`
- `Mixed`: `90`

Reference file:

- `reports/rq1_filtered_pair_groups.md`

## 4. RQ2 / RQ3 Pair Selection

Batch 1 non-overlapping selection:

`RQ2 batch 1`

- `16` both-failed pairs
- `14` mixed pairs
- total `30`

`RQ3 batch 1`

- `26` both-successful pairs
- `4` mixed pairs
- total `30`

Batch 2 mixed-only supplement:

`RQ2 batch 2`

- `36` remaining mixed pairs

`RQ3 batch 2`

- `36` remaining mixed pairs

There is no overlap:

- between `RQ2` and `RQ3` inside batch 1
- between `RQ2` and `RQ3` inside batch 2
- between batch 1 mixed pairs and batch 2 mixed pairs

Reference files:

- `reports/rq2_rq3_pair_selection.md`
- `reports/rq2_selected_30_commands.md`
- `reports/rq3_selected_30_commands.md`
- `reports/rq2_selected_36_batch2_commands.md`
- `reports/rq3_selected_36_batch2_commands.md`
- `reports/rq2_selected_60_commands.md`
- `reports/rq3_selected_60_commands.md`

The `selected_60` filenames are legacy files. The new `selected_30` files are the active command references.

This selection has been revalidated against `RQ1` grouping and is correct in the latest setup.

## 5. Invalid RQ2 / RQ3 Runs Already Removed

Earlier `RQ2/RQ3` attempts were invalid because they were accidentally truncated to `10 + 10 + 10`.

Those invalid records have been cleaned from the active formal path using:

- `scripts/cleanup_invalid_rq2_rq3_runs.py`

Latest cleanup actions removed:

- the previous incorrect `RQ2/RQ3` run set
- the later partial failed `13`-persona strong-premise rerun

After cleanup, those invalid partial runs are no longer meant to be used for formal analysis.

## 6. Current Active Run

### 6.1 What is running now

The current active run is:

- `RQ2 strong premise rerun for 13 MBTI types`

Important instruction:

- after strong premise finishes, stop
- do **not** automatically continue into `RQ2 pair` or `RQ3 pair`

This behavior has already been enforced by stopping the outer recovery controller while leaving the inner strong-premise runner alive.

### 6.2 Why this run is important

The previous `RQ2 strong premise` outputs were problematic for two different reasons:

1. some earlier attempts were truncated to `10` samples
2. some strong MBTI premise runs produced `XXXX` because MBTI answer labels were not parseable

The current rerun is the first one on the corrected `93 + 30 + 30` pipeline, so this is the run that should be used going forward.

### 6.3 Latest confirmed runtime status

At the latest confirmed checkpoint:

- the run is active
- raw generations and usage logs are updating
- the run has already produced correct-sized outputs such as:
  - `93` MBTI items
  - `30` Machine Mindset items
  - `30` IFEval items

Examples already verified:

- `ESFP`
  - `MBTI_only_strong`
  - `MBTI = 93`
  - `Machine Mindset = 30`
  - `IFEval = 30`
- `ISFJ`
  - `MBTI = 93`
  - `Machine Mindset = 30`
  - `IFEval` in progress or continuing at the last checked point

### 6.4 Latest confirmed qualitative strong-premise result behavior

The corrected rerun is already showing that:

- the sample-size bug is fixed
- MBTI parseability is much better than the bad `10-sample` partial runs

Examples:

- `ESFP` strong premise currently aggregates to `ENFP`
- `ISFJ` strong premise currently aggregates to `ISFJ`

Interpretation:

- the pipeline is now producing credible results
- exact self-match is still persona-dependent
- this is now a model behavior question, not a sample-size or pipeline corruption issue

## 7. Current Process / Monitoring

The active process is the inner strong-premise runner, not the outer recovery wrapper.

You may not see a visible PowerShell window because the launcher uses hidden/background startup.

Progress should be tracked through the progress files instead of a visible console window.

Main live monitoring files:

- `outputs/logs/run_rq2_strong_premise_rerun_13_progress_latest.log`
- `outputs/logs/run_rq2_strong_premise_rerun_13_progress_latest.status.txt`

Current session-specific progress file:

- `outputs/logs/run_rq2_strong_premise_rerun_13_progress_20260412T214717.log`
- `outputs/logs/run_rq2_strong_premise_rerun_13_progress_20260412T214717.status.txt`

## 8. Model Loading / Performance Status

Repeated per-spec model loading is no longer the intended execution pattern.

Current behavior:

- `Machine Mindset` scoring uses `sentence-transformers/all-MiniLM-L6-v2`
- scorer class keeps a process-local singleton cache
- strong-premise rerun and corrected `RQ2/RQ3` are designed as single-process runners

This means:

- model loading is reused within each long-lived Python process
- it is no longer reloaded once per pair-condition-dataset spec

In practice:

- one large phase = one Python process
- not one model reload per spec

## 9. Next Steps

### Immediate next step

Let the current `13`-persona strong premise rerun finish.

### After strong premise completes

Do **not** automatically start `RQ2 pair` or `RQ3 pair`.

Instead:

1. review the full corrected strong-premise result table
2. confirm whether the strong prompt is acceptable as-is for `RQ2`
3. then launch:
   - corrected formal `RQ2 pair`
   - corrected formal `RQ3 pair`

### Important current truth

At this moment:

- `RQ1` is complete and usable
- `RQ2/RQ3` pair-level formal reruns have **not yet** been completed on the corrected pipeline
- the current active formal task is only the corrected `13`-persona `RQ2 strong premise` rerun
