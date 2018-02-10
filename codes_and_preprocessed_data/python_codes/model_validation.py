import api
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LassoCV, RidgeCV
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_squared_log_error as msle
import numpy as np

trainx, trainy, testx, testy = api.read_train()

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
    score = mse(np.log(testy), predy) ** .5
    print(score)
else:
    model.fit(trainx, trainy)
    predy = model.predict(testx)
    predy[predy <= 500000] = 500000
    score = msle(testy, predy) ** .5
    print(score)
