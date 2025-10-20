#(Simulated) Data Ingestion
import pandas as pd
import numpy as np

#Synthetic example: time series with covariates
rng = pd.date_range("2022-01-01", periods=600, freq="D")
np.random.seed(42)
df = pd.DataFrame({
    "date": rng,
    "feature_search_interest": np.clip(np.sin(np.linspace(0, 30, len(rng))) * 50 + 50 + np.random.randn(len(rng))*5, 0, None),
    "feature_promo": np.random.binomial(1, 0.1, size=len(rng)),
    "feature_price": np.clip(100 + np.random.randn(len(rng))*3, 0, None)
})
# target depends on features with noise
df["target_demand"] = (
    0.6*df["feature_search_interest"] -
    0.3*df["feature_price"] +
    20*df["feature_promo"] +
    np.random.randn(len(rng))*8 +
    30
).clip(0)

df.head()
