import numpy as np
import pandas as pd

data = pd.read_csv("..\\total.csv")
data_f = pd.read_csv("..\\bad_address_fix.csv")

p = np.array(data_f['id']) - 1
p[2:] = p[2:] - 2
data_f.index = p
r = data_f.columns.values

data.ix[p, r] = data_f

data.to_csv("..\\total_modified.csv", index=None)
