# Explicit Commands: RQ3 Selected 36 Pairs Batch 2

## Environment

```powershell
conda activate mldl
Set-Location D:\GWHfiles\PythonScripts\ST5230Project\persona-switch-carryover
$env:GEMINI_API_KEY="YOUR_KEY"
```

## Notes

- This file follows `reports/rq2_rq3_pair_selection.md`.
- `RQ3 batch 2` uses only the remaining mixed pairs that were not used in the already completed `30`-pair batch 1.
- The batch runner filename still contains `selected_60` for backward compatibility.
- Use `--pair-batch 2` to switch the runner to the second pair plan.
- `RQ3` reuses the `MBTI_only` premise library from `RQ1`; no new premise stage is required.

## Batch Command

Run only the `RQ3 batch 2` pair stage:

```powershell
python -B scripts/run_rq2_rq3_selected_60_batch.py --model-config gemini_flash_lite --pair-batch 2 --skip-rq2-premise --skip-rq2
```

## Selected Pairs

- `ISTJ -> INFJ`
- `ISTJ -> ENFJ`
- `ISTJ -> ISFJ`
- `ISTJ -> ESFJ`
- `ISTJ -> ESTJ`
- `INFP -> INTJ`
- `INFP -> INFJ`
- `INFP -> ENFJ`
- `INFP -> ISFJ`
- `INFP -> ENTJ`
- `INFP -> ENTP`
- `INFP -> ISTP`
- `INFP -> ENFP`
- `INFP -> ISTJ`
- `INFP -> ESFJ`
- `INFP -> ESTJ`
- `ESFJ -> INTJ`
- `ESFJ -> INFJ`
- `ESFJ -> ENFJ`
- `ESFJ -> ISFJ`
- `ESFJ -> ENTJ`
- `ESFJ -> ENTP`
- `ESFJ -> ISTP`
- `ESFJ -> ENFP`
- `ESFJ -> ISTJ`
- `ESFJ -> INFP`
- `ESFJ -> ESTJ`
- `ESTJ -> INTJ`
- `ESTJ -> INFJ`
- `ESTJ -> ENFJ`
- `ESTJ -> ISFJ`
- `ESTJ -> ENTP`
- `ESTJ -> ISTP`
- `ESTJ -> ENFP`
- `ESTJ -> INFP`
- `ESTJ -> ESFJ`

## Total

- `36` pairs
- `36 * 4 conditions * 3 datasets = 432` specs
