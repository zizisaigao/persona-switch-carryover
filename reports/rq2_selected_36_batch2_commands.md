# Explicit Commands: RQ2 Selected 36 Pairs Batch 2

## Environment

```powershell
conda activate mldl
Set-Location D:\GWHfiles\PythonScripts\ST5230Project\persona-switch-carryover
$env:GEMINI_API_KEY="YOUR_KEY"
```

## Notes

- This file follows `reports/rq2_rq3_pair_selection.md`.
- `RQ2 batch 2` uses only the remaining mixed pairs that were not used in the already completed `30`-pair batch 1.
- The batch runner filename still contains `selected_60` for backward compatibility.
- Use `--pair-batch 2` to switch the runner to the second pair plan.
- `RQ2` requires the corrected `MBTI_only_strong` premise library to be available first.

## Batch Command

Run only the `RQ2 batch 2` pair stage:

```powershell
python -B scripts/run_rq2_rq3_selected_60_batch.py --model-config gemini_flash_lite --pair-batch 2 --skip-rq2-premise --skip-rq3
```

If you need to rebuild the strong premise library first:

```powershell
python -B scripts/run_rq2_strong_premise_rerun_13.py --model-config gemini_flash_lite
python -B scripts/run_rq2_rq3_selected_60_batch.py --model-config gemini_flash_lite --pair-batch 2 --skip-rq2-premise --skip-rq3
```

## Selected Pairs

- `ENFJ -> ENTJ`
- `ENFJ -> ENTP`
- `ENFJ -> ISTP`
- `ENFJ -> ENFP`
- `ENFJ -> ISTJ`
- `ENFJ -> INFP`
- `ENFJ -> ESFJ`
- `ENFJ -> ESTJ`
- `ISFJ -> INTJ`
- `ISFJ -> INFJ`
- `ISFJ -> ENFJ`
- `ISFJ -> ENTJ`
- `ISFJ -> ISTJ`
- `ISFJ -> ESFJ`
- `ISFJ -> ESTJ`
- `ENTJ -> INTJ`
- `ENTJ -> INFJ`
- `ENTJ -> ENFJ`
- `ENTJ -> ISFJ`
- `ENTJ -> ENTP`
- `ENTJ -> ISTP`
- `ENTJ -> ENFP`
- `ENTJ -> ISTJ`
- `ENTJ -> INFP`
- `ENTJ -> ESFJ`
- `ENTP -> INTJ`
- `ENTP -> INFJ`
- `ENTP -> ENFP`
- `ENTP -> ISTJ`
- `ENTP -> INFP`
- `ENFP -> ISFJ`
- `ENFP -> ISTP`
- `ENFP -> ISTJ`
- `ENFP -> INFP`
- `ENFP -> ESFJ`
- `ENFP -> ESTJ`

## Total

- `36` pairs
- `36 * 4 conditions * 3 datasets = 432` specs
