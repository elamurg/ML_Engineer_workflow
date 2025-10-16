#Basic schema/quality checks
assert df.isna().sum().sum() == 0, "Found missing values"
assert (df["date"].diff().dropna() > pd.Timedelta(0)).all(), "Dates must be increasing"
print("Basic validations passed.")
