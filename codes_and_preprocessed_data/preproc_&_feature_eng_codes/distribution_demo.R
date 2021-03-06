data=read.csv("..\\total_mod_manu.csv")
x=data$full_sq
y=data$price_doc
par(mfrow=c(2,1))
plot(x,y,cex=.5,
     xlab="full_sq",
     ylab="price_doc",
     main="Scatter plot: price vs area")
hist(y,10,xlab="price_doc",
     main="Histogram: price")