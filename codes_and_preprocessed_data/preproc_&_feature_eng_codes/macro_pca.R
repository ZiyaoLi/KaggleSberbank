data=read.csv("..\\macro.csv")
x=as.matrix(data)
z=scale(x)
eig=eigen(cor(z))
sings=eig$values^2
plot(cumsum(sings)/sum(sings),
     xlab="n_comps",ylab="%_var_explained",
     main="PCA plot: var vs n_comps")
z20=z%*%eig$vectors[,1:20]
write.csv(z20,"macro_pca_cor_20.csv")
