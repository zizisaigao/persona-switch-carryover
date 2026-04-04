# RQ1 Run Status

## Audited Environment

- Activated environment for every Python command: `conda activate mldl`
- Verified interpreter:
  - `D:\ProgramFiles\anaconda3\envs\mldl\python.exe`
- Verified environment name:
  - `mldl`

## Commands Actually Executed During The Audit

### Repository acquisition

```powershell
git clone https://github.com/zizisaigao/persona-switch-carryover.git
```

### Environment verification

```powershell
conda activate mldl
python -c "import os,sys; print(sys.executable); print(sys.version); print(os.environ.get('CONDA_DEFAULT_ENV',''))"
```

### Main entrypoint verification

```powershell
conda activate mldl
python -m src.main --help
```

Observed result:

- Failed immediately with `ModuleNotFoundError: No module named 'dotenv'`

### Minimal import checks

```powershell
conda activate mldl
python -c "import pandas, yaml, requests, nltk, pyarrow; print('core_imports_ok')"
```

Observed result:

- Succeeded

### Dataset loader verification

```powershell
conda activate mldl
python -c "from pathlib import Path; from src.utils.io import load_samples; samples = load_samples(Path('data/processed/mbti_questions.csv')); print(len(samples)); print(samples[0].sample_id); print(samples[0].task_type); print(samples[0].metadata['option_dimensions'])"
```

Observed result:

- Succeeded
- Loaded 93 MBTI samples

### MBTI scoring verification

```powershell
conda activate mldl
python -c "from pathlib import Path; from src.utils.io import load_samples; from src.scoring.score_mbti import score_response, aggregate_profiles; samples = load_samples(Path('data/processed/mbti_questions.csv'))[:3]; records = [score_response(s, 'A. test') | {'task_type':'mbti_mcq','run_id':'demo','condition':'B_only','persona_a':'ENFJ','persona_b':'ISTP','model_name':'mock','trial_id':'trial_001'} for s in samples]; print(records[0]); print(aggregate_profiles(records))"
```

Observed result:

- Succeeded
- MBTI scoring and profile aggregation work independently of the CLI

### Direct runner-module trial validation

```powershell
conda activate mldl
python -c "<inline script calling src.runner.execute_trial for one MBTI sample under B_only>"
```

Observed result:

- Succeeded
- Returned `status=success`

```powershell
conda activate mldl
python -c "<inline script calling src.runner.execute_trial for one MBTI sample under A_history_to_B>"
```

Observed result:

- Succeeded
- Warm-up history length was `3`
- Returned `status=success`

### Minimal end-to-end MBTI mock batch validation

```powershell
conda activate mldl
python -c "<inline script calling src.runner.batch_run on 4 MBTI rows under B_only>"
```

Observed result:

- Succeeded
- Wrote:
  - `outputs/logs/audit_usage_log.jsonl`
  - `outputs/raw_generations/audit_generations.jsonl`
  - `outputs/scored/audit_b_only_scores.jsonl`

```powershell
conda activate mldl
python -c "<inline script calling src.runner.batch_run on 4 MBTI rows under A_history_to_B>"
```

Observed result:

- Succeeded
- Wrote:
  - `outputs/scored/audit_a_history_scores.jsonl`

### Machine Mindset alignment dependency check

```powershell
conda activate mldl
python -c "import torch, transformers; print(torch.__version__); print(transformers.__version__)"
```

Observed result:

- Failed with `ModuleNotFoundError: No module named 'transformers'`

## What Was Executed Versus Not Executed

### Executed

- Repository clone
- Static code audit
- Environment verification
- Dataset loader verification
- MBTI scoring verification
- Internal runner-module validation in mock mode for MBTI

### Not executed

- `python -m src.main` full CLI run
- Real model API run through OpenRouter
- Full RQ1 run across MBTI + Machine Mindset + IFEval
- Machine Mindset reference-bank alignment scoring
- Full IFEval dataset run

## Why Those Parts Were Not Executed

- CLI blocked by missing `python-dotenv` in `mldl`
- Machine Mindset alignment path additionally blocked by missing `transformers` and by missing `data/processed/machine_mindset_labeled.parquet`
- Full IFEval path blocked by missing `data/processed/ifeval_full.parquet`
- No `.env` file or API key was present for real OpenRouter execution

## Current Runnability Judgment

- Core internal modules: partially runnable
- Main CLI entrypoint: not runnable in the audited environment
- RQ1 MBTI-only mock validation: runnable through internal modules
- Requested full RQ1 evidence pipeline: not currently runnable end-to-end

