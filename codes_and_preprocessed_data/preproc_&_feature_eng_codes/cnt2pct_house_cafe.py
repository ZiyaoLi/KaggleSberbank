import pandas as pd
import numpy as np

data = pd.read_csv("..\\total.csv")
dist = ["500", "1000", "1500", "2000", "3000", "5000"]
price = ["500", "1000", "1500", "2500", "4000", "high"]
pref = "cafe_count_"
midf = "_price_"

for d in dist:
    print(d)
    tot = data[pref + d]
    tot[tot == 0] = -1
    for p in price:
        name = pref + d + midf + p
        series = data[name]
        series = series / tot
        series[series < 0] = 0
        data[name] = series

data.to_csv("..\\house_cafe_percentaged.csv")
