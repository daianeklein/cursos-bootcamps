library(datasets) # USArrests
library(cluster)
library(tidyverse)
library(corrplot)
library(gridExtra)
library(GGally)
library(factoextra)

# 1. PREPARE CONHECA SEU DADO

help(USArrests)
head(USArrests)

# Missing values
any(is.na(USArrests))
is.null(USArrests)

# dtypes
any(as.logical(sapply(USArrests, is.numeric )-1))
unlist(lapply(USArrests,class))

# Scale data

mydata = data.frame(scale(USArrests))
summary(mydata)
sapply(mydata,median) 
sapply(mydata,var)

# 2. NUMERO DE K
# 2.1. Within and Betweenss: Elbow  
RNGversion("3.5.2")
set.seed(1987)
wss = 0
bss = 0
for (i in 1:10) wss[i] = sum(kmeans(mydata,i, nstart=25)$withinss) 
for (i in 1:10) bss[i] = sum(kmeans(mydata,i, nstart=25)$betweenss)

par(mfrow=c(1,2)) 
plot(1:10, wss, type="b", xlab="Number of Clusters", ylab="Within groups sum of squares")

# o ponto de cotovelo
abline(v=4,col="red")

plot(1:10, bss, type="b", xlab="Number of Clusters", ylab="Betweenss groups sum of squares")

# o ponto de cotovelo
abline(v=4,col="red")

# consulte o help(kmeans) e empregue a fun��o para responder a Q2  
fit = kmeans(USArrests, centers = 4, nstart=25) 
#

# 2.2. Group Sizes                                 Q3  
# ----------------------------------------------------------------------------------

set.seed(1987) # n�o altere para que seu resultados correspondam ao question�rio
par(mfrow=c(2,2))
for (i in 3:6){
  fit <- kmeans(mydata,i, nstart=25)
  main_ = paste("Size groups for k=", i)
  barplot(fit$size, main = main_ )
}  

# 
# consulte o help(kmeans) e empregue a fun��o para responder a Q3  
kmeans(USArrests, 4, nstart=25)
#
# 2.3. Silhouette Method                           Q4  
# ----------------------------------------------------------------------------------

set.seed(1987) # n�o altere para que seu resultados correspondam ao question�rio
ss_m = c(0)
for (i in 3:10){
  fit <- kmeans(mydata,  i, nstart=25)
  ss <- silhouette(fit$cluster, dist(mydata))
  ss_m[i] <-  mean(ss[,3])
}

par(mfrow=c(1,1))
plot(ss_m,
     type = "b", pch = 19, frame = FALSE, 
     xlab = "Number of clusters K",
     ylab = "Average Silhouettes",
     xlim=c(3,10))
# Voce s� poder� definir o valor abaixo depois de inspecionar no gr�fico acima
# o ponto de cotovelo
abline(v=4,col="red")

set.seed(1987) # n�o altere para que seu resultados correspondam ao question�rio
par(mfrow=c(2,2))
fit <- kmeans(mydata,  3, nstart=25)
ss <- silhouette(fit$cluster, dist(mydata))
plot(ss)

  fit <- kmeans(mydata,  4, nstart=25)
  ss <- silhouette(fit$cluster, dist(mydata))
  plot(ss)

fit <- kmeans(mydata,  5, nstart=25)
ss <- silhouette(fit$cluster, dist(mydata))
plot(ss)

fit <- kmeans(mydata,  6, nstart=25)
ss <- silhouette(fit$cluster, dist(mydata))
plot(ss)


# 3. ANALISE DOS GRUPOS (DOS RESULTADOS)           Q5  

set.seed(1987) # n�o altere para que seu resultados correspondam ao question�rio
fit <- kmeans(mydata,4, nstart=25)

par(mfrow=c(1, 1))
ss <- silhouette(fit$cluster, dist(mydata))
plot(ss)
mean(ss[,3])

# a. Visualizando o Cluster para os Dois Componentes Principais

par(mfrow=c(1, 1))
clusplot(mydata, fit$cluster, color=TRUE, shade=TRUE, labels=2, lines=0)

# 
# b. Visualizando o Cluster para Duas vari�veis de sua escolha 
#

p1 = ggplot(mydata, aes(UrbanPop, Murder, color = as.factor(fit$cluster))) + geom_point()
p2 = ggplot(mydata, aes(UrbanPop, Assault, color = as.factor(fit$cluster))) + geom_point()
p3 = ggplot(mydata, aes(UrbanPop, Rape, color = as.factor(fit$cluster))) + geom_point()

grid.arrange(p1, p2, p3)


# 
# c. Visualizando os valores m�dios de cada Cluster 
#

mydata$predict = fit$cluster # adicionando o atributo predict

par(mfrow=c(2, 2))
for (i in 1:4){
  main_ = paste("Group =", i)
  barplot(sapply(mydata[mydata$predict==i,-5],mean),main=main_) 
}

# d. Visualizando o Cluster para a diferentes pares de vari�veis e suas distribui��es

ggpairs(cbind(mydata, Cluster=as.factor(fit$cluster)),
        columns=1:4, aes(colour=Cluster, alpha=0.5),
        lower=list(continuous="points"),
        upper=list(continuous="blank"),
        axisLabels="none", switch="both") 

# 4. PAM K MED�IDES                       Q6 
mydata_pam = mydata[,-c(5)] # retira o valor predict acrescentado anteriormente

set.seed(1987) # n�o altere para que seu resultados correspondam ao question�rio
fit = pam(mydata_pam,4)

# Compare PAM e Kmeans
table(fit$cluster, mydata$predict)

ss <- silhouette(fit$cluster, dist(mydata_pam))

par(mfrow=c(1, 1))
plot(ss)
mean(ss[,3])

# 
# 5. CLUSTER HIERARQUICO HCLUST            Q7 Q8 Q9
# ----------------------------------------------------------------------------------

mydata_hclu = mydata[,-c(5)] # retira o valor predict acrescentado anteriormente

set.seed(1987) # n�o altere para que seu resultados correspondam ao question�rio
d <- dist(mydata_hclu, method = "euclidean") # distance matrix

#    ATEN��O: altere o c�digo para escolha de um m�todo e execute um m�todo por 
#    vez escolhendo o melhor particionamento
#

fit <- hclust(d, method = "complete")
fit

fit <- hclust(d, method = "single")
fit

fit <- hclust(d, method = "average")
fit

#
#    A seguir repetem-se os mesmos procedimentos empregados para o K-m�dias: 
#    an�lise do Silhouette, Visualiza��o dos resultados e um comparativo com o PAM.


par(mfrow=c(1, 1))
plot(fit) # display dendogram

# cut tree into 4 clusters
groups <- cutree(fit, k=4) 

# draw dendogram with red borders around the 4 clusters 
rect.hclust(fit, k=4, border="red")

#
#  Silhouette
#
ss = silhouette(groups, dist(mydata_hclu))
plot(ss)
mean(ss[,3])
#
# Compare aqui agrupamentos (PAM, hclust) e (Kmeans, hclust) a 
# exemplo c�digo acima em que comparamos (PAM, Kmeans) 
#
# responda ent�o a quest�o 9
#

# o c�digo para essa quest�o n�o � fornecido

set.seed(1987)

#
# see results like kmeans 
#
par(mfrow=c(1, 1))
clusplot(mydata_hclu, groups, color=TRUE, shade=TRUE, 
         labels=2, lines=0)

# Centroid Plot against 1st 2 discriminant functions
# library(fpc)
plotcluster(mydata_hclu, groups)

ggpairs(cbind(mydata_hclu, Cluster=as.factor(groups)),
        columns=1:4, aes(colour=Cluster, alpha=0.5),
        lower=list(continuous="points"),
        upper=list(continuous="blank"),
        axisLabels="none", switch="both")

#
# 6. OUTROS M�TODOS E DISCUSS�O           Q10
# 
# Acesse help(fviz_nbclust) ou pesquise na internet sobre esse pacote 
# e execute o c�digo abaixo para os m�todos kmeans e hclust
# 

# para reestabelecer somente os valores de Murder, Assault, UrbanPop, Rape  
mydata = mydata[,-c(5)] # retira o valor predict acrescentado anteriormente

set.seed(1987) # n�o altere para que seu resultados correspondam ao question�rio
fviz_nbclust(mydata, kmeans, method = "silhouette")

# Veja no help(fviz_nbclust) o que a fun��o abaixo faz e como alterar o
# parametro de kmeans para o cluster hierarquico (n�o � hclust! ;-) )

set.seed(1987) # n�o altere para que seu resultados correspondam ao question�rio
fviz_nbclust(mydata, FUNcluster = kmeans, method = c("silhouette", "wss",
                                                     "gap_stat"), diss = NULL, k.max = 20, nboot = 100,
             verbose = interactive(), barfill = "steelblue", barcolor = "steelblue",
             linecolor = "steelblue", print.summary = TRUE)
