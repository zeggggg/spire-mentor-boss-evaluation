# Testing a boss specialist in Slay the Spire 2

As a player, I was surprised by how often the open-source *spire-mentor* agent won. I wondered whether practice against a single difficult boss could help it win fights it usually lost. Against the Test Subject boss, **the specialist rescued three fights and lost four that the original agent had won**. I kept the original agent.

## How I tested the idea

The agent uses a search algorithm to choose its next move. During search, a rollout network helps it play out possible continuations. The experiment swapped the original rollout network for a specialist trained for Test Subject. Both agents started each comparison in the same combat state and had the same budget of 8,000 simulations per decision.

I wanted to count both kinds of changes. A replay where the specialist rescued a loss was just as relevant as one where it turned a win into a loss.

| Difficulty | Pairs | Both win | Baseline only | Specialist only | Both lose |
|---|---:|---:|---:|---:|---:|
| 9 | 32 | 14 | 3 | 1 | 14 |
| 10 | 48 | 14 | 1 | 2 | 31 |
| All | 80 | 28 | 4 | 3 | 45 |

These 80 pairs came from **40 combat starts across 18 game seeds**, with two repeats per start. The agents agreed on 73 outcomes. The other seven gave me little reason to advance the specialist to the reserved test set. This comparison measures performance in one boss fight. A claim about winning more full games would need a separate experiment.

## Reproduce the result

Run the following command from the repository root with Python 3. It prints the table above and counts the distinct starts and seeds.

```sh
python3 summarize.py
```

The CSV contains one row per start and repeat. The last two columns record whether each agent won (1) or lost (0). The export was verified against the SHA-256 hashes of all 160 source replay logs. [Paired outcomes](data/test_subject_pairs.csv) · [Analysis script](summarize.py)

## My contribution

I proposed specializing the agent by encounter, drawing on my experience playing the game. I used AI tools for implementation, simulation, analysis, and this write-up. Thomas Friedel's project supplied the game engine, search algorithm, and original agent. [Upstream spire-mentor](https://github.com/tfriedel/spire-mentor)
