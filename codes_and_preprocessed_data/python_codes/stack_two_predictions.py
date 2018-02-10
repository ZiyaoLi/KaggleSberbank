import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_squared_log_error as msle


def cosine_(p1, p2, a, b, c):
    print("h:  %.6f" % (a * (1 - (a*a + c*c - b*b)**2/(2*a*c)**2) ** .5))
    print("p1: %.6f" % (.5 - (a ** 2 - b ** 2) / (2 * c ** 2)))
    print("p2: %.6f" % (.5 + (a ** 2 - b ** 2) / (2 * c ** 2)))
    return (p1 + p2) / 2 - (a ** 2 - b ** 2) / (2 * c ** 2) * (p1 - p2)

r1 = 30628
r2 = 30
name1 = "..\\submit\\"+str(r1)+".csv"
name2 = "..\\submit\\"+str(r2)+".csv"

df = pd.read_csv(name1)
array1 = df['price_doc']
array2 = pd.read_csv(name2)['price_doc']
array1 = np.log(array1)
array2 = np.log(array2)

r1 /= 100000
r2 /= 100000
r3 = mse(array1, array2) ** .5

print((r1, r2, r3))

p = cosine_(array1, array2, r1, r2, r3)
df['price_doc'] = np.exp(p)
df.to_csv("merge_%d_%d.csv" % (r1 * 100000, r2 * 100000), index=None)
