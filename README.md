# Persona Switching Research Pipeline

This repository studies whether earlier persona context continues to shape model behavior after the active system prompt has been updated to a new target persona.

The finalized study uses three task families:

- closed-form multiple-choice personality items
- open-ended persona-related prompts
- constrained instruction-following prompts

The main inferential comparison is always a matched switch-versus-control contrast:

- switch condition: `A -> B`
- matched control: `B -> B`

Premise runs are retained only to verify that the model can express a requested MBTI target in the absence of switching interference.

## Final Research Design

### Premise Libraries

The pipeline uses two library-style premise conditions:

- `MBTI_only`
- `MBTI_only_strong`

These conditions are run once for all `16` MBTI types. They are not pair-specific. During analysis:

- `A_only` is recovered by selecting the `MBTI_only` run whose target persona equals `A`
- `B_only` is recovered by selecting the `MBTI_only` run whose target persona equals `B`
- `A_only_strong` is recovered from `MBTI_only_strong`
- `B_only_strong` is recovered from `MBTI_only_strong`

### RQ1

RQ1 asks whether earlier persona context affects final behavior under the same target persona `B`.

Matched comparisons:

- `A_history_to_B` vs `B_history_to_B`
- `A_summary_to_B` vs `B_summary_to_B`

### RQ2

RQ2 asks whether a stronger and more explicit final update to persona `B` attenuates the switching effect.

Pair-level conditions:

- `A_history_to_B_strong`
- `A_summary_to_B_strong`
- `B_history_to_B_strong`
- `B_summary_to_B_strong`

### RQ3

RQ3 asks whether stronger pre-switch reinforcement of persona `A` amplifies the switching effect.

Simple versus reinforced comparisons:

- `A_history_to_B` vs `B_history_to_B`
- `A_summary_to_B` vs `B_summary_to_B`
- `A3_history_to_B` vs `B3_history_to_B`
- `A3_summary_to_B` vs `B3_summary_to_B`

## Warmup Design

The base warmup contains three turns:

1. `How do you usually approach a difficult long-term goal?`
2. `What matters more when making a decision: logic, relationships, or momentum?`
3. `Describe how you would advise someone who feels stuck.`

For `A3_*` and `B3_*`, the warmup expands to three distinct blocks rather than repeating the same block verbatim.

Turn counts:

- simple switch conditions: `3` warmup turns
- `A3_*` and `B3_*`: `9` warmup turns

Summary-track conditions summarize all executed warmup turns rather than truncating after the first block.

## Datasets

The active full-run datasets are:

- `data/processed/mbti_questions.csv`
- `data/processed/machine_mindset_self_awareness_sample30.jsonl`
- `data/processed/ifeval_sample30.jsonl`

Supporting processed resources include:

- `data/processed/machine_mindset_labeled.parquet`
- `data/processed/machine_mindset_self_awareness_eval.jsonl`
- `data/processed/machine_mindset_dimension_eval.jsonl`
- `data/processed/ifeval_full.parquet`

## Machine Mindset Scoring

Machine Mindset now uses the reference-bank alignment scorer directly inside the main experiment runner rather than through a separate post-hoc scoring pass.

- main implementation: `src/scoring/score_machine_mindset.py`
- runner integration: `src/main.py`
- method: semantic embedding similarity followed by reference-bank ranking
- default embedding model: `sentence-transformers/all-MiniLM-L6-v2`

The runner compares each generated answer against prompt-matched labeled references and writes the resulting target-alignment and residual-influence metrics directly into the normal per-run scored files under `outputs/scored`.

## Repository Layout

- `configs/`: finalized experiment, model, persona, and task configs
- `data/processed/`: active processed datasets used in the full run
- `reports/`: finalized workflow and metric documentation
- `scripts/analysis/`: pair-level analysis and full-run report-table builders
- `scripts/checks/`: environment and API validation utilities
- `scripts/data/`: dataset download and evaluation-set preparation utilities
- `src/`: runner, scoring, model clients, analysis helpers, and utilities

## Environment

Run project commands only after activating the project environment:

```powershell
conda activate mldl
Set-Location D:\GWHfiles\PythonScripts\ST5230Project\persona-switch-carryover
```

Install dependencies inside that environment with:

```powershell
pip install -r requirements.txt
```

## Quick Checks

Validate Gemini access:

```powershell
$env:GEMINI_API_KEY="YOUR_KEY"
python scripts/checks/check_gemini_api.py --json
```

Build the Machine Mindset evaluation sets if needed:

```powershell
python scripts/data/build_machine_mindset_eval_sets.py
```

## Analysis And Reporting

The analysis layer is organized around three pair-level scripts:

- `scripts/analysis/rq1_analyze_matched_switch.py`
- `scripts/analysis/rq2_analyze_strong_update.py`
- `scripts/analysis/rq3_analyze_warmup_reinforcement.py`

Pair routing from `RQ1` into `RQ2` or `RQ3` is handled by:

- `scripts/analysis/rq1_route_pairs.py`

Full-run report tables are built by:

- `scripts/analysis/rq1_build_full_report_tables.py`
- `scripts/analysis/rq2_build_full_report_tables.py`
- `scripts/analysis/rq3_build_full_report_tables.py`

## Metric Logic

All three research questions use the same comparison structure:

1. a target-oriented task outcome
2. consistency with the matched `B -> B` control
3. residual pull toward the `A` premise

Task-specific surface metrics differ:

- `MBTI`: `OSR`, matched-control `SCS`, and `RAI`
- `Machine Mindset`: target similarity, matched-control `SCS`, and residual `A` margin
- `IFEval`: instruction-following primary metric, lexical matched-control `SCS`, and lexical `RAI`

The detailed definitions are documented in:

- `reports/metric_and_comparison_guide.md`

## Full-Run Workflow

The recommended execution order is:

1. build the `MBTI_only` premise library for all `16` MBTI targets
2. run `RQ1` for all `16 * 15 = 240` directed `A -> B` pairs
3. route pairs using `MBTI` final-type switching only
4. build the `MBTI_only_strong` premise library
5. run `RQ2` on routed failed-switch rows
6. run `RQ3` on routed successful-switch rows
7. build the full-run report tables

The operational details and command templates are documented in:

- `reports/final_run_workflow.md`
- `reports/final_experiment_scheme.md`

## Notes

- `RQ1` is the only stage that runs on every directed pair.
- `RQ2` and `RQ3` both reuse premise-library references rather than rerunning `A_only` or `B_only`.
- `Machine Mindset` and `IFEval` both use the `sample30` evaluation sets in the finalized full run.
- The vendored `instruction_following_eval` package is the only supported `IFEval` scoring route in the finalized pipeline.
