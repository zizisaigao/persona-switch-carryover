param(
    [string]$ModelConfig = "gemini_flash_lite",
    [string]$GeminiApiKey = "",
    [switch]$SkipRq2Premise,
    [switch]$SkipRq2,
    [switch]$SkipRq3
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$timestamp = Get-Date -Format "yyyyMMddTHHmmss"
$logDir = Join-Path $repoRoot "outputs/logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logPath = Join-Path $logDir "run_rq2_rq3_selected_60_batch_$timestamp.log"
$statusPath = Join-Path $logDir "run_rq2_rq3_selected_60_batch_$timestamp.status.txt"
$stopFlagPath = Join-Path $logDir "stop_after_rq2_premise.flag"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Message
    $line | Tee-Object -FilePath $logPath -Append
}

"STARTED $(Get-Date -Format o)" | Set-Content -Path $statusPath
Write-Log "=== Starting single-process resumable RQ2/RQ3 batch runner ==="

if (Test-Path $stopFlagPath) {
    "SKIPPED $(Get-Date -Format o)" | Set-Content -Path $statusPath
    Write-Log "=== SKIPPED RQ2/RQ3 batch runner because stop_after_rq2_premise.flag exists ==="
    exit 0
}

$command = @(
    "call D:\ProgramFiles\anaconda3\condabin\conda.bat activate mldl",
    "cd /d $repoRoot",
    "set PYTHONDONTWRITEBYTECODE=1",
    $(if ($GeminiApiKey) { "set GEMINI_API_KEY=$GeminiApiKey" } else { "rem use existing GEMINI_API_KEY" }),
    ("python -B scripts\run_rq2_rq3_selected_60_batch.py --model-config $ModelConfig" +
        $(if ($SkipRq2Premise) { " --skip-rq2-premise" } else { "" }) +
        $(if ($SkipRq2) { " --skip-rq2" } else { "" }) +
        $(if ($SkipRq3) { " --skip-rq3" } else { "" }))
) -join " && "

$stdoutPath = Join-Path $env:TEMP ("codex_rq23_batch_stdout_" + [guid]::NewGuid().ToString("N") + ".log")
$stderrPath = Join-Path $env:TEMP ("codex_rq23_batch_stderr_" + [guid]::NewGuid().ToString("N") + ".log")
try {
    $proc = Start-Process -FilePath cmd.exe -ArgumentList "/c", $command -WorkingDirectory $repoRoot -Wait -PassThru -NoNewWindow -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath
    if (Test-Path $stdoutPath) {
        Get-Content -Path $stdoutPath | Tee-Object -FilePath $logPath -Append | Out-Null
    }
    if (Test-Path $stderrPath) {
        Get-Content -Path $stderrPath | Tee-Object -FilePath $logPath -Append | Out-Null
    }
    if ($proc.ExitCode -ne 0) {
        throw "Batch continuation failed with exit code $($proc.ExitCode)"
    }

    "COMPLETED $(Get-Date -Format o)" | Set-Content -Path $statusPath
    Write-Log "=== COMPLETED single-process resumable RQ2/RQ3 batch runner ==="
}
catch {
    "FAILED $(Get-Date -Format o)" | Set-Content -Path $statusPath
    Write-Log ("=== FAILED single-process resumable RQ2/RQ3 batch runner: {0} ===" -f $_.Exception.Message)
    throw
}
finally {
    Remove-Item -LiteralPath $stdoutPath -ErrorAction SilentlyContinue
    Remove-Item -LiteralPath $stderrPath -ErrorAction SilentlyContinue
}
