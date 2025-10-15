.PHONY: setup test train serve format

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -e . 

test:
	pytest -q

train:
	python -m src.models.train --config configs/dev.yaml

serve:
	uvicorn src.serving.service:app --reload

format:
	ruff check --fix . || true