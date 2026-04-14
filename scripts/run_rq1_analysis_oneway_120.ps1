param(
    [string]$ModelName = "gemini-2.5-flash-lite",
    [string]$OutputPrefix = "rq1_oneway120_full_run"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $repoRoot

$mbti = @(
    "INTJ","ESFP","INFJ","ENFJ",
    "ISFJ","ENTJ","ENTP","ESTP",
    "ISTP","ISFP","ENFP","ISTJ",
    "INTP","INFP","ESFJ","ESTJ"
)

for ($i = 0; $i -lt $mbti.Count; $i++) {
    for ($j = $i + 1; $j -lt $mbti.Count; $j++) {
        $personaA = $mbti[$i]
        $personaB = $mbti[$j]
        $prefix = "rq1_{0}_to_{1}_gemini_flash_lite" -f $personaA.ToLower(), $personaB.ToLower()

        python -B scripts/analysis/rq1_analyze_matched_switch.py `
            --persona-a $personaA `
            --persona-b $personaB `
            --model-name $ModelName `
            --output-prefix $prefix
        if ($LASTEXITCODE -ne 0) {
            throw "rq1_analyze_matched_switch.py failed for $personaA -> $personaB"
        }

        python -B scripts/analysis/rq1_route_pairs.py `
            --summary-file ("outputs/tables/{0}_summary.csv" -f $prefix) `
            --output-prefix $prefix
        if ($LASTEXITCODE -ne 0) {
            throw "rq1_route_pairs.py failed for $personaA -> $personaB"
        }
    }
}

python -B scripts/analysis/rq1_build_full_report_tables.py --output-prefix $OutputPrefix
if ($LASTEXITCODE -ne 0) {
    throw "rq1_build_full_report_tables.py failed"
}
