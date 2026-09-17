.PHONY: setup clean

setup:
	@mkdir -p build
	@python3 scripts/compat.py
	@python3 scripts/report.py --input data/sample_journal.csv --output build/summary.txt

clean:
	rm -rf build
