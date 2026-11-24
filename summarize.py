"""Recompute the paired combat results from the exported replay outcomes."""

import csv
from collections import Counter
from pathlib import Path


def main():
    path = Path(__file__).parent / "data" / "test_subject_pairs.csv"
    with path.open(newline="") as source:
        rows = list(csv.DictReader(source))

    pairs = {(r["entry_id"], r["repeat"]) for r in rows}
    if len(pairs) != len(rows):
        raise ValueError("Duplicate entry and repeat")

    print("| Difficulty | Pairs | Both win | Baseline only | Specialist only | Both lose |")
    print("|---|---:|---:|---:|---:|---:|")
    for label in ["9", "10", "All"]:
        subset = [r for r in rows if label == "All" or r["ascension"] == label]
        counts = Counter((r["baseline_win"], r["specialist_win"]) for r in subset)
        outcomes = [("1", "1"), ("1", "0"), ("0", "1"), ("0", "0")]
        if set(counts).difference(outcomes):
            raise ValueError("Outcomes must be zero or one")
        cells = [label, len(subset), *(counts[key] for key in outcomes)]
        print("| " + " | ".join(map(str, cells)) + " |")
    entries = {r["entry_id"] for r in rows}
    seeds = {r["game_seed"] for r in rows}
    print(f"\n{len(entries)} combat starts from {len(seeds)} game seeds.")


if __name__ == "__main__":
    main()
