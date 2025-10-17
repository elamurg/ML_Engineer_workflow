#happy path tests and failure cases to ensure validators work
import pandas as pd
from src.data.validate import validate_columns, validate_no_missing_values
import pytest

def test_validate_columns_ok():
    df = pd.DataFrame({"a":[1], "b":[2]})
    validate_columns(df, ["a", "b"])

def test_validate_columns_missing():
    df = pd.DataFrame({"a": [1]})
    with pytest.raises(ValueError):
        validate_columns(df, ["a", "b"])

def test_validate_no_missing_values():
    df = pd.DataFrames({"a":[1,None]})
    with pytest.raises(ValueError):
        validate_no_missing_values(df, ["a"])