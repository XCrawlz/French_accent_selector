MAIN	= french_accents_selector.py

install:
	python -m venv .fasvenv
	.fasvenv/bin/python -m pip install -r requirements.txt

run:
	.fasvenv/bin/python $(MAIN)

run-gui:
	.fasvenv/bin/python $(MAIN) -g

debug:
	.favenv/bin/python -m pdb $(MAIN)

clean:
	find . -type d -name ".fasvenv" -exec rm -rf {} +
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

.PHONY: install run debug clean lint lint-strict⏎   
