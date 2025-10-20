#Custom metrics + logging for model evaluation
from sklearn.metrics import accuracy_score, f1_score #import common metrics
from typing import Dict
import numpy as np

def classification_report(y_true, y_pred) -> Dict[str, float]:
    """Generate a classification report with accuracy and F1 score."""
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "f1": float(f1_score(y_true, y_pred, average ="weighted")),
    }

def rmse(y_true, y_pred) -> float:
    """Calculate RMSE."""
    return float(np.sqrt(((y_pred - y_true) ** 2).mean()))

