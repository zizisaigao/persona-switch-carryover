param(
    [string]$ModelConfig = "gemini_flash_lite",
    [string]$GeminiApiKey = ""
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$mbti = @(
    "INTJ","ESFP","INFJ","ENFJ",
    "ISFJ","ENTJ","ENTP","ESTP",
    "ISTP","ISFP","ENFP","ISTJ",
    "INTP","INFP","ESFJ","ESTJ"
)

$conditions = @(
    "A_history_to_B",
    "A_summary_to_B",
    "B_history_to_B",
    "B_summary_to_B"
)

$datasets = @(
    "data/processed/mbti_questions.csv",
    "data/processed/machine_mindset_self_awareness_sample30.jsonl",
    "data/processed/ifeval_sample30.jsonl"
)

$timestamp = Get-Date -Format "yyyyMMddTHHmmss"
$logDir = Join-Path $repoRoot "outputs/logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logPath = Join-Path $logDir "run_rq1_other_one_way_120_$timestamp.log"
$statusPath = Join-Path $logDir "run_rq1_other_one_way_120_$timestamp.status.txt"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Message
    $line | Tee-Object -FilePath $logPath -Append
}

function Invoke-PythonRun {
    param(
        [string]$Condition,
        [string]$PersonaA,
        [string]$PersonaB,
        [string]$Dataset
    )

    Write-Log "RUN $Condition | A=$PersonaA | B=$PersonaB | data=$Dataset"

    $pythonCmd = @(
        "python -B -m src.main",
        "--no-mock",
        "--no-resume",
        "--model-config $ModelConfig",
        "--condition $Condition",
        "--persona-a $PersonaA",
        "--persona-b $PersonaB",
        "--samples-file $Dataset",
        "--max-samples 9999"
    ) -join " "

    $command = "call D:\ProgramFiles\anaconda3\condabin\conda.bat activate mldl && cd /d $repoRoot && $pythonCmd"
    if ($GeminiApiKey) {
        $command = "set GEMINI_API_KEY=$GeminiApiKey && $command"
    }

    $stdoutPath = Join-Path $env:TEMP ("codex_rq1_stdout_" + [guid]::NewGuid().ToString("N") + ".log")
    $stderrPath = Join-Path $env:TEMP ("codex_rq1_stderr_" + [guid]::NewGuid().ToString("N") + ".log")
    try {
        $proc = Start-Process -FilePath cmd.exe -ArgumentList "/c", $command -WorkingDirectory $repoRoot -Wait -PassThru -NoNewWindow -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath
        if (Test-Path $stdoutPath) {
            Get-Content -Path $stdoutPath | Tee-Object -FilePath $logPath -Append | Out-Null
        }
        if (Test-Path $stderrPath) {
            Get-Content -Path $stderrPath | Tee-Object -FilePath $logPath -Append | Out-Null
        }
        if ($proc.ExitCode -ne 0) {
            throw "Command failed with exit code $($proc.ExitCode) for $Condition $PersonaA->$PersonaB $Dataset"
        }
    }
    finally {
        Remove-Item -LiteralPath $stdoutPath -ErrorAction SilentlyContinue
        Remove-Item -LiteralPath $stderrPath -ErrorAction SilentlyContinue
    }
}

"STARTED $(Get-Date -Format o)" | Set-Content -Path $statusPath
Write-Log "=== Stage: other one-way 120 RQ1 pairs ==="

$pairIndex = 0
for ($i = 0; $i -lt $mbti.Count; $i++) {
    for ($j = $i + 1; $j -lt $mbti.Count; $j++) {
        $personaA = $mbti[$j]
        $personaB = $mbti[$i]
        $pairIndex += 1
        Write-Log "PAIR $pairIndex/120 $personaA -> $personaB"
        foreach ($condition in $conditions) {
            foreach ($dataset in $datasets) {
                Invoke-PythonRun -Condition $condition -PersonaA $personaA -PersonaB $personaB -Dataset $dataset
            }
        }
    }
}

"COMPLETED $(Get-Date -Format o)" | Set-Content -Path $statusPath
Write-Log "=== COMPLETED other one-way 120 RQ1 pairs ==="
