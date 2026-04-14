# Explicit Commands: RQ2 Selected 60 Pairs

## Environment

```powershell
conda activate mldl
Set-Location D:\GWHfiles\PythonScripts\ST5230Project\persona-switch-carryover
$env:GEMINI_API_KEY="YOUR_KEY"
```

## Notes

- This file follows the pair selection in `reports/rq2_rq3_pair_selection.md`.
- `RQ2` requires the strong premise library `MBTI_only_strong` before pair-level runs.

## Stage 0: MBTI_only_strong Premise Library

### MBTI_only_strong: INTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INTJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INTJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INTJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only_strong: INFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INFJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INFJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INFJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only_strong: ENFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENFJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENFJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENFJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only_strong: ISFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only_strong: ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only_strong: ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENTP --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENTP --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENTP --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only_strong: ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only_strong: ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENFP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENFP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENFP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only_strong: ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only_strong: INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only_strong: ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only_strong: ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## Stage 1: Pair-Level RQ2 Runs

### Pair 1 of 60: ISFJ -> ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 2 of 60: ISFJ -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 3 of 60: ISFJ -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 4 of 60: ISFJ -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 5 of 60: ENTP -> ENFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 6 of 60: ENTP -> ISFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 7 of 60: ENTP -> ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 8 of 60: ENTP -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 9 of 60: ENTP -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 10 of 60: ISTJ -> INTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 11 of 60: ISTJ -> ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 12 of 60: ISTJ -> ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 13 of 60: ISTJ -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 14 of 60: ISTJ -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 15 of 60: ISTJ -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 16 of 60: ESTJ -> ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ESTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ESTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ESTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ESTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ESTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ESTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ESTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ESTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ESTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ESTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ESTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ESTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 17 of 60: INTJ -> INFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 18 of 60: INTJ -> ENFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 19 of 60: INTJ -> ISFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 20 of 60: INTJ -> ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 21 of 60: INTJ -> ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 22 of 60: INTJ -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 23 of 60: INTJ -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 24 of 60: INTJ -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 25 of 60: INTJ -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 26 of 60: INTJ -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 27 of 60: INFJ -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a INFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a INFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a INFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a INFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 28 of 60: ENFJ -> INTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 29 of 60: ENFJ -> INFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 30 of 60: ENFJ -> ISFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 31 of 60: ENFJ -> ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 32 of 60: ENFJ -> ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 33 of 60: ENFJ -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 34 of 60: ENFJ -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 35 of 60: ENFJ -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 36 of 60: ENFJ -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 37 of 60: ENFJ -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 38 of 60: ENFJ -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 39 of 60: ISFJ -> INTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 40 of 60: ISFJ -> INFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 41 of 60: ISFJ -> ENFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 42 of 60: ISFJ -> ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 43 of 60: ISFJ -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 44 of 60: ISFJ -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 45 of 60: ISFJ -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 46 of 60: ENTJ -> INTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 47 of 60: ENTJ -> INFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 48 of 60: ENTJ -> ENFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 49 of 60: ENTJ -> ISFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 50 of 60: ENTJ -> ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 51 of 60: ENTJ -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 52 of 60: ENTJ -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 53 of 60: ENTJ -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 54 of 60: ENTJ -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 55 of 60: ENTJ -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 56 of 60: ENTP -> INTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 57 of 60: ENTP -> INFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 58 of 60: ENTP -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 59 of 60: ENTP -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 60 of 60: ENTP -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B_strong --persona-a ENTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B_strong --persona-a ENTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B_strong --persona-a ENTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B_strong --persona-a ENTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

