import pandas as pd

heart = pd.read_csv("data/heart.csv")
print(f" {len(heart)} rows and {len(heart.columns)} columns")
heart= heart.drop_duplicates()
print(f" {len(heart)} rows and {len(heart.columns)} columns after dropping duplicates")
uci = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data",
    header=None,
    names=[*heart.columns[:-1], "num"],
)

keys = ["age", "sex", "trestbps", "chol", "fbs", "thalach", "exang", "oldpeak"]
matched = heart.merge(uci, on=keys, validate="one_to_one")

print(f"Matched {len(matched)} of {len(heart)} distinct rows")
print(pd.crosstab(matched["target"], matched["num"] > 0))