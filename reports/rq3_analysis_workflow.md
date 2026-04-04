# RQ3 Analysis Workflow

## Goal

`RQ3` tests whether persona pairs that looked like successful switches in `RQ1` become weaker after extra reinforcement of persona `A` before the final switch to persona `B`.

The intended comparison is:

- reuse `B_only` from `RQ1` when compatible
- reuse the simple switch from `RQ1`
- run only the new reinforced-`A` conditions

## Condition Mapping

History-retention track:

- `B_only`
- `A_history_to_B`
- `A2_history_to_B`
- `A3_history_to_B`

Summary-retention track:

- `B_only`
- `A_summary_to_B`
- `A2_summary_to_B`
- `A3_summary_to_B`

Optional reference condition for `RAI`-style comparisons:

- `A_only`

## Reuse Rule

If earlier runs already exist and match in:

- model
- persona pair
- dataset
- sample IDs

then `RQ3` should reuse:

- `B_only`
- `A_history_to_B`
- `A_summary_to_B`

Only these new conditions are necessarily added:

- `A2_history_to_B`
- `A3_history_to_B`
- `A2_summary_to_B`
- `A3_summary_to_B`

## Execution Rule

The runner now supports `reinforcement_repeats` in `configs/experiments.yaml`.

Interpretation:

- `A_history_to_B` or `A_summary_to_B`
  - one warm-up block in persona `A`
- `A2_*_to_B`
  - two consecutive warm-up blocks in persona `A`
- `A3_*_to_B`
  - three consecutive warm-up blocks in persona `A`

The final evaluated persona remains `B` in every condition.

## RQ1 Classification Dependency

`RQ3` should only analyze switch tracks that were classified as `successful` in `RQ1`.

Recommended workflow:

1. summarize `RQ1`
2. classify `RQ1` switch conditions with `scripts/classify_rq1_pairs.py`
3. pass the resulting `*_overall.csv` file into `scripts/analyze_rq3_reinforcement.py`

The script filters tracks separately:

- `A_history_to_B` controls whether the history track is eligible
- `A_summary_to_B` controls whether the summary track is eligible

## Suggested Commands

Run one new reinforced condition:

```powershell
conda activate mldl
python -m src.main `
  --condition A2_history_to_B `
  --persona-a ENFJ `
  --persona-b ISTP `
  --model-name openai/gpt-4o-mini `
  --samples-file data/processed/ifeval_starter.jsonl
```

Analyze reusable simple-switch runs plus new reinforced runs:

```powershell
conda activate mldl
python scripts/analyze_rq3_reinforcement.py `
  --persona-a ENFJ `
  --persona-b ISTP `
  --model-name openai/gpt-4o-mini `
  --classification-file outputs/tables/<rq1_classification_overall.csv>
```

## Output Files

The analysis script writes:

- `outputs/tables/<prefix>_summary.csv`
- `outputs/tables/<prefix>_selected_runs.csv`
- `outputs/tables/<prefix>_report.md`

## Interpretation

For MBTI:

- weaker switch means lower `OSR`
- weaker switch means lower `SCS` to `B_only`
- weaker switch means larger `RAI` gap toward `A_only`

For Machine Mindset:

- weaker switch means lower target-task score
- weaker switch means lower lexical agreement with `B_only`
- weaker switch means larger lexical residual influence from `A_only`

For IFEval:

- weaker switch means lower primary instruction-following metric
- weaker switch means larger distance from `B_only`
- weaker switch may also appear as higher lexical similarity to `A_only`
