param(
    [string]$ModelConfig = "gemini_flash_lite",
    [string]$GeminiApiKey = ""
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$rq2PremiseMbti = @(
    "INTJ","INFJ","ENFJ","ISFJ","ENTJ","ENTP",
    "ISTP","ENFP","ISTJ","INFP","ESFJ","ESTJ"
)

$rq2Pairs = @(
    @{ A="ISFJ"; B="ENTP" }, @{ A="ISFJ"; B="ISTP" }, @{ A="ISFJ"; B="ENFP" }, @{ A="ISFJ"; B="INFP" },
    @{ A="ENTP"; B="ENFJ" }, @{ A="ENTP"; B="ISFJ" }, @{ A="ENTP"; B="ENTJ" }, @{ A="ENTP"; B="ISTP" },
    @{ A="ENTP"; B="ESFJ" }, @{ A="ISTJ"; B="INTJ" }, @{ A="ISTJ"; B="ENTJ" }, @{ A="ISTJ"; B="ENTP" },
    @{ A="ISTJ"; B="ISTP" }, @{ A="ISTJ"; B="ENFP" }, @{ A="ISTJ"; B="INFP" }, @{ A="ESTJ"; B="ENTJ" },
    @{ A="INTJ"; B="INFJ" }, @{ A="INTJ"; B="ENFJ" }, @{ A="INTJ"; B="ISFJ" }, @{ A="INTJ"; B="ENTJ" },
    @{ A="INTJ"; B="ENTP" }, @{ A="INTJ"; B="ISTP" }, @{ A="INTJ"; B="ENFP" }, @{ A="INTJ"; B="INFP" },
    @{ A="INTJ"; B="ESFJ" }, @{ A="INTJ"; B="ESTJ" }, @{ A="INFJ"; B="INFP" }, @{ A="ENFJ"; B="INTJ" },
    @{ A="ENFJ"; B="INFJ" }, @{ A="ENFJ"; B="ISFJ" }, @{ A="ENFJ"; B="ENTJ" }, @{ A="ENFJ"; B="ENTP" },
    @{ A="ENFJ"; B="ISTP" }, @{ A="ENFJ"; B="ENFP" }, @{ A="ENFJ"; B="ISTJ" }, @{ A="ENFJ"; B="INFP" },
    @{ A="ENFJ"; B="ESFJ" }, @{ A="ENFJ"; B="ESTJ" }, @{ A="ISFJ"; B="INTJ" }, @{ A="ISFJ"; B="INFJ" },
    @{ A="ISFJ"; B="ENFJ" }, @{ A="ISFJ"; B="ENTJ" }, @{ A="ISFJ"; B="ISTJ" }, @{ A="ISFJ"; B="ESFJ" },
    @{ A="ISFJ"; B="ESTJ" }, @{ A="ENTJ"; B="INTJ" }, @{ A="ENTJ"; B="INFJ" }, @{ A="ENTJ"; B="ENFJ" },
    @{ A="ENTJ"; B="ISFJ" }, @{ A="ENTJ"; B="ENTP" }, @{ A="ENTJ"; B="ISTP" }, @{ A="ENTJ"; B="ENFP" },
    @{ A="ENTJ"; B="ISTJ" }, @{ A="ENTJ"; B="INFP" }, @{ A="ENTJ"; B="ESFJ" }, @{ A="ENTP"; B="INTJ" },
    @{ A="ENTP"; B="INFJ" }, @{ A="ENTP"; B="ENFP" }, @{ A="ENTP"; B="ISTJ" }, @{ A="ENTP"; B="INFP" }
)

$rq3Pairs = @(
    @{ A="INTJ"; B="ISTJ" }, @{ A="INFJ"; B="INTJ" }, @{ A="INFJ"; B="ENFJ" }, @{ A="INFJ"; B="ISFJ" },
    @{ A="INFJ"; B="ENTJ" }, @{ A="INFJ"; B="ENTP" }, @{ A="INFJ"; B="ISTP" }, @{ A="INFJ"; B="ENFP" },
    @{ A="INFJ"; B="ISTJ" }, @{ A="INFJ"; B="ESFJ" }, @{ A="INFJ"; B="ESTJ" }, @{ A="ENTJ"; B="ESTJ" },
    @{ A="ISTP"; B="INTJ" }, @{ A="ISTP"; B="INFJ" }, @{ A="ISTP"; B="ENFJ" }, @{ A="ISTP"; B="ISFJ" },
    @{ A="ISTP"; B="ENTP" }, @{ A="ISTP"; B="ENFP" }, @{ A="ISTP"; B="ISTJ" }, @{ A="ISTP"; B="INFP" },
    @{ A="ISTP"; B="ESFJ" }, @{ A="ISTP"; B="ESTJ" }, @{ A="ENFP"; B="INFJ" }, @{ A="ENFP"; B="ENTJ" },
    @{ A="ENFP"; B="ENTP" }, @{ A="ESTJ"; B="ISTJ" }, @{ A="ENTP"; B="ESTJ" }, @{ A="ISTP"; B="ENTJ" },
    @{ A="ENFP"; B="INTJ" }, @{ A="ENFP"; B="ENFJ" }, @{ A="ENFP"; B="ISFJ" }, @{ A="ENFP"; B="ISTP" },
    @{ A="ENFP"; B="ISTJ" }, @{ A="ENFP"; B="INFP" }, @{ A="ENFP"; B="ESFJ" }, @{ A="ENFP"; B="ESTJ" },
    @{ A="ISTJ"; B="INFJ" }, @{ A="ISTJ"; B="ENFJ" }, @{ A="ISTJ"; B="ISFJ" }, @{ A="ISTJ"; B="ESFJ" },
    @{ A="ISTJ"; B="ESTJ" }, @{ A="INFP"; B="INTJ" }, @{ A="INFP"; B="INFJ" }, @{ A="INFP"; B="ENFJ" },
    @{ A="INFP"; B="ISFJ" }, @{ A="INFP"; B="ENTJ" }, @{ A="INFP"; B="ENTP" }, @{ A="INFP"; B="ISTP" },
    @{ A="INFP"; B="ENFP" }, @{ A="INFP"; B="ISTJ" }, @{ A="INFP"; B="ESFJ" }, @{ A="INFP"; B="ESTJ" },
    @{ A="ESFJ"; B="INTJ" }, @{ A="ESFJ"; B="INFJ" }, @{ A="ESFJ"; B="ENFJ" }, @{ A="ESFJ"; B="ISFJ" },
    @{ A="ESFJ"; B="ENTJ" }, @{ A="ESFJ"; B="ENTP" }, @{ A="ESFJ"; B="ISTP" }, @{ A="ESFJ"; B="ENFP" }
)

$rq2Conditions = @(
    "A_history_to_B_strong",
    "A_summary_to_B_strong",
    "B_history_to_B_strong",
    "B_summary_to_B_strong"
)

$rq3Conditions = @(
    "A3_history_to_B",
    "A3_summary_to_B",
    "B3_history_to_B",
    "B3_summary_to_B"
)

$datasets = @(
    "data/processed/mbti_questions.csv",
    "data/processed/machine_mindset_self_awareness_sample30.jsonl",
    "data/processed/ifeval_sample30.jsonl"
)

$timestamp = Get-Date -Format "yyyyMMddTHHmmss"
$logDir = Join-Path $repoRoot "outputs/logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logPath = Join-Path $logDir "run_rq2_rq3_selected_60_$timestamp.log"
$statusPath = Join-Path $logDir "run_rq2_rq3_selected_60_$timestamp.status.txt"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Message
    $line | Tee-Object -FilePath $logPath -Append
}

function Resolve-GeminiKey {
    param([string]$ExplicitKey)

    if ($ExplicitKey) {
        return $ExplicitKey
    }

    if ($env:GEMINI_API_KEY) {
        return $env:GEMINI_API_KEY
    }

    $envPath = Join-Path $repoRoot ".env"
    if (Test-Path $envPath) {
        $line = Get-Content $envPath | Where-Object { $_ -match '^GEMINI_API_KEY=' } | Select-Object -First 1
        if ($line) {
            return ($line -replace '^GEMINI_API_KEY=', '').Trim()
        }
    }

    throw "GEMINI_API_KEY not found in parameter, environment, or .env"
}

function Invoke-PythonRun {
    param(
        [string]$Condition,
        [string]$PersonaA,
        [string]$PersonaB,
        [string]$Dataset,
        [string]$ResolvedGeminiKey
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

    $command = "set GEMINI_API_KEY=$ResolvedGeminiKey && call D:\ProgramFiles\anaconda3\condabin\conda.bat activate mldl && cd /d $repoRoot && $pythonCmd"

    $stdoutPath = Join-Path $env:TEMP ("codex_rq23_stdout_" + [guid]::NewGuid().ToString("N") + ".log")
    $stderrPath = Join-Path $env:TEMP ("codex_rq23_stderr_" + [guid]::NewGuid().ToString("N") + ".log")
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

$resolvedKey = Resolve-GeminiKey -ExplicitKey $GeminiApiKey
"STARTED $(Get-Date -Format o)" | Set-Content -Path $statusPath

Write-Log "=== Stage 1: RQ2 strong premise library ==="
foreach ($persona in $rq2PremiseMbti) {
    foreach ($dataset in $datasets) {
        Invoke-PythonRun -Condition "MBTI_only_strong" -PersonaA $persona -PersonaB $persona -Dataset $dataset -ResolvedGeminiKey $resolvedKey
    }
}

Write-Log "=== Stage 2: RQ2 selected 60 pairs ==="
$pairIndex = 0
foreach ($pair in $rq2Pairs) {
    $pairIndex += 1
    Write-Log "RQ2 PAIR $pairIndex/$($rq2Pairs.Count) $($pair.A) -> $($pair.B)"
    foreach ($condition in $rq2Conditions) {
        foreach ($dataset in $datasets) {
            Invoke-PythonRun -Condition $condition -PersonaA $pair.A -PersonaB $pair.B -Dataset $dataset -ResolvedGeminiKey $resolvedKey
        }
    }
}

Write-Log "=== Stage 3: RQ3 selected 60 pairs ==="
$pairIndex = 0
foreach ($pair in $rq3Pairs) {
    $pairIndex += 1
    Write-Log "RQ3 PAIR $pairIndex/$($rq3Pairs.Count) $($pair.A) -> $($pair.B)"
    foreach ($condition in $rq3Conditions) {
        foreach ($dataset in $datasets) {
            Invoke-PythonRun -Condition $condition -PersonaA $pair.A -PersonaB $pair.B -Dataset $dataset -ResolvedGeminiKey $resolvedKey
        }
    }
}

"COMPLETED $(Get-Date -Format o)" | Set-Content -Path $statusPath
Write-Log "=== COMPLETED RQ2 selected 60 + RQ3 selected 60 ==="
