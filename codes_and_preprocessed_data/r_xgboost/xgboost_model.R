library(xgboost)
fit=xgb.DMatrix("fit.data")
val=xgb.DMatrix("val.data")
train=xgb.DMatrix("train.data")
test=read.csv("test.data")
row.names(test)=(30474:38135)

xgb_params=list(
  eta=0.01,
  max_depth=8,
  min_child_weight=20,
  subsample=1,
  colsample_bytree=0.5,
  objective='reg:linear',
  eval_metric='rmse',
  silent=1
)
watchlist=list(
  val=val
)

fit.model=xgb.train(
  xgb_params,
  fit,
  watchlist=watchlist,
  nrounds=2000,
  verbose=1,
  print_every_n=20,
  early_stopping_rounds=80
)

total.model=xgb.train(
  xgb_params,
  train,
  nrounds=1000,
  watchlist=watchlist,
  verbose=1,
  print_every_n=20
)

imp_mat=xgb.importance(total.model)
feature_id=as.numeric(imp_mat$Features)+1
imp_mat$Features=colnames(test)
xgb.plot.importance(imp_mat,top_n=10)

pred=exp(predict(total.model, as.matrix(test)))
write.csv(pred,"pred.csv")
