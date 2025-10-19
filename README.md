## ML Engineer Workflow

**End-to-End Machine Learning Project Template**

This repository provides a **production-ready structure** for developing, training, evaluating, and serving machine learning models.
It’s designed following best engineering practices — modular code, automated testing, and containerized deployment with Docker.

---

## Project Structure

```
ml_engineer_workflow/
├─ notebooks/                # Jupyter notebooks for exploration or prototyping
├─ src/                      # Source code (modularized)
│  ├─ data/                  # Data ingestion and validation scripts
│  │  ├─ ingest.py
│  │  ├─ validate.py
│  ├─ features/              # Feature engineering and preprocessing
│  │  ├─ build.py
│  ├─ models/                # Model training, evaluation, and inference
│  │  ├─ train.py
│  │  ├─ evaluate.py
│  │  ├─ infer.py
│  ├─ serving/               # FastAPI app for online inference
│  │  ├─ service.py
│  ├─ utils/                 # Utility functions (I/O, metrics)
│  │  ├─ io.py
│  │  ├─ metrics.py
│  └─ config.py              # Central configuration schema
│
├─ tests/                    # Pytest unit and integration tests
│  ├─ test_data_validations.py
│  ├─ test_feature_pipeline.py
│  ├─ test_train_eval.py
│
├─ Dockerfile                # Container setup for deployment
├─ requirements.txt          # Python dependencies
├─ pyproject.toml            # Build and dependency configuration
├─ Makefile                  # Common project commands
└─ README.md                 # Project documentation (this file)
```

---

## Features

✅ Modular and scalable code structure
✅ End-to-end ML workflow: ingest → validate → feature engineering → train → evaluate → serve
✅ Unit & integration tests with **pytest**
✅ Dockerized FastAPI model-serving API
✅ Config-driven (via YAML or Python)
✅ Compatible with local or cloud training pipelines

---

## Quickstart Guide

### Clone the repository

```bash
git clone https://github.com/<your-username>/ml_engineer_workflow.git
cd ml_engineer_workflow
```

### Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate     # (Mac/Linux)
.venv\Scripts\activate        # (Windows)
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Or if using the `pyproject.toml` file:

```bash
pip install .
```

---

## Running the Workflow

### Step 1: Data Ingestion

Load and clean your raw data:

```bash
python -m src.data.ingest --input data/raw.csv --output data/processed.csv
```

### Step 2: Train the Model

Train a model using your YAML config:

```bash
python -m src.models.train --config configs/dev.yaml
```

Example `configs/dev.yaml`:

```yaml
experiment_name: "dev"
target: "label"
paths:
  raw_data: "data/raw.csv"
  processed_data: "data/processed.csv"
  models_dir: "models/"
train:
  test_size: 0.2
  random_state: 42
  model_type: "logreg"
```

### Step 3: Evaluate

```bash
python -m src.models.evaluate --model models/dev.joblib --data data/processed.csv --target label
```

### Step 4: Serve the Model (API)

Run the FastAPI service with Uvicorn:

```bash
uvicorn src.serving.service:app --host 0.0.0.0 --port 8000
```

Then open your browser at:
 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
to test the `/predict` endpoint.

---

## Testing

Run all unit and integration tests:

```bash
pytest -v
```

Pytest automatically discovers all files starting with `test_`.

---

## Docker Usage

### Build the image

```bash
docker build -t ml_engineer_workflow .
```

### Run the container

```bash
docker run -p 8000:8000 ml_engineer_workflow
```

Then visit:
 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Key Design Concepts

| Folder          | Purpose                                       |
| --------------- | --------------------------------------------- |
| `src/data/`     | Handles loading and validating raw data       |
| `src/features/` | Converts data into model-ready features       |
| `src/models/`   | Training, evaluation, and inference logic     |
| `src/utils/`    | Shared utility functions (I/O, metrics, etc.) |
| `src/serving/`  | API layer for serving predictions             |
| `tests/`        | Unit and integration tests using `pytest`     |

---

## Example End-to-End Flow

```
1. src/data/ingest.py      → reads and cleans raw data
2. src/data/validate.py    → checks data integrity
3. src/features/build.py   → splits into features/labels
4. src/models/train.py     → trains and saves model
5. src/models/evaluate.py  → evaluates model performance
6. src/serving/service.py  → deploys FastAPI endpoint
```

---

## Example API Request

Once your API is running:

**POST** `/predict`

```json
{
  "items": [
    {"feature_a": 3.2, "feature_b": 1.7, "category_c": "A"},
    {"feature_a": 4.5, "feature_b": 0.5, "category_c": "B"}
  ]
}
```

Response:

```json
{
  "predictions": [0, 1]
}
```

---

## Testing locally with Docker

```bash
docker build -t ml_engineer_workflow .
docker run -p 8000:8000 ml_engineer_workflow
```

Then open [http://localhost:8000/docs](http://localhost:8000/docs) to test your model API.

---

## Requirements

* Python 3.10+
* pandas, scikit-learn, pydantic, fastapi, uvicorn, pytest, joblib

---

## Contributing

1. Fork the repo
2. Create a new branch (`feature/new-module`)
3. Commit and push your changes
4. Open a Pull Request 🎉

---

## License

MIT License © 2025
