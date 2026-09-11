MAIN	= french_accents_selector.py

install:
	python -m venv .fasvenv
	.fasvenv/bin/python -m pip install -r requirements.txt
	.fasvenv/bin/pyinstaller $(MAIN)
	rm -rf build/
	sudo mv dist/french_accents_selector/ /opt/
	sudo ln -s /opt/french_accents_selector/french_accents_selector /usr/local/bin/french_accent_selector
	rm -rf .
.PHONY: install
