library(xgboost)
set.seed(100)

# read data and merge them
house=read.csv("..\\house_cate2avg.csv")
macro=read.csv("..\\macro.csv")
raion=read.csv("..\\raions_raw_pct_all.csv")

macro_cols = c("timestamp", "balance_trade", "balance_trade_growth", "us.eur_rub", "average_provision_of_build_contract",
               "micex_rgbi_tr", "micex_cbi_tr", "deposits_rate", "mortgage_value", "mortgage_rate",
               "income_per_cap", "rent_price_4.room_bus", "museum_visitis_per_100_cap", "apartment_build")

macro=macro[,macro_cols]

total=merge(house, macro, by='timestamp')
total=merge(total, raion, by='sub_area')
total=total[order(total$id),]

# split data into train and test; remove redundant columns
data=total
data$id=NULL
data$sub_area=NULL

train=data[data$test == 0,]
test=data[data$test == 1,]
train$test=NULL
test$test=NULL
test$price_doc=NULL

trainy=train$price_doc
trainy=log1p(trainy)
trainx=train;trainx$price_doc=NULL

n_sample=length(trainy)
test_id=sort(sample(n_sample,0.2*n_sample))

fitx=trainx[-test_id,]
fity=trainy[-test_id]
valx=trainx[test_id,]
valy=trainy[test_id]

dfit=xgb.DMatrix(as.matrix(fitx), label=fity)
dval=xgb.DMatrix(as.matrix(valx), label=valy)
xgb.DMatrix.save(dfit, "fit.data")
xgb.DMatrix.save(dval, "val.data")

dtrain=xgb.DMatrix(as.matrix(trainx), label=trainy)
xgb.DMatrix.save(dtrain, "train.data")
write.csv(test,"test.data",row.names=F)
