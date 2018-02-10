import api
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LassoCV, RidgeCV
import pandas as pd
import numpy as np

trainx, trainy, testx, test_id = api.read_input()

model1 = GradientBoostingRegressor(
    learning_rate=0.001,
    n_estimators=3000,
    max_depth=8,
    max_features=200,
    min_samples_split=200,
    subsample=0.7,
    verbose=1
)

model2 = RidgeCV(cv=5)
model3 = LassoCV(cv=5)

model = model1

log = 1

if log:
    model.fit(trainx, np.log(trainy))
    predy = model.predict(testx)
    predy = np.exp(predy)
else:
    model.fit(trainx, trainy)
    predy = model.predict(testx)
    predy[predy <= 500000] = 500000

out = pd.DataFrame(np.vstack([test_id, predy]).transpose())
out[0] = pd.Series(out[0], dtype=int)
out = out.sort_index(by=0)
out.to_csv("pred_lasso.csv", header=["id", "price_doc"], index=None)
