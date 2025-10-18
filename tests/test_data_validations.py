#happy path tests and failure cases to ensure validators work
import pandas as pd
from src.data.validate import validate_columns, validate_no_missing_values
import pytest

def test_validate_columns_ok(): #test function that runs with pytest
    df = pd.DataFrame({"a":[1], "b":[2]}) #alter the column names based on the dataset
    validate_columns(df, ["a", "b"])

def test_validate_columns_missing():
    df = pd.DataFrame({"a": [1]}) #uses pytest.raises(ValueError) to check the error code
    with pytest.raises(ValueError):
        validate_columns(df, ["a", "b"])

def test_validate_no_missing_values():
    df = pd.DataFrames({"a":[1,None]})
    with pytest.raises(ValueError):
        validate_no_missing_values(df, ["a"]) #if a contains missing values, function raises an error