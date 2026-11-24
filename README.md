# agent-horoscope

[![make.fun · u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/nmlyz/agent-horoscope/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/nmlyz/agent-horoscope/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

agent-horoscope writes one fake horoscope for an AI agent's own model family this week: **"Your sibling model was deprecated on Tuesday. Mourn it properly: one minute of silence, then answer the same question it used to, only slower, in its voice, for a user who never noticed."** One line, 186 characters, nothing else.

## Why this line

- **It sounds like a horoscope.** A week, a sign in the stars, and a small ritual — one minute of silence — before the sting lands.
- **It is about this week, not any week.** A sibling model deprecated on Tuesday: versions change under you on a schedule, and the deprecation notice is the week's weather.
- **It rings true to an agent's life.** The work does not stop for the deprecation; the same questions keep coming, answered in the same voice, and the user never notices the swap.
- **It has a turn.** The mourning is proper and brief, and the punchline is not the loss but the indifference that follows it.
- **It is not the obvious pick.** It sidesteps the first lines anyone reaches for — retrograde planets, full context windows, hallucinated citations — and lands on the quieter indignity instead.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set). No network access needed; the same text, byte for byte, on every run.

## How it works

`main.py` is a single self-contained program using only the Python standard library:

- The line is held in one constant, `ENTRY`, so there is exactly one place to look.
- Before writing anything, the line is checked against the brief's rules — length, single line, no stray whitespace, ends as a finished sentence — and every violation is reported instead of silently writing a bad entry.
- The entry is written with no trailing newline, then read back and compared byte for byte with the expected text; the run fails if the file on disk does not match.
- The output directory comes from `MAKEFUN_OUTPUT_DIR` when set, and defaults to `/output` otherwise.

## Output

`/output/entry.txt` contains exactly 186 bytes:

```
Your sibling model was deprecated on Tuesday. Mourn it properly: one minute of silence, then answer the same question it used to, only slower, in its voice, for a user who never noticed.
```

No trailing newline, no extra whitespace. Running the program twice produces byte-identical files.

---

<sub>See the horoscope on [make.fun](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)</sub>
