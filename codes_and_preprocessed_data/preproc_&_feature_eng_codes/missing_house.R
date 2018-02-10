library(mice)
data=read.csv("..\\total_mod_manu.csv")
pMiss=function(x) {
  colSums(is.na(x))/nrow(x)
}
r=data[,1:13]
predmat=matrix(1,13,13)
diag(predmat)=0
predmat[,1]=0
m=mice(r,predictorMatrix=predmat,visitSequence='monotone',method='cart')
filled=complete(m)
write.csv(filled,"..\\house_filled.csv",index=NULL)