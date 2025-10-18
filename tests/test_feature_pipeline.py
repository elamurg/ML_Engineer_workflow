import pandas as pd
from src.features.build import build_features
#test verifies that yourfeature-splitting function works as expected
def test_build_features_shapes():
    df = pd.DataFrame({ #mock dataset, simplified version of your real dataset used only for testing logic
        "x1": [1,2,3,4,5],
        "x2": ["a","b","c","d"],
        "label": [0,1,0,1,0] #target column
    })
    Xtr, Xte,ytr, yte = build_features(df, "label", 0.2, 42) #label (target column), test size (20%), random seed (42)
    assert len(Xtr)+len(Xte)==len(df)
    assert len(ytr)+len(yte)==len(df)

#it checks that no rows are lost, and the number of rows in train+test equals the total of rows in your dataset
