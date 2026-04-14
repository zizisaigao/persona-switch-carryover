# Explicit Commands: RQ2 Selected 30 Pairs

## Environment

```powershell
conda activate mldl
Set-Location D:\GWHfiles\PythonScripts\ST5230Project\persona-switch-carryover
$env:GEMINI_API_KEY="YOUR_KEY"
```

## Notes

- This file follows `reports/rq2_rq3_pair_selection.md`.
- `RQ2` keeps all `16` `Both Failed` pairs and only the first `14` eligible `Mixed` pairs.
- The batch runner filename still contains `selected_60` for backward compatibility, but it now uses the reduced `30`-pair plan defined in `scripts/rq2_rq3_selected_60_plan.py`.
- `RQ2` requires the corrected `MBTI_only_strong` premise library to be available first.

## Batch Command

Run only the `RQ2` pair stage:

```powershell
python -B scripts/run_rq2_rq3_selected_60_batch.py --model-config gemini_flash_lite --skip-rq2-premise --skip-rq3
```

If you need to rebuild the strong premise library first:

```powershell
python -B scripts/run_rq2_strong_premise_rerun_13.py --model-config gemini_flash_lite
python -B scripts/run_rq2_rq3_selected_60_batch.py --model-config gemini_flash_lite --skip-rq2-premise --skip-rq3
```

## Selected Pairs

### Core `Both Failed` Pairs (`16`)

- `ISFJ -> ENTP`
- `ISFJ -> ISTP`
- `ISFJ -> ENFP`
- `ISFJ -> INFP`
- `ENTP -> ENFJ`
- `ENTP -> ISFJ`
- `ENTP -> ENTJ`
- `ENTP -> ISTP`
- `ENTP -> ESFJ`
- `ISTJ -> INTJ`
- `ISTJ -> ENTJ`
- `ISTJ -> ENTP`
- `ISTJ -> ISTP`
- `ISTJ -> ENFP`
- `ISTJ -> INFP`
- `ESTJ -> ENTJ`

### Additional `Mixed` Pairs (`14`)

- `INTJ -> INFJ`
- `INTJ -> ENFJ`
- `INTJ -> ISFJ`
- `INTJ -> ENTJ`
- `INTJ -> ENTP`
- `INTJ -> ISTP`
- `INTJ -> ENFP`
- `INTJ -> INFP`
- `INTJ -> ESFJ`
- `INTJ -> ESTJ`
- `INFJ -> INFP`
- `ENFJ -> INTJ`
- `ENFJ -> INFJ`
- `ENFJ -> ISFJ`

## Total

- `30` pairs
- `30 * 4 conditions * 3 datasets = 360` specs
