# How To Run

## Important Constraint For This Workspace

Use only the `mldl` conda environment.
Run `conda activate mldl` before every Python command and before every package installation.

## Main Entrypoint

The main experiment runner is:

```powershell
conda activate mldl
python -m src.main --condition B_only --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --mock
```

## Current Known Blockers

At audit time, the following blockers were observed in the `mldl` environment:

- Missing `python-dotenv` blocks `python -m src.main`
- Missing `transformers` blocks Machine Mindset alignment scoring
- `src/scoring/machine_mindset_alignment.py` also imports `torch`
- Missing data files block some documented commands:
  - `data/processed/ifeval_full.parquet`
  - `data/processed/machine_mindset_full.parquet`
  - `data/processed/machine_mindset_labeled.parquet`

## Existing Entry Points

### Runner

```powershell
conda activate mldl
python -m src.main --help
```

### Public dataset download

```powershell
conda activate mldl
python scripts/download_public_datasets.py --dataset all
```

### Machine Mindset labeled dataset reconstruction

```powershell
conda activate mldl
python scripts/download_machine_mindset_labeled.py --languages en
```

### Machine Mindset eval set build

```powershell
conda activate mldl
python scripts/build_machine_mindset_eval_sets.py
```

### Deterministic sampling

```powershell
conda activate mldl
python scripts/sample_dataset.py --input-file data/processed/machine_mindset_self_awareness_eval.jsonl --output-file data/processed/machine_mindset_self_awareness_sample30.jsonl --sample-ids-output outputs/tables/machine_mindset_self_awareness_sample30_ids.csv --max-samples 30 --seed 42
```

### Machine Mindset alignment scoring

```powershell
conda activate mldl
python scripts/score_machine_mindset_alignment.py --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-5.4 --eval-samples-file data/processed/machine_mindset_self_awareness_eval.jsonl
```

### IFEval summary

```powershell
conda activate mldl
python scripts/summarize_ifeval_switch.py --persona-a ENFJ --persona-b ISTP --model-name openai/gpt-4o-mini --source-dataset ifeval
```

## Recommended Order If Execution Is Resumed Later

1. Fix missing Python packages in `mldl`.
2. Confirm the required data files exist locally.
3. Run `python -m src.main` in mock mode on MBTI first.
4. Run the target real-data conditions for the chosen research question.
5. Run the corresponding downstream scorer and summarizer.

