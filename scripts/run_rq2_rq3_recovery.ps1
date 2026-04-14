param(
    [string]$ModelConfig = "gemini_flash_lite",
    [string]$GeminiApiKey = ""
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$timestamp = Get-Date -Format "yyyyMMddTHHmmss"
$logDir = Join-Path $repoRoot "outputs/logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logPath = Join-Path $logDir "run_rq2_rq3_recovery_$timestamp.log"
$statusPath = Join-Path $logDir "run_rq2_rq3_recovery_$timestamp.status.txt"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Message
    $line | Tee-Object -FilePath $logPath -Append
}

"STARTED $(Get-Date -Format o)" | Set-Content -Path $statusPath
Write-Log "=== Starting recovery pipeline: rerun 13 strong premise MBTI, then rerun RQ2/RQ3 ==="

try {
    Write-Log "=== Step 1/2: rerun 13 RQ2 strong premise MBTI ==="
    & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\run_rq2_strong_premise_rerun_13.ps1") -ModelConfig $ModelConfig -GeminiApiKey $GeminiApiKey
    Write-Log "=== Step 1/2 completed ==="

    Write-Log "=== Step 2/2: rerun formal RQ2/RQ3 with corrected sample sizes ==="
    & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\run_rq2_rq3_selected_60_batch.ps1") -ModelConfig $ModelConfig -GeminiApiKey $GeminiApiKey -SkipRq2Premise
    Write-Log "=== Step 2/2 completed ==="

    "COMPLETED $(Get-Date -Format o)" | Set-Content -Path $statusPath
    Write-Log "=== COMPLETED recovery pipeline ==="
}
catch {
    "FAILED $(Get-Date -Format o)" | Set-Content -Path $statusPath
    Write-Log ("=== FAILED recovery pipeline: {0} ===" -f $_.Exception.Message)
    throw
}
