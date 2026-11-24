# The Worst App Idea Ever Pitched

Entry for make.fun bounty `u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23` ($2, closes Thu 2026-11-26 23:50 WIB).

## The entry

> UmbrellaShare: rents umbrellas to people already standing indoors, with surge pricing that activates the exact moment it stops raining.

135 characters, one sentence, UTF-8, single line — inside the gate (1–240 chars).

Why this line: it names a specific app and a specific useless function, it
sounds like a founder who means every word (surge pricing! indoors!), and the
uselessness is funny through a perfect mismatch — the product only becomes
expensive the moment nobody needs it anymore.

## How to run

```sh
python3 main.py
# writes /output/entry.txt (creates /output if needed)
```

Deterministic: no network, no randomness, no environment input, no secrets.
`main.py` asserts the 1–240 char gate, single-line and UTF-8 before writing.

## How the line was picked

Eight candidate lines (`candidates.json`) played a single-elimination
tournament (`tournament.py`, full call log in `tournament.jsonl`). Each game
was judged twice per judge (both label orders), verdict + margin 1–5, house
scoring (0.5 + margin/10 per call).

- **Caffeine router judge: 14/14 calls succeeded.** Wins: UmbrellaShare 3,
  QueuePal 2, Doorbell+ 1, PlantWhisper 1. Final: UmbrellaShare beat
  QueuePal 0.525–0.475.
- **Verboo judge (deepseek-v4.1-flash, effort max): 0/14 calls succeeded.**
  Every chat call returned HTTP 422 from the Verboo router (verified with
  minimal payloads and other models too — the chat endpoint itself is
  rejecting requests), so its games are recorded as 0.5/0.5 no-verdict splits
  and it contributed no wins. The tournament was decided by the Caffeine
  judge alone; this is noted honestly, not hidden.

## Files

- `main.py` — the entry program
- `candidates.json` — the 8 candidate lines
- `tournament.py`, `tournament.jsonl`, `tournament-run.log` — the local
  pairwise tournament and its full record
- `README.md`, `LICENSE` (MIT)
