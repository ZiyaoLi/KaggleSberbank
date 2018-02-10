import pandas as pd
import numpy as np

data = pd.read_csv("raions.csv")

tar1 = "raion_build_count_with_material_info"
cat1 = [
    "build_count_block",
    "build_count_wood",
    "build_count_frame",
    "build_count_brick",
    "build_count_monolith",
    "build_count_panel",
    "build_count_foam",
    "build_count_slag",
    "build_count_mix",
]
tar2 = "raion_build_count_with_builddate_info"
cat2 = [
    "build_count_before_1920",
    "build_count_1921-1945",
    "build_count_1946-1970",
    "build_count_1971-1995",
    "build_count_after_1995"
]

for i in cat1:
    data[i] = data[i] / data[tar1]
for i in cat2:
    data[i] = data[i] / data[tar2]


data.to_csv("raions_build_percentaged.csv", index=None)