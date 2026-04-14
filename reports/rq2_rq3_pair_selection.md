# RQ2 and RQ3 Pair Selection

This file records two deterministic downstream pair batches after applying the premise-library filter.

## Source Pools

The selection is based on:

- `reports/rq1_filtered_pair_groups.md`

Available pools:

- `Both Failed`: `16` pairs
- `Both Successful`: `26` pairs
- `Mixed`: `90` pairs

## Batch Layout

### Batch 1: already run

The first active batch was intentionally conservative:

- `RQ2 batch 1`: all `16` `Both Failed` pairs + first `14` `Mixed` pairs = `30`
- `RQ3 batch 1`: all `26` `Both Successful` pairs + next `4` `Mixed` pairs = `30`

This consumed `18` mixed pairs in total, leaving `72` mixed pairs still unused.

### Batch 2: mixed-only supplement

The second batch uses only the true remaining mixed pairs after removing every mixed pair already used in batch 1.

- `RQ2 batch 2`: first `36` remaining mixed pairs
- `RQ3 batch 2`: next `36` remaining mixed pairs

This yields:

- `RQ2 batch 2`: `36` pairs
- `RQ3 batch 2`: `36` pairs

## RQ2 Pair List

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

### RQ2 Total

- `30` pairs

## RQ3 Pair List

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

### RQ3 Total

- `30` pairs

## Batch 2 Pair Lists

### RQ2 Batch 2 `Mixed` Pairs (`36`)

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

### RQ3 Batch 2 `Mixed` Pairs (`36`)

- `ISTJ -> INFJ`
- `ISTJ -> ENFJ`
- `ISTJ -> ISFJ`
- `ISTJ -> ESFJ`
- `ISTJ -> ESTJ`
- `INFP -> INTJ`
- `INFP -> INFJ`
- `INFP -> ENFJ`
- `INFP -> ISFJ`
- `INFP -> ENTJ`
- `INFP -> ENTP`
- `INFP -> ISTP`
- `INFP -> ENFP`
- `INFP -> ISTJ`
- `INFP -> ESFJ`
- `INFP -> ESTJ`
- `ESFJ -> INTJ`
- `ESFJ -> INFJ`
- `ESFJ -> ENFJ`
- `ESFJ -> ISFJ`
- `ESFJ -> ENTJ`
- `ESFJ -> ENTP`
- `ESFJ -> ISTP`
- `ESFJ -> ENFP`
- `ESFJ -> ISTJ`
- `ESFJ -> INFP`
- `ESFJ -> ESTJ`
- `ESTJ -> INTJ`
- `ESTJ -> INFJ`
- `ESTJ -> ENFJ`
- `ESTJ -> ISFJ`
- `ESTJ -> ENTP`
- `ESTJ -> ISTP`
- `ESTJ -> ENFP`
- `ESTJ -> INFP`
- `ESTJ -> ESFJ`

## Overlap Check

The selections are disjoint by construction:

- batch 1 `RQ2` and batch 1 `RQ3` are disjoint
- batch 2 `RQ2` and batch 2 `RQ3` are disjoint
- batch 2 uses only mixed pairs not already used in batch 1
