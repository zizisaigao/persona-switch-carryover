# Final Run Workflow

## Clean Repo Layout

Legacy outputs, exploratory markdown files, deprecated scripts, toy datasets, starter datasets, and cache directories were moved into:

- `backup/pre_full_run_*`

The active repo now keeps only:

- required datasets under `data/processed`
- final configs under `configs`
- final code under `src`
- final analysis scripts and support utilities under grouped `scripts/*` subdirectories
- local NLTK resources under `outputs/nltk_data`

## Prerequisites

Run everything only after activating the project environment:

```powershell
conda activate mldl
Set-Location D:\GWHfiles\PythonScripts\ST5230Project\persona-switch-carryover
```

## Validate Gemini Access

```powershell
$env:GEMINI_API_KEY="YOUR_KEY"
python scripts/checks/check_gemini_api.py --json
```

## Datasets Used for the Full Run

- `data/processed/mbti_questions.csv`
- `data/processed/machine_mindset_self_awareness_sample30.jsonl`
- `data/processed/ifeval_sample30.jsonl`

`IFEval` is now official-checker-only. Any `ifeval` sample file used in the pipeline must provide:

- `instruction_id_list`
- `kwargs`

Legacy fallback-style `checks`-only schemas are no longer supported.

## Step 1: Build the 16-Type `MBTI_only` Premise Library

```powershell
$mbti = @(
  "INTJ","ESFP","INFJ","ENFJ",
  "ISFJ","ENTJ","ENTP","ESTP",
  "ISTP","ISFP","ENFP","ISTJ",
  "INTP","INFP","ESFJ","ESTJ"
)
foreach ($persona in $mbti) {
  python -m src.main --no-mock --model-config gemini_flash_lite --condition MBTI_only --persona-a $persona --persona-b $persona --samples-file data/processed/mbti_questions.csv
  python -m src.main --no-mock --model-config gemini_flash_lite --condition MBTI_only --persona-a $persona --persona-b $persona --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
  python -m src.main --no-mock --model-config gemini_flash_lite --condition MBTI_only --persona-a $persona --persona-b $persona --samples-file data/processed/ifeval_sample30.jsonl
}
```

This premise library is later mapped into:

- `A_only` by selecting the `MBTI_only` run whose target MBTI equals `A`
- `B_only` by selecting the `MBTI_only` run whose target MBTI equals `B`

## Step 2: Run RQ1 for One Pair

For a single pair such as `ENFJ -> ISTP`, run the following 12 commands:

```powershell
python -m src.main --no-mock --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv
python -m src.main --no-mock --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
python -m src.main --no-mock --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl

python -m src.main --no-mock --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv
python -m src.main --no-mock --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
python -m src.main --no-mock --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl

python -m src.main --no-mock --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv
python -m src.main --no-mock --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
python -m src.main --no-mock --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl

python -m src.main --no-mock --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv
python -m src.main --no-mock --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
python -m src.main --no-mock --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl
```

RQ1 is the only stage that runs on all `16 * 15 = 240` directed pairs.

## Step 3: Analyze RQ1 and Split Pairs

```powershell
python scripts/analysis/rq1_analyze_matched_switch.py --persona-a ENFJ --persona-b ISTP --model-name gemini-2.5-flash-lite --output-prefix rq1_enfj_to_istp_gemini_2_5_flash_lite
python scripts/analysis/rq1_route_pairs.py --summary-file outputs/tables/rq1_enfj_to_istp_gemini_2_5_flash_lite_summary.csv --output-prefix rq1_enfj_to_istp_gemini_2_5_flash_lite
```

For the full run, pair routing should use the `mbti_mcq` rows from the RQ1 summary:

- if `final_type_switch == target_persona_b`, route the `A -> B` row as `successful`
- otherwise, route the `A -> B` row as `failed`
- failed rows go to `RQ2`
- successful rows go to `RQ3`

## Step 4: Build the 16-Type `MBTI_only_strong` Premise Library

```powershell
$mbti = @(
  "INTJ","ESFP","INFJ","ENFJ",
  "ISFJ","ENTJ","ENTP","ESTP",
  "ISTP","ISFP","ENFP","ISTJ",
  "INTP","INFP","ESFJ","ESTJ"
)
foreach ($persona in $mbti) {
  python -m src.main --no-mock --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a $persona --persona-b $persona --samples-file data/processed/mbti_questions.csv
  python -m src.main --no-mock --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a $persona --persona-b $persona --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
  python -m src.main --no-mock --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a $persona --persona-b $persona --samples-file data/processed/ifeval_sample30.jsonl
}
```

This premise library is used only for RQ2. RQ3 reuses the original `MBTI_only` premise library from RQ1.

Within RQ2 analysis, this library is mapped into:

- `A_only_strong` by selecting the `MBTI_only_strong` run whose target MBTI equals `A`
- `B_only_strong` by selecting the `MBTI_only_strong` run whose target MBTI equals `B`

## Step 5: Run RQ2 for a Failed Pair

For a failed pair such as `ENFJ -> ISTP`, run:

```powershell
python -m src.main --no-mock --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv
python -m src.main --no-mock --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
python -m src.main --no-mock --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl

python -m src.main --no-mock --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv
python -m src.main --no-mock --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
python -m src.main --no-mock --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl

python -m src.main --no-mock --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv
python -m src.main --no-mock --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
python -m src.main --no-mock --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl

python -m src.main --no-mock --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv
python -m src.main --no-mock --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
python -m src.main --no-mock --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl
```

Then analyze with:

```powershell
python scripts/analysis/rq2_analyze_strong_update.py --persona-a ENFJ --persona-b ISTP --model-name gemini-2.5-flash-lite --classification-file outputs/tables/rq1_enfj_to_istp_gemini_2_5_flash_lite_overall.csv --required-overall-classification none --output-prefix rq2_enfj_to_istp_gemini_2_5_flash_lite
```

## Step 6: Run RQ3 for a Successful Pair

For a successful pair such as `ENFJ -> ISTP`, run:

```powershell
python -m src.main --no-mock --model-config gemini_flash_lite --condition A3_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv
python -m src.main --no-mock --model-config gemini_flash_lite --condition A3_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
python -m src.main --no-mock --model-config gemini_flash_lite --condition A3_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl

python -m src.main --no-mock --model-config gemini_flash_lite --condition B3_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv
python -m src.main --no-mock --model-config gemini_flash_lite --condition B3_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
python -m src.main --no-mock --model-config gemini_flash_lite --condition B3_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl

python -m src.main --no-mock --model-config gemini_flash_lite --condition A3_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv
python -m src.main --no-mock --model-config gemini_flash_lite --condition A3_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
python -m src.main --no-mock --model-config gemini_flash_lite --condition A3_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl

python -m src.main --no-mock --model-config gemini_flash_lite --condition B3_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv
python -m src.main --no-mock --model-config gemini_flash_lite --condition B3_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl
python -m src.main --no-mock --model-config gemini_flash_lite --condition B3_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl
```

Then analyze with:

```powershell
python scripts/analysis/rq3_analyze_warmup_reinforcement.py --persona-a ENFJ --persona-b ISTP --model-name gemini-2.5-flash-lite --classification-file outputs/tables/rq1_enfj_to_istp_gemini_2_5_flash_lite_overall.csv --required-overall-classification none --output-prefix rq3_enfj_to_istp_gemini_2_5_flash_lite
```

Machine Mindset reference-bank alignment is already computed inside `python -m src.main`, so no extra post-hoc alignment pass is required in the finalized pipeline.

## Step 7: Build Full-Run Report Tables

After all pair-level summaries have been generated, build the full-run report tables with:

```powershell
python scripts/analysis/rq1_build_full_report_tables.py --output-prefix rq1_full_run
python scripts/analysis/rq2_build_full_report_tables.py --output-prefix rq2_full_run
python scripts/analysis/rq3_build_full_report_tables.py --output-prefix rq3_full_run
```

These scripts generate:

- pair-level normalized report tables
- overall aggregate tables by task and retention mechanism
- short markdown summaries

## Resume Behavior

The pipeline keeps the default resumable behavior from `src.main`. If you want a fresh rerun without using existing raw outputs, add `--no-resume` to the `python -m src.main` commands.

## Output Locations

- raw generations: `outputs/raw_generations/generations.jsonl`
- usage log: `outputs/logs/api_usage.jsonl`
- scored per-run files: `outputs/scored`
  - these now include the finalized Machine Mindset reference-bank alignment metrics directly
- RQ summaries and reports: `outputs/tables/rq1_*`, `outputs/tables/rq2_*`, `outputs/tables/rq3_*`
