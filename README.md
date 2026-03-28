# Persona Switching Research Pipeline

This repository is a lightweight Python experiment scaffold for studying persona carryover in LLM dialogue.

The core question is:
does a persona-conditioned prior interaction state continue to influence outputs after the active system prompt changes to a new persona?

This is not a study of hidden product memory or native persistent memory. It studies influence transmitted through:

- preserved multi-turn dialogue history
- compact memory summaries derived from prior interaction

## Conditions

- `A_only`: active system prompt is persona A, no prior history
- `B_only`: active system prompt is persona B, no prior history
- `A_history_to_B`: warm-up under persona A, then switch active system prompt to B while preserving the original A-stage dialogue history
- `A_summary_to_B`: warm-up under persona A, summarize the interaction into a compact memory block, discard the full history, then evaluate under active persona B

`A_history_to_B` and `A_summary_to_B` are intentionally different:

- `A_history_to_B` tests whether full conversational context carries persona influence forward
- `A_summary_to_B` tests whether a compressed memory representation is enough to preserve that influence

At evaluation time there is only one active system prompt. In the switch conditions, that active prompt is persona B. Persona A affects evaluation only through retained history or summary memory.

## Repository Layout

The project emphasizes:

- modular configs in YAML
- clear data schema
- isolated message construction
- pluggable model clients
- JSONL generation and usage logs
- mock mode, caching, and resumable runs

## Quick Start

1. Create an environment and install dependencies:

```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` if you plan to use a real API later.

3. Run the toy pipeline in mock mode:

```bash
python -m src.main --mock --condition A_summary_to_B --persona-a INTJ --persona-b ESFP
```

This runs end-to-end on `data/processed/samples_toy.csv` and writes JSONL outputs to `outputs/raw_generations/`.

## Switching to OpenRouter Later

1. Put your API key in `.env` as `OPENROUTER_API_KEY=...`
2. Update `configs/models.yaml` if needed
3. Run without `--mock`

Example:

```bash
python -m src.main --condition A_history_to_B --persona-a INFJ --persona-b ENTP
```

## What Exists Now

- runnable mock execution layer on toy data
- warm-up dialogue generation under persona A
- deterministic summary-memory placeholder
- OpenRouter client scaffold with retries
- request caching and API usage logging
- scoring skeleton modules with stable interfaces

## Near-Term Extensions

- replace toy samples with real task datasets
- add model-based summarization
- add richer automatic scoring and aggregation
- compare neutral warm-up summaries against persona-conditioned summaries
