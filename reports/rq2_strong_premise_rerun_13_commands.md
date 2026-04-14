# RQ2 Strong Premise Rerun Commands for 13 MBTI Types

Excluded from rerun: `INTJ`, `INFJ`, `ENFJ`.

```powershell
conda activate mldl
Set-Location D:\GWHfiles\PythonScripts\ST5230Project\persona-switch-carryover
$env:GEMINI_API_KEY="<YOUR_GEMINI_API_KEY>"
```

## 1. MBTI_only_strong: ESFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESFP --persona-b ESFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESFP --persona-b ESFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESFP --persona-b ESFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## 2. MBTI_only_strong: ISFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISFJ --persona-b ISFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISFJ --persona-b ISFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISFJ --persona-b ISFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## 3. MBTI_only_strong: ENTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENTJ --persona-b ENTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENTJ --persona-b ENTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENTJ --persona-b ENTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## 4. MBTI_only_strong: ENTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENTP --persona-b ENTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENTP --persona-b ENTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENTP --persona-b ENTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## 5. MBTI_only_strong: ESTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESTP --persona-b ESTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESTP --persona-b ESTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESTP --persona-b ESTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## 6. MBTI_only_strong: ISTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISTP --persona-b ISTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISTP --persona-b ISTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISTP --persona-b ISTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## 7. MBTI_only_strong: ISFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISFP --persona-b ISFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISFP --persona-b ISFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISFP --persona-b ISFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## 8. MBTI_only_strong: ENFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENFP --persona-b ENFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENFP --persona-b ENFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ENFP --persona-b ENFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## 9. MBTI_only_strong: ISTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISTJ --persona-b ISTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISTJ --persona-b ISTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ISTJ --persona-b ISTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## 10. MBTI_only_strong: INTP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INTP --persona-b INTP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INTP --persona-b INTP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INTP --persona-b INTP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## 11. MBTI_only_strong: INFP

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INFP --persona-b INFP --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INFP --persona-b INFP --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a INFP --persona-b INFP --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## 12. MBTI_only_strong: ESFJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESFJ --persona-b ESFJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESFJ --persona-b ESFJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESFJ --persona-b ESFJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```

## 13. MBTI_only_strong: ESTJ

```powershell
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESTJ --persona-b ESTJ --samples-file data/processed/mbti_questions.csv --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESTJ --persona-b ESTJ --samples-file data/processed/machine_mindset_self_awareness_sample30.jsonl --max-samples 9999
python -B -m src.main --no-mock --no-resume --model-config gemini_flash_lite --condition MBTI_only_strong --persona-a ESTJ --persona-b ESTJ --samples-file data/processed/ifeval_sample30.jsonl --max-samples 9999
```
