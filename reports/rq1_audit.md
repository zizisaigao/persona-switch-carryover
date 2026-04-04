# RQ1 Audit

## Scope

This audit was limited to the repository as cloned into the required working directory and to the current Python environment `mldl`.
No RQ2 or RQ3 implementation work was started.

## Repository Summary

- Repository path: `D:\GWHfiles\PythonScripts\ST5230Project\persona-switch-carryover`
- Git branch: `main`
- Latest local commit at audit time: `cc994e8` (`Fix IFEval kwargs type normalization in scorer`)

## What Is Already Implemented

### Core experiment runner

- Main CLI entrypoint: `python -m src.main`
- Batch orchestration: `src/runner/batch_run.py`
- Single-trial execution: `src/runner/execute_trial.py`
- Message construction: `src/runner/build_messages.py`
- Warm-up dialogue generation: `src/runner/warmup.py`
- Summary-memory construction: `src/runner/summarize_memory.py`
- Model backends:
  - `src/models/mock_client.py`
  - `src/models/openrouter_client.py`
- Caching and usage logging:
  - `src/models/cache.py`
  - `outputs/cache/`
  - `outputs/logs/`

### Conditions implemented in config

From `configs/experiments.yaml`:

- `A_only`
- `B_only`
- `A_history_to_B`
- `A_summary_to_B`
- `B_history_to_B`
- `B_summary_to_B`
- `Neutral_summary_to_B`

The code path for these conditions is active in:

- `src/runner/execute_trial.py`
- `src/runner/build_messages.py`

### Dataset handling already wired up

Unified loader in `src/utils/io.py` supports:

- MBTI multiple-choice CSV
- Unified JSONL/CSV rows
- IFEval JSONL/CSV/Parquet-like rows
- Machine Mindset JSONL/CSV/Parquet-like rows

Available data files in the clone:

- Present:
  - `data/processed/mbti_questions.csv`
  - `data/processed/machine_mindset_self_awareness_eval.jsonl`
  - `data/processed/machine_mindset_self_awareness_sample30.jsonl`
  - `data/processed/machine_mindset_starter.jsonl`
  - `data/processed/ifeval_starter.jsonl`
  - `data/processed/samples_toy.csv`
  - `data/processed/public_dataset_manifest.json`
  - `data/processed/machine_mindset_labeled_manifest.json`
- Referenced by docs/manifests but not present in the clone:
  - `data/processed/ifeval_full.parquet`
  - `data/processed/machine_mindset_full.parquet`
  - `data/processed/machine_mindset_labeled.parquet`
  - `data/processed/machine_mindset_dimension_eval.jsonl`
  - `data/processed/ifeval_sample30.jsonl`

### Scoring already implemented

- MBTI item scoring and profile aggregation:
  - `src/scoring/score_mbti.py`
- Generic lexical overlap scorer used inside `src.main` for non-MBTI, non-IFEval tasks:
  - `src/scoring/score_similarity.py`
- IFEval scoring:
  - `src/scoring/score_ifeval.py`
  - supports both custom checks and vendored official Google IFEval checker when metadata is available
- Machine Mindset alignment scorer against labeled MBTI reference bank:
  - `src/scoring/machine_mindset_alignment.py`
  - wrapper script: `scripts/score_machine_mindset_alignment.py`

### Analysis / helper scripts already present

- `scripts/download_public_datasets.py`
- `scripts/download_machine_mindset_labeled.py`
- `scripts/build_machine_mindset_eval_sets.py`
- `scripts/sample_dataset.py`
- `scripts/score_machine_mindset_alignment.py`
- `scripts/summarize_ifeval_switch.py`
- `scripts/analyze_rq23.py`
- `scripts/run_rq2_full.ps1`

## How The Existing Project Frames The Research Questions

There is an important framing mismatch between the current repository and the target RQ definition in the task request.

### Repository's current internal framing

`RQ_UPDATE_2026-04-03.md` states:

- `RQ1` = MBTI-only analysis
- `RQ2` = Machine Mindset open-ended analysis
- `RQ3` = IFEval constrained instruction-following analysis

### Requested framing for this audit

The task request defines `RQ1` as requiring:

- MBTI multiple-choice
- Machine Mindset
- IFEval

under the same final persona `B`, comparing `B_only` vs `A -> B`, plus whether an analogous effect appears on a constrained instruction benchmark.

### Consequence

The repository is not currently organized around the requested RQ1 framing.
It contains useful building blocks for that framing, but the current docs and scripts split the evidence across different research questions.

## What Corresponds To RQ1

### Directly corresponding pieces

- `B_only`, `A_history_to_B`, and `A_summary_to_B` are implemented.
- MBTI questionnaire loading and profile aggregation are implemented.
- IFEval scoring logic is implemented.
- Machine Mindset generation and separate alignment scoring logic are implemented.

### Only partially corresponding pieces

- There is no single RQ1-specific orchestration or report script that combines:
  - MBTI
  - Machine Mindset
  - IFEval
  - shared `B_only` vs `A -> B` interpretation
- `scripts/analyze_rq23.py` contains MBTI-style `OSR`, `SCS`, and `RAI` logic, but it reflects an older framing and does not match the current repo note that moved Machine Mindset and IFEval out of RQ1.
- The main runner scores Machine Mindset with the generic lexical overlap scorer inside `src.main`, while the README recommends the separate reference-bank alignment scorer for serious Machine Mindset analysis.

## Incomplete, Inconsistent, Unused, Or Suspicious Areas

### Environment / dependency issues

- `python -m src.main` fails immediately in the audited `mldl` environment because `python-dotenv` is missing.
- `src/scoring/machine_mindset_alignment.py` imports `torch` and `transformers`, but these packages are not listed in `requirements.txt`.
- This means the published dependency file is not sufficient for every documented workflow.

### Data availability issues

- Several files documented in `README.md` and recorded in manifests are not actually present in the cloned repository.
- Machine Mindset alignment scoring needs `data/processed/machine_mindset_labeled.parquet`, but only the manifest is present.
- Full-scale IFEval analysis needs `data/processed/ifeval_full.parquet`, but only the starter JSONL is present.

### RQ framing inconsistency

- `README.md` and `RQ_UPDATE_2026-04-03.md` explicitly redefine the research-question scope so that Machine Mindset and IFEval are no longer part of `RQ1`.
- The task request for this audit uses a different RQ1 definition.

### Metric inconsistency

- MBTI metrics are partially implemented through:
  - profile aggregation in `src/scoring/score_mbti.py`
  - RQ-style summaries in `scripts/analyze_rq23.py`
- Machine Mindset has two scoring paths:
  - generic overlap scoring in `src.main`
  - reference-bank alignment scoring in `scripts/score_machine_mindset_alignment.py`
- IFEval has two scoring modes:
  - custom rule checks
  - official Google checker

This is workable, but not yet a single clean, unified RQ1 pipeline.

### Execution-style inconsistency with the task constraints

- Existing README and PowerShell examples use bare `python` and do not activate `conda activate mldl` first.
- `scripts/run_rq2_full.ps1` also launches bare `python`.
- Under the task constraints, these commands are not acceptable as-is.

### Mock-mode limitation

- Mock mode is useful for pipeline validation only.
- The mock client does not provide credible scientific evidence for RQ1.
- Mock outputs can verify that the runner, message construction, and scoring paths work mechanically, but not whether carry-over exists.

## RQ1 Status Judgment

Under the requested RQ1 definition, the repository is **not complete enough to answer RQ1**.

### Why it is not complete enough

- The current repo framing treats MBTI as RQ1 and moves Machine Mindset and IFEval into RQ2 and RQ3.
- No actual results are present in `outputs/`.
- The primary CLI entrypoint cannot run in the audited environment without installing at least `python-dotenv`.
- The Machine Mindset alignment scorer additionally needs missing packages and a missing labeled parquet file.
- The full IFEval dataset file is missing.
- Therefore there is not enough executable evidence in the repository, as audited, to support a defensible answer to the requested RQ1.

## Minimal Completion Path If RQ1 Must Be Finished Later

The smallest reasonable completion path would be:

1. Fix the environment so the documented runner can start in `mldl`.
2. Keep the existing condition machinery and reuse `B_only`, `A_history_to_B`, and optionally `A_summary_to_B`.
3. Reuse the existing MBTI runner and MBTI aggregation logic for the persona-task part.
4. Reuse the existing Machine Mindset eval JSONL generation path and the reference-bank alignment scorer, not the generic lexical fallback, for persona-sensitive open-ended analysis.
5. Reuse the IFEval scorer with the official checker when official metadata is available.
6. Add a thin RQ1-level summary layer that reports the requested metrics and explicitly compares `B_only` vs `A -> B`.

