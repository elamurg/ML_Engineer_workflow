import pandas as pd

def validate_columns(df: pd.DataFrame, required: list[str]) -> None: #ensure expected schema
    """Validate that the DataFrame contains the requred columns."""
    missing = set(required) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
def validate_no_na(df: pd.DataFrame, cols: list[str])-> None: #block training is cols has NAs
    """Validate that there are no NA values in the specified columns."""
    bad = [c for c in cols if df[c].isna().any()]
    if bad:
        raise ValueError(f"NA values found in columns: {bad}")