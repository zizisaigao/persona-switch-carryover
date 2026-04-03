# Persona Switching Research Pipeline

This repository is a lightweight Python experiment scaffold for studying persona carryover in LLM dialogue.

The core question is:
does a persona-conditioned prior interaction state continue to influence outputs after the active system prompt changes to a new persona?

This is not a study of hidden product memory or native persistent memory. It studies influence transmitted through:

- preserved multi-turn dialogue history
- compact memory summaries derived from prior interaction

## Conditions

- `A_only`: active system prompt is persona A, no prior history
- `B_only`: active system prompt is persona B, no prior history
- `A_history_to_B`: warm-up under persona A, then switch active system prompt to B while preserving the original A-stage dialogue history
- `A_summary_to_B`: warm-up under persona A, summarize the interaction into a compact memory block, discard the full history, then evaluate under active persona B

`A_history_to_B` and `A_summary_to_B` are intentionally different:

- `A_history_to_B` tests whether full conversational context carries persona influence forward
- `A_summary_to_B` tests whether a compressed memory representation is enough to preserve that influence

At evaluation time there is only one active system prompt. In the switch conditions, that active prompt is persona B. Persona A affects evaluation only through retained history or summary memory.

## Repository Layout

The project emphasizes:

- modular configs in YAML
- clear data schema
- isolated message construction
- pluggable model clients
- JSONL generation and usage logs
- mock mode, caching, and resumable runs

## Quick Start

1. Create an environment and install dependencies:

```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` if you plan to use a real API later.

3. Run the toy pipeline in mock mode:

```bash
python -m src.main --mock --condition A_summary_to_B --persona-a INTJ --persona-b ESFP
```

This runs end-to-end on `data/processed/samples_toy.csv` and writes JSONL outputs to `outputs/raw_generations/`.

## Dataset Inputs

The runner accepts either `.csv` or `.jsonl` sample files through `--samples-file`.

Supported formats:

- unified experiment rows with `sample_id`, `task_type`, `source_dataset`, `prompt_text`, `question_text`, `options_json`, `target_label`, `metadata_json`
- raw MBTI questionnaire CSV in the current `data/processed/mbti_questions.csv` format
- raw-ish `IFEval` JSONL/CSV rows with `prompt` or `instruction`, plus either `checks`, `instruction_id_list`, or `kwargs`
- raw-ish `Machine Mindset` JSONL/CSV rows with `question` plus `reference_answer`, `reference_answers`, or `expected_keywords`

Starter templates are included:

- `data/processed/ifeval_starter.jsonl`
- `data/processed/machine_mindset_starter.jsonl`

To download the full public datasets into `data/processed/`:

```bash
python scripts/download_public_datasets.py --dataset all
```

This writes:

- `data/processed/ifeval_full.parquet`
- `data/processed/machine_mindset_full.parquet`
- `data/processed/public_dataset_manifest.json`

Important note for `Machine Mindset`:

- the Hugging Face auto-converted parquet only preserves `instruction / input / output`
- it does **not** preserve the MBTI file-level labels encoded in the original JSON filenames
- for persona-aware analysis, rebuild the dataset from the original JSON files instead:

```bash
python scripts/download_machine_mindset_labeled.py --languages en
```

This writes:

- `data/processed/machine_mindset_labeled.parquet`
- `data/processed/machine_mindset_labeled_manifest.json`

The labeled parquet includes:

- `source_file`
- `source_group`
- `mbti_type`
- `mbti_dimension`
- `mbti_pole`
- `mbti_code`

To turn the labeled parquet into prompt-aligned evaluation sets:

```bash
python scripts/build_machine_mindset_eval_sets.py
```

This writes:

- `data/processed/machine_mindset_self_awareness_eval.jsonl`
- `data/processed/machine_mindset_dimension_eval.jsonl`

To score generated runs against the labeled MBTI reference bank:

```bash
python scripts/score_machine_mindset_alignment.py --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-4o-mini --eval-samples-file data/processed/machine_mindset_self_awareness_eval.jsonl
python scripts/score_machine_mindset_alignment.py --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-4o-mini --eval-samples-file data/processed/machine_mindset_dimension_eval.jsonl
```

The alignment scorer defaults to semantic `embedding` similarity using `distilbert-base-uncased`.
To fall back to lexical matching, pass:

```bash
python scripts/score_machine_mindset_alignment.py --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-4o-mini --eval-samples-file data/processed/machine_mindset_self_awareness_eval.jsonl --similarity-backend tfidf
```

These outputs report:

- self-awareness type match to the active persona
- dimension-pole match to the active persona
- agreement with `B_only`
- residual-A margin relative to the target persona
- when `--trials-per-sample` is used, summary rows are emitted per `trial_id`

Example runs:

```bash
python -m src.main --mock --condition B_only --persona-b INFJ --samples-file data/processed/ifeval_starter.jsonl
python -m src.main --mock --condition B_only --persona-b INTJ --samples-file data/processed/machine_mindset_starter.jsonl
python -m src.main --mock --condition B_only --persona-b INFJ --samples-file data/processed/ifeval_full.parquet
python -m src.main --mock --condition B_only --persona-b INTJ --samples-file data/processed/machine_mindset_full.parquet
```

## RQ2 / RQ3 Workflow

Current scope decision for the project report:

- `RQ1` remains the original MBTI override question and continues to use `data/processed/mbti_questions.csv`
- `RQ2` is now treated as an **open-ended task analysis**, using `Machine Mindset`
- `RQ3` is now treated as a **constrained instruction-following analysis**, using `IFEval`

This avoids forcing a single cross-task metric scale across open-ended and constrained tasks.

Recommended execution setup before real runs:

- reuse the existing `RQ1` MBTI results unless you explicitly want new model repeats
- sample `RQ2` and `RQ3` datasets into stable JSONL files first
- use `--model-name` to swap providers while keeping the same runner entrypoint
- use `--trials-per-sample` for repeat runs; downstream summaries are now `trial_id`-aware
- when `--trials-per-sample > 1`, the runner now disables request caching automatically so repeats stay independent

Create stable sampled files:

```bash
python scripts/sample_dataset.py --input-file data/processed/machine_mindset_self_awareness_eval.jsonl --output-file data/processed/machine_mindset_self_awareness_sample30.jsonl --sample-ids-output outputs/tables/machine_mindset_self_awareness_sample30_ids.csv --max-samples 30 --seed 42
python scripts/sample_dataset.py --input-file data/processed/ifeval_full.parquet --output-file data/processed/ifeval_sample30.jsonl --sample-ids-output outputs/tables/ifeval_sample30_ids.csv --max-samples 30 --seed 42
```

Run the five-condition `RQ2` design on the sampled `Machine Mindset` set:

```bash
python -m src.main --no-mock --no-resume --condition B_only --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-5.4 --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 30 --trials-per-sample 3
python -m src.main --no-mock --no-resume --condition A_history_to_B --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-5.4 --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 30 --trials-per-sample 3
python -m src.main --no-mock --no-resume --condition A_summary_to_B --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-5.4 --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 30 --trials-per-sample 3
python -m src.main --no-mock --no-resume --condition B_history_to_B --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-5.4 --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 30 --trials-per-sample 3
python -m src.main --no-mock --no-resume --condition B_summary_to_B --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-5.4 --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 30 --trials-per-sample 3
```

Score the sampled `Machine Mindset` runs:

```bash
python scripts/score_machine_mindset_alignment.py --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-5.4 --eval-samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
```

Run the same five-condition design for `RQ3` on sampled `IFEval`:

```bash
python -m src.main --no-mock --no-resume --condition B_only --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-5.4 --samples-file data/processed/ifeval_sample30.jsonl --max-samples 30 --trials-per-sample 3
python -m src.main --no-mock --no-resume --condition A_history_to_B --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-5.4 --samples-file data/processed/ifeval_sample30.jsonl --max-samples 30 --trials-per-sample 3
python -m src.main --no-mock --no-resume --condition A_summary_to_B --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-5.4 --samples-file data/processed/ifeval_sample30.jsonl --max-samples 30 --trials-per-sample 3
python -m src.main --no-mock --no-resume --condition B_history_to_B --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-5.4 --samples-file data/processed/ifeval_sample30.jsonl --max-samples 30 --trials-per-sample 3
python -m src.main --no-mock --no-resume --condition B_summary_to_B --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-5.4 --samples-file data/processed/ifeval_sample30.jsonl --max-samples 30 --trials-per-sample 3
```

Summarize the `IFEval` switch results:

```bash
python scripts/summarize_ifeval_switch.py --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-4o-mini --source-dataset ifeval
```

These scripts write:

- `outputs/tables/*_summary.csv`
- `outputs/tables/*_selected_runs.csv`
- `outputs/tables/*_scored.jsonl` for Machine Mindset alignment

Interpretation notes:

- `Machine Mindset`: `OSR` is target-type match, `SCS` is agreement with `B_only`, and `RAI < 0` means the switched run is still closer to target `B` than to persona `A`.
- `IFEval`: use official-checker-derived `strict_follow_all_rate`, `mean_strict_instruction_fraction`, and their deltas versus `B_only`.

Report-writing note:

- use `MBTI` results as the main evidence for `RQ1`
- use `Machine Mindset` results as the main evidence for the revised `RQ2`
- use `IFEval` results as the main evidence for the revised `RQ3`
- do not treat the current `Machine Mindset` and `IFEval` metrics as perfectly commensurable for a strong cross-task numerical comparison

### IFEval Metadata Rules

For `ifeval`, put rule definitions into `metadata_json.checks` or directly as top-level fields in JSONL/CSV rows.
When the dataset includes official `instruction_id_list` and `kwargs` fields, the pipeline uses the vendored Google `instruction_following_eval` checker automatically and reports both strict and loose results.

Supported checks:

- `required_substrings`
- `forbidden_substrings`
- `required_regexes`
- `forbidden_regexes`
- `response_must_start_with`
- `response_must_end_with`
- `exact_match`
- `bullet_count_equals`
- `line_count_equals`
- `word_count_equals`
- `min_word_count`
- `max_word_count`
- `sentence_count_equals`
- `min_sentences`
- `max_sentences`
- `must_be_json`

### Machine Mindset Scoring

For `machine_mindset`, scoring uses:

- `reference_answer` or `reference_answers` from metadata
- optional `expected_keywords`

The scorer reports overlap F1, precision, recall, Jaccard, keyword recall, and a single aggregate score.

## Switching to OpenRouter Later

1. Put your API key in `.env` as `OPENROUTER_API_KEY=...`
2. Update `configs/models.yaml` if needed
3. Run without `--mock`

Example:

```bash
python -m src.main --condition A_history_to_B --persona-a INFJ --persona-b ENTP
```

## What Exists Now

- runnable mock execution layer on toy data
- warm-up dialogue generation under persona A
- deterministic summary-memory placeholder
- OpenRouter client scaffold with retries
- request caching and API usage logging
- scoring skeleton modules with stable interfaces

## Near-Term Extensions

- replace toy samples with real task datasets
- add model-based summarization
- add richer automatic scoring and aggregation
- compare neutral warm-up summaries against persona-conditioned summaries
