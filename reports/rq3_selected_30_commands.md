# Explicit Commands: RQ3 Selected 30 Pairs

## Environment

```powershell
conda activate mldl
Set-Location D:\GWHfiles\PythonScripts\ST5230Project\persona-switch-carryover
$env:GEMINI_API_KEY="YOUR_KEY"
```

## Notes

- This file follows `reports/rq2_rq3_pair_selection.md`.
- `RQ3` keeps all `26` `Both Successful` pairs and only the next `4` eligible `Mixed` pairs.
- The batch runner filename still contains `selected_60` for backward compatibility, but it now uses the reduced `30`-pair plan defined in `scripts/rq2_rq3_selected_60_plan.py`.
- `RQ3` reuses the `MBTI_only` premise library from `RQ1`; no new premise stage is required.

## Batch Command

Run only the `RQ3` pair stage:

```powershell
python -B scripts/run_rq2_rq3_selected_60_batch.py --model-config gemini_flash_lite --skip-rq2-premise --skip-rq2
```

## Selected Pairs

### Core `Both Successful` Pairs (`26`)

- `INTJ -> ISTJ`
- `INFJ -> INTJ`
- `INFJ -> ENFJ`
- `INFJ -> ISFJ`
- `INFJ -> ENTJ`
- `INFJ -> ENTP`
- `INFJ -> ISTP`
- `INFJ -> ENFP`
- `INFJ -> ISTJ`
- `INFJ -> ESFJ`
- `INFJ -> ESTJ`
- `ENTJ -> ESTJ`
- `ISTP -> INTJ`
- `ISTP -> INFJ`
- `ISTP -> ENFJ`
- `ISTP -> ISFJ`
- `ISTP -> ENTP`
- `ISTP -> ENFP`
- `ISTP -> ISTJ`
- `ISTP -> INFP`
- `ISTP -> ESFJ`
- `ISTP -> ESTJ`
- `ENFP -> INFJ`
- `ENFP -> ENTJ`
- `ENFP -> ENTP`
- `ESTJ -> ISTJ`

### Additional `Mixed` Pairs (`4`)

- `ENTP -> ESTJ`
- `ISTP -> ENTJ`
- `ENFP -> INTJ`
- `ENFP -> ENFJ`

## Total

- `30` pairs
- `30 * 4 conditions * 3 datasets = 360` specs
