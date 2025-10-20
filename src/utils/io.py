#Utility function for I/O operations
from pathlib import Path
import joblib
import pandas as pd

def ensure_dir(path: str | Path) -> Path:
    """Ensure the target directory exists."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok = True)
    return p

def save_model(obj, path: str | Path):
    """Save a model to disk using joblib."""
    path = Path(path)
    ensure_dir(path.parent)
    joblib.dump(obj, path)

def load_model(path: str | Path): #persist sklearn models via joblib
    """Load a model from disk using joblib."""
    return joblib.load(Path(path))

def read_csv(path: str | Path) -> pd.DataFrame: #centralized CSV I/O
    """Read a CSV file into a pandas DataFrame."""
    return pd.read_csv(path)

def write_csv(df: pd.DataFrame, path: str | Path) -> None:
    """Write a pandas DataFrame to a CSV file."""
    path = Path(path)
    ensure_dir(path.parent)
    df.to_csv(path, index =False)

