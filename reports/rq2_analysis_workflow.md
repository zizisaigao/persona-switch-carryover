# RQ2 Analysis Workflow

## Goal

`RQ2` should only be analyzed for persona pairs that were classified as failed switches in `RQ1`.

The intended workflow is:

1. run or reuse `RQ1` default-condition outputs
2. summarize `RQ1`
3. classify the persona pair as failed or successful
4. run or reuse `RQ2` strong-condition outputs
5. compare reusable default runs against strong runs

## Scripts

### RQ1 summary

Use:

```powershell
conda activate mldl
python -B scripts/analyze_rq1_triplet_switch.py --persona-a ENFJ --persona-b ISTP --task-types mbti_mcq machine_mindset ifeval
```

This script produces:

- `*_summary.csv`
- `*_selected_runs.csv`
- `*_report.md`

### RQ1 pair classification

Use:

```powershell
conda activate mldl
python -B scripts/classify_rq1_pairs.py --summary-file outputs/tables/<rq1_summary>.csv
```

This script produces:

- `*_rows.csv`
- `*_overall.csv`

The row file classifies each task-row.
The overall file aggregates those row classifications into an overall failed or successful label per switch condition.

### RQ2 default-vs-strong comparison

Use:

```powershell
conda activate mldl
python -B scripts/analyze_rq2_strength.py --persona-a ENFJ --persona-b ISTP --classification-file outputs/tables/<rq1_classification_overall>.csv --required-overall-classification failed
```

This script compares:

- reusable default conditions
- newly generated strong conditions

and writes:

- `*_summary.csv`
- `*_selected_runs.csv`
- `*_report.md`

## Important Behavior

### Success-only filtering

`scripts/analyze_rq2_strength.py` filters scored rows against raw generation records whose status is `success`.

This prevents failed API calls or empty outputs from being silently counted as valid RQ2 evidence.

### Classification gating

If the classification file does not contain the requested overall label, the RQ2 analysis script stops intentionally.

Example:

- if the pair is classified as `successful`
- and `--required-overall-classification failed` is requested
- the script exits instead of producing an inappropriate RQ2 comparison

### Reuse assumptions

Default-side RQ1 runs should only be reused when they are compatible in:

- model
- persona pair
- dataset
- sample IDs
- condition semantics

## Recommended Output Interpretation

For MBTI:

- higher `OSR` is better
- higher `SCS` is better
- lower `RAI` gap is better

For Machine Mindset:

- higher target-facing task score is better
- higher lexical similarity to `B_only` is better
- lower residual `A` influence is better

For IFEval:

- higher pass-rate metrics are better
- smaller distance to `B_only` is better

The RQ2 script adds convenience columns such as:

- `improved_distance_to_b_only`
- `improved_osr`
- `reduced_a_influence`
- `rq2_improved`

These are heuristic decision helpers, not replacements for interpretation.
