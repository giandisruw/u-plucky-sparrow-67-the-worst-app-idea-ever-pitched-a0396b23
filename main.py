#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — entry program.

Writes one sentence (<= 240 chars, UTF-8, single line) to /output/entry.txt.
The line below is the winner of the local pairwise tournament
(tournament.py / tournament.jsonl): UmbrellaShare won 3 games on the
Caffeine router judge (the Verboo judge was down for the whole tournament —
every chat call returned HTTP 422, so its verdicts are recorded as 0.5/0.5
no-verdict splits and it contributed no wins). Final: UmbrellaShare beat
QueuePal 0.525–0.475.
Deterministic: no network, no randomness, no environment input.
"""

import os

ENTRY = (
    "UmbrellaShare: rents umbrellas to people already standing indoors, "
    "with surge pricing that activates the exact moment it stops raining."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry length {len(text)} outside 1-240"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
