import pandas as pd
from sklearn.model_selection import train_test_split

def build_features(df: pd.DataFrame, target: str, test_size: float, random_state: int):
    """Split the DataFrame into training and testing sets. """
    y = df[target]
    X = df.drop(columns = [target])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, 
        stratify=y if y.nunique() < 20 else None
    )
    return X_train, X_test, y_train, y_test