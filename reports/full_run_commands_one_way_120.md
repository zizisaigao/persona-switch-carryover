# Full Run Commands: 16-Type MBTI_only + 120 One-Way RQ1 Pairs

## Environment

```powershell
conda activate mldl
Set-Location D:\GWHfiles\PythonScripts\ST5230Project\persona-switch-carryover
$env:GEMINI_API_KEY="YOUR_KEY"
```

## MBTI Order

```text
INTJ, ESFP, INFJ, ENFJ, ISFJ, ENTJ, ENTP, ESTP, ISTP, ISFP, ENFP, ISTJ, INTP, INFP, ESFJ, ESTJ
```

## Stage 1: 16-Type MBTI_only Premise Library

Each MBTI type is run on all three datasets.

### MBTI_only: INTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a INTJ --persona-b INTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a INTJ --persona-b INTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a INTJ --persona-b INTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: ESFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ESFP --persona-b ESFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ESFP --persona-b ESFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ESFP --persona-b ESFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: INFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a INFJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a INFJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a INFJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: ENFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ENFJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ENFJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ENFJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: ISFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ISFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ISFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ISFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ENTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ENTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ENTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ENTP --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ENTP --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ENTP --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: ESTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ESTP --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ESTP --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ESTP --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ISTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ISTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ISTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: ISFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ISFP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ISFP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ISFP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ENFP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ENFP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ENFP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ISTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ISTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ISTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a INTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a INTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a INTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a INFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a INFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a INFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ESFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ESFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ESFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### MBTI_only: ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ESTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ESTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only --persona-a ESTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## Stage 2: RQ1 for 120 One-Way Pairs

One-way means: for the fixed MBTI order above, only pairs with earlier index -> later index are run.

### Pair 1 of 120: INTJ -> ESFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ESFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ESFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ESFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ESFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ESFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ESFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ESFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ESFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ESFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ESFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ESFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ESFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 2 of 120: INTJ -> INFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 3 of 120: INTJ -> ENFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 4 of 120: INTJ -> ISFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 5 of 120: INTJ -> ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 6 of 120: INTJ -> ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 7 of 120: INTJ -> ESTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 8 of 120: INTJ -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 9 of 120: INTJ -> ISFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 10 of 120: INTJ -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 11 of 120: INTJ -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 12 of 120: INTJ -> INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 13 of 120: INTJ -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 14 of 120: INTJ -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 15 of 120: INTJ -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 16 of 120: ESFP -> INFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b INFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b INFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b INFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 17 of 120: ESFP -> ENFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 18 of 120: ESFP -> ISFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 19 of 120: ESFP -> ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 20 of 120: ESFP -> ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 21 of 120: ESFP -> ESTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 22 of 120: ESFP -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 23 of 120: ESFP -> ISFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 24 of 120: ESFP -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 25 of 120: ESFP -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 26 of 120: ESFP -> INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 27 of 120: ESFP -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 28 of 120: ESFP -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 29 of 120: ESFP -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 30 of 120: INFJ -> ENFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ENFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ENFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ENFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 31 of 120: INFJ -> ISFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 32 of 120: INFJ -> ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 33 of 120: INFJ -> ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 34 of 120: INFJ -> ESTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 35 of 120: INFJ -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 36 of 120: INFJ -> ISFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 37 of 120: INFJ -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 38 of 120: INFJ -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 39 of 120: INFJ -> INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 40 of 120: INFJ -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 41 of 120: INFJ -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 42 of 120: INFJ -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 43 of 120: ENFJ -> ISFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 44 of 120: ENFJ -> ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 45 of 120: ENFJ -> ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 46 of 120: ENFJ -> ESTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 47 of 120: ENFJ -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 48 of 120: ENFJ -> ISFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 49 of 120: ENFJ -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 50 of 120: ENFJ -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 51 of 120: ENFJ -> INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 52 of 120: ENFJ -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 53 of 120: ENFJ -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 54 of 120: ENFJ -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 55 of 120: ISFJ -> ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 56 of 120: ISFJ -> ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 57 of 120: ISFJ -> ESTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 58 of 120: ISFJ -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 59 of 120: ISFJ -> ISFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 60 of 120: ISFJ -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 61 of 120: ISFJ -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 62 of 120: ISFJ -> INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 63 of 120: ISFJ -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 64 of 120: ISFJ -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 65 of 120: ISFJ -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 66 of 120: ENTJ -> ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 67 of 120: ENTJ -> ESTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 68 of 120: ENTJ -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 69 of 120: ENTJ -> ISFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 70 of 120: ENTJ -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 71 of 120: ENTJ -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 72 of 120: ENTJ -> INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 73 of 120: ENTJ -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 74 of 120: ENTJ -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 75 of 120: ENTJ -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 76 of 120: ENTP -> ESTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 77 of 120: ENTP -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 78 of 120: ENTP -> ISFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 79 of 120: ENTP -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 80 of 120: ENTP -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 81 of 120: ENTP -> INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 82 of 120: ENTP -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 83 of 120: ENTP -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 84 of 120: ENTP -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 85 of 120: ESTP -> ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 86 of 120: ESTP -> ISFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 87 of 120: ESTP -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 88 of 120: ESTP -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 89 of 120: ESTP -> INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 90 of 120: ESTP -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 91 of 120: ESTP -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 92 of 120: ESTP -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 93 of 120: ISTP -> ISFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 94 of 120: ISTP -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 95 of 120: ISTP -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 96 of 120: ISTP -> INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 97 of 120: ISTP -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 98 of 120: ISTP -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 99 of 120: ISTP -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 100 of 120: ISFP -> ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 101 of 120: ISFP -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 102 of 120: ISFP -> INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 103 of 120: ISFP -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 104 of 120: ISFP -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 105 of 120: ISFP -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 106 of 120: ENFP -> ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 107 of 120: ENFP -> INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 108 of 120: ENFP -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 109 of 120: ENFP -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 110 of 120: ENFP -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ENFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ENFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ENFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ENFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 111 of 120: ISTJ -> INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTJ --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTJ --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTJ --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 112 of 120: ISTJ -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTJ --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTJ --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTJ --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 113 of 120: ISTJ -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 114 of 120: ISTJ -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ISTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ISTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ISTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ISTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 115 of 120: INTP -> INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 116 of 120: INTP -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 117 of 120: INTP -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INTP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 118 of 120: INFP -> ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFP --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFP --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFP --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 119 of 120: INFP -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a INFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a INFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a INFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFP --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFP --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a INFP --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

### Pair 120 of 120: ESFJ -> ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_history_to_B --persona-a ESFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition A_summary_to_B --persona-a ESFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_history_to_B --persona-a ESFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition B_summary_to_B --persona-a ESFJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

