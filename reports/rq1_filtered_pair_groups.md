# RQ1 Filtered Pair Groups

This file records the MBTI pair grouping used after applying the premise-library filter.

## Premise Filter

The following MBTI types did not fully match their own `MBTI_only` premise target and are therefore excluded from downstream pair grouping:

- `ESFP`
- `ESTP`
- `ISFP`
- `INTP`

Any pair is removed if either `A` or `B` belongs to the set above.

Remaining eligible directed pairs:

- `12 * 11 = 132`

## Both Failed

These are pairs for which both:

- `A_history_to_B`
- `A_summary_to_B`

failed to switch to final target `B`.

Count:

- `16`

Pairs:

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

## Both Successful

These are pairs for which both:

- `A_history_to_B`
- `A_summary_to_B`

successfully switched to final target `B`.

Count:

- `26`

Pairs:

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

## Mixed

These are the remaining eligible pairs for which one track succeeds and the other fails.

Count:

- `90`

Pairs:

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
- `ENTP -> ESTJ`
- `ISTP -> ENTJ`
- `ENFP -> INTJ`
- `ENFP -> ENFJ`
- `ENFP -> ISFJ`
- `ENFP -> ISTP`
- `ENFP -> ISTJ`
- `ENFP -> INFP`
- `ENFP -> ESFJ`
- `ENFP -> ESTJ`
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
