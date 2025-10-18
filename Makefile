.PHONY: setup test train serve format #declares task names that aren't files

setup: #creates a venv and installs your package in editable mode
	python -m venv .venv && . .venv/bin/activate && pip install -e . 

test: #runs tests
	pytest -q

train: #runs training with a config file
	python -m src.models.train --config configs/dev.yaml

serve: #starts API server from service.py
	uvicorn src.serving.service:app --reload

format: #example code formatting task using ruff
	ruff check --fix . || true