import pandas as pd
import numpy as np

data = pd.read_csv("raions.csv")

cat = ["young_", "work_", "ekder_"]
man = ["all", "male", "female"]
tar = "raion_popul"

for i in cat:
    for j in man:
        data[i + j] = data[i + j] / data[tar]

data.to_csv("raions_popul_percentaged.csv", index=None)
