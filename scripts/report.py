#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()

with open(args.input, newline="") as source:
    rows = list(csv.DictReader(source))

by_account = {}
for row in rows:
    by_account[row["account"]] = by_account.get(row["account"], 0.0) + float(row["amount"])

Path(args.output).parent.mkdir(parents=True, exist_ok=True)
with open(args.output, "w") as output:
    for account, amount in sorted(by_account.items()):
        output.write(f"{account}: {amount:.2f}\n")
