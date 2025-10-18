#central config schema (validated with Pydantic)
from pydantic import BaseModel, Field
from typing import Optional

class Paths(BaseModel): #group all filesystem paths
    raw_data: str = Field(..., description="Path to raw input data") #...=required, add docstring
    processed_data: str = Field(..., description = "Path to processed data")
    models_dir: str = Field(..., description= "Directory to save trained models")

class TrainConfig(BaseModel): #training hyperparameters
    test_size: float = 0.2
    random_state: int = 42
    model_type: str = "logreg" 

class Config(BaseModel): #top-level bundle: paths+training+optional name
    paths: Paths
    train: TrainConfig
    experiment_name: Optional[str] = "dev"