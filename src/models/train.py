import argparse
from pathlib import Path
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from scr.config import Config, Paths, TrainConfig
from src.utils.io import read_csv, save_model, ensure_dir
from src.features.build import build_features

def make_model(model_type: str, random_state: int):
    if model_type == "logreg":
        return LogisticRegression(max_iter = 1000)
    if model_type == "rf":
        return RandomForestClassifier(n_estimators = 200, random_state = random_state)
    raise ValueError(f"Unknown model_type: {model_type}")

def infer_column_types(df: pd.DataFrame, target: str):
    numeric = df.drop(columns = [target]).select_dtypes(include=["number"]).columns.tolist()
    categorical = df.drop(columns = [target]).select_dtypes(exclude = ["number"]).columns.tolist()
    return numeric, categorical

def main(config_path: str): #--- parse a very simple "config" inline for brevity ---
    import yaml
    cfg_dict = yaml.safe_load(Path(config_path).read_text)
    cfg = Config(
        paths = Paths(**cfg_dict["paths"]),
        train = TrainConfig(**cfg_dict["train"]),
        experiment_name = cfg_dict.get("experiment_name", "dev"),
    ) 
    df = read_csv(cfg.paths.processed_data) #load processed data
    target = cfg_dict["target"] #specify target column
    num_cols, cat_cols = infer_column_types(df, target)

    preproc = ColumnTransformer(
        transformers = [
            ("num", StandardScaler(), num_cols),
            ("cat", OneHotEncoder(handle_unknown = "ignore"), cat_cols)
        ],
        remainder = "drop",
    )
    model = make_model(cfg.train.model_type, cfg.train.random_state) #model choice
    pipe = Pipeline(
        steps =[("preproc", preproc), ("model", model)]
    )
    X_train, X_test, y_train, y_test = build_features(
        df, target, cfg.train.test_size, cfg.train.random_state
    )
    pipe.fit(X.train, y_train) #train
    ensure_dir(cfg.paths.models_dir)
    model_path = Path(cfg.paths.models_dir)/f"{cfg.experiment_name}.joblib"
    save_model(pipe, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required =True)
    args = parser.parse_args()
    main(args.config)
