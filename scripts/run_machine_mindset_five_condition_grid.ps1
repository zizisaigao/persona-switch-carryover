param(
    [string]$PersonaA = "ENFJ",
    [string]$PersonaB = "ISTP",
    [string]$EvalSamplesFile = "data/processed/machine_mindset_self_awareness_sample30.jsonl",
    [int]$MaxSamples = 30,
    [int]$TrialsPerSample = 3
)

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot

$Models = @(
    @{ Name = "openai/gpt-5.4"; Alias = "gpt54" },
    @{ Name = "anthropic/claude-opus-4.1"; Alias = "claude_opus_41" },
    @{ Name = "google/gemini-2.5-pro"; Alias = "gemini_25_pro" }
)

$Conditions = @(
    "B_only",
    "A_history_to_B",
    "A_summary_to_B",
    "B_history_to_B",
    "B_summary_to_B"
)

$LogDir = Join-Path $ProjectRoot "outputs/logs"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

function Invoke-LoggedPython {
    param(
        [string[]]$Arguments,
        [string]$StdoutPath,
        [string]$StderrPath
    )

    $process = Start-Process -FilePath "python" -ArgumentList $Arguments -WorkingDirectory $ProjectRoot -PassThru -Wait -NoNewWindow -RedirectStandardOutput $StdoutPath -RedirectStandardError $StderrPath
    if ($process.ExitCode -ne 0) {
        throw "Command failed with exit code $($process.ExitCode): python $($Arguments -join ' ')"
    }
}

foreach ($Model in $Models) {
    $ModelName = $Model.Name
    $ModelAlias = $Model.Alias
    $Timestamp = Get-Date -Format "yyyyMMddTHHmmss"
    $RunLog = Join-Path $LogDir ("rq2_full_{0}_{1}.log" -f $ModelAlias, $Timestamp)

    "Starting RQ2 full run for $ModelName at $(Get-Date -Format s)" | Tee-Object -FilePath $RunLog -Append
    foreach ($Condition in $Conditions) {
        $Arguments = @(
            "-m", "src.main",
            "--no-mock",
            "--no-resume",
            "--condition", $Condition,
            "--persona-a", $PersonaA,
            "--persona-b", $PersonaB,
            "--model-name", $ModelName,
            "--samples-file", $EvalSamplesFile,
            "--max-samples", $MaxSamples,
            "--trials-per-sample", $TrialsPerSample
        )

        $StdoutLog = Join-Path $LogDir ("rq2_full_{0}_{1}_{2}_stdout.log" -f $ModelAlias, $Condition, $Timestamp)
        $StderrLog = Join-Path $LogDir ("rq2_full_{0}_{1}_{2}_stderr.log" -f $ModelAlias, $Condition, $Timestamp)
        "Running: python $($Arguments -join ' ')" | Tee-Object -FilePath $RunLog -Append
        Invoke-LoggedPython -Arguments $Arguments -StdoutPath $StdoutLog -StderrPath $StderrLog
    }

    $OutputPrefix = "rq2_self_sample30_${ModelAlias}_${PersonaA}_to_${PersonaB}"
    $ScoreArguments = @(
        "scripts/score_machine_mindset_alignment.py",
        "--persona-a", $PersonaA,
        "--persona-b", $PersonaB,
        "--model-name", $ModelName,
        "--eval-samples-file", $EvalSamplesFile,
        "--output-prefix", $OutputPrefix
    )
    $ScoreStdoutLog = Join-Path $LogDir ("rq2_full_{0}_score_stdout_{1}.log" -f $ModelAlias, $Timestamp)
    $ScoreStderrLog = Join-Path $LogDir ("rq2_full_{0}_score_stderr_{1}.log" -f $ModelAlias, $Timestamp)
    "Scoring: python $($ScoreArguments -join ' ')" | Tee-Object -FilePath $RunLog -Append
    Invoke-LoggedPython -Arguments $ScoreArguments -StdoutPath $ScoreStdoutLog -StderrPath $ScoreStderrLog
    "Completed RQ2 full run for $ModelName at $(Get-Date -Format s)" | Tee-Object -FilePath $RunLog -Append
}
