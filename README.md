# Can a boss specialist win fights the original game AI loses?

Playing Slay the Spire 2, I was surprised by how often the open-source spire-mentor agent won. I proposed training separate specialists for difficult bosses. This repository follows one candidate through its last development check against the Test Subject boss. The specialist rescued three fights and lost four that the baseline had won. On that evidence, I kept the baseline.

## The comparison

Both agents started from the same combat state, used the same search budget of 8,000 simulations per decision, and differed in the rollout network used by search. A rollout network guides simulated continuations while the agent evaluates a move. Each of 40 starts was replayed twice per agent, giving 80 paired comparisons from 18 original game seeds. Repeated fights from a given seed share game history.

| Difficulty | Pairs | Both win | Baseline only | Specialist only | Both lose |
|---|---:|---:|---:|---:|---:|
| 9 | 32 | 14 | 3 | 1 | 14 |
| 10 | 48 | 14 | 1 | 2 | 31 |
| All | 80 | 28 | 4 | 3 | 45 |

The 73 agreements show why I wanted to see *which* fights changed. The candidate won 31 fights overall and the baseline won 32. The specialist fell short of the criterion to advance, so the separate test set remained unused. These results cover one boss during development. Full-game performance is a separate question.

## Reproduce the table

Run `python3 summarize.py` from this directory. It uses the Python standard library. Each CSV row pairs the original agent and the TestSubject-B candidate by combat start and repeat, with 1 for a combat win and 0 for a loss. The export was checked against SHA-256 hashes for all 160 source replay logs. It contains the outcomes needed to recompute the table.

## Credits

I proposed encounter-specific specialization based on my experience with the game. I used AI assistance for implementation, simulation, analysis, and preparing this write-up. The underlying engine, search algorithm and original agent come from Thomas Friedel's open-source project. [Upstream spire-mentor](https://github.com/tfriedel/spire-mentor)
