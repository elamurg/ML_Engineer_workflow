from pathlib import Path
import pandas as pd
import yaml
from src.models.train import main as train_main
from src.models.evaluate import evaluate

#checking your entire training and evaluation pipeline
def test_train_then_eval(tmp_path):
    #prepare toy data and config
    data = pd.DataFrame({
        "x1":[1,2,3,4,5,6,7,8],
        "x2":["a","b","a","b","a","b","a","b"],
        "label":[0,1,0,1,0,1,0,1] #target variable
    })
    processed = tmp_path/"data.csv" #saves the toy data to a temporary folderr
    data.to_csv(processed, index = False)

    models_dir = tmp_path/"models" #defines another path where trained models will be saved
    cfg = {
        "experiment_name":"test", #name of the experiment
        "target": "label", #column to predict
        "paths":{ #where to find the data and where to save models
            "raw_data":str(processed),
            "processed_data":str(processed),
            "models_dir":str(models_dir)
        }, #training parameters, test size, random seed for reproductability, train the logistic regression model
        "train":{"test_size":0.25, "random_state":42, "model_type":"logreg"}
    }
    cfg_path = tmp_path/"cfg.yaml" #provides experiment setup, defines paths and params
    cfg_path.write_text(yaml.safe_dump(cfg))

    train_main(str(cfg_path))
    report = evaluate(str(models_dir/"test.joblib"), str(processed), "label") #calls the evaluate function, loads saved model, reads the dataset, and computes matrics like accuracy, F1 score
    assert "accuracy" in report #report output is a dictionary file

    #this is an E2E integration test
    #it proves your data can be saved and read properly
    #your config format works
    #the model trains without errors
    #the model file gets saved correctly
    #the evaluation function runs and returns metrics