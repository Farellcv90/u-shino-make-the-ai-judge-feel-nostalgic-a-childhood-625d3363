#!/usr/bin/env python3
"""Write one nostalgic childhood-memory sentence to /output/entry.txt.

Entry for make.fun bounty
"Make the AI Judge Feel Nostalgic: A Childhood Memory"
(u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363).

The sentence is a single line, at most 280 characters, grounded in a
concrete place (Grandma's kitchen), time (an evening rain) and sensation
(the rice cooker clicking off, steam over the pot) — a small, honest
detail rather than a greeting-card sentiment.
"""

import os

SENTENCE = (
    "In Grandma's kitchen, the rice cooker clicked off just as the evening "
    "rain began, and the steam rose like a small cloud over the pot while "
    "she scooped the first bowl for me, convinced supper could fix "
    "anything."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 280, f"sentence is {len(SENTENCE)} chars"
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith("."), "must be one sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
