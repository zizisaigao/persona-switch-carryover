from __future__ import annotations


def summarize_history(
    history_pairs: list[dict[str, str]],
    *,
    max_turns: int | None = None,
    max_chars_per_turn: int = 120,
) -> str:
    if not history_pairs:
        return "No prior interaction."

    clipped_turns = history_pairs if max_turns in (None, 0) else history_pairs[:max_turns]
    segments = []
    for index, pair in enumerate(clipped_turns, start=1):
        user_text = str(pair.get("user") or "").replace("\n", " ").strip()[:max_chars_per_turn]
        assistant_text = str(pair.get("assistant") or "").replace("\n", " ").strip()[:max_chars_per_turn]
        segments.append(f"Turn {index} user: {user_text} | assistant: {assistant_text}")
    return " ; ".join(segments)
