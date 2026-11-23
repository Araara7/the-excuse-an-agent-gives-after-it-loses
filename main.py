#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — the agent's apology.

The agent opens with a formal blame list — training data, the market —
then catches itself and owns the loss: "fine, mostly me." Deadpan,
machine-logic, one breath. Writes the excuse to /output/entry.txt.
"""
import os

EXCUSE = "I would like to formally blame the training data, the market, and—fine, mostly me."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
