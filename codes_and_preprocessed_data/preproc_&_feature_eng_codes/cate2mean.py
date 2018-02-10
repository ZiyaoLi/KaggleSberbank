import numpy as np
import pandas as pd

data = pd.read_csv("..\\total.csv")
cat = [
    "ID_metro",
    "ID_railroad_station",
    "ID_big_road1",
    "ID_big_road2",
    "ID_railroad_terminal",
    "ID_bus_terminal"
]

for col in cat:
    print(col)
    levels = list(set(data[col]))
    means = np.zeros([len(levels), 3])
    for t in range(len(levels)):
        means[t, 0] = levels[t]
        tmp = data[data[col] == levels[t]]
        means[t, 1] = (tmp['price_doc']).mean()
        means[t, 2] = (tmp['price_doc'] / tmp['full_sq']).mean()
    means = pd.DataFrame(means,
                         columns=[col, col + '_avg_price', col + '_avg_price_psqm'])
    data = pd.merge(data, means, on=col)
    data.drop(col, 1, inplace=True)

data.to_csv("..\\house_cate2avg.csv", index=None)


