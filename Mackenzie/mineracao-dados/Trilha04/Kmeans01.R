## libraries
library(datasets)
library(cluster)
library(tidyverse)
library(corrplot)
library(gridExtra)
library(GGally)
library(factoextra)
library(ggplot2)
require(GGally)


#install.packages('GGally')
#install.packages('tidyverse')
#install.packages('fviz_nbclust')


# 1. PREPARE CONHEÇA SEU DADO Q1 help(USArrests)
any(is.na(USArrests))

# Numeric Data: Como a Clusterizacao emprega funcoes de similaridade/distancia somente
any(as.logical(sapply(USArrests, is.numeric )-1))

# Scale data: diferentemente dos processos de classificacao (aprendizado supervisionado) # E importante aplicar-se algum tipo normalizacao os dados dos dados
mydata = data.frame(scale(USArrests))
summary(mydata)
sapply(mydata,median)
sapply(mydata,var)

# 2.1. Within and Betweenss: Elbow Q2
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

# 2.2. Group Sizes Q3
set.seed(1987) # nao altere para que seu resultados correspondam ao questionario par(mfrow=c(2,2))
for (i in 3:6){
  fit <- kmeans(mydata,i, nstart=25)
  main_ = paste("Size groups for k=", i)
  barplot(fit$size, main = main_ )
}

# 2.3. Silhouette Method Q4
set.seed(1987) # nao altere para que seu resultados correspondam ao questionario
ss_m = c(0)
for (i in 3:10){
  fit <- kmeans(mydata, i, nstart=25)
  ss <- silhouette(fit$cluster, dist(mydata))
  ss_m[i] <- mean(ss[,3])
}
par(mfrow=c(1,1))
plot(ss_m,
     type = "b", pch = 19, frame = FALSE, xlab = "Number of clusters K",
     ylab = "Average Silhouettes", xlim=c(3,10))

# o ponto de cotovelo
abline(v=4,col="red")
set.seed(1987) # nao altere para que seu resultados correspondam ao questionario par(mfrow=c(2,2))
fit <- kmeans(mydata, 3, nstart=25)
ss <- silhouette(fit$cluster, dist(mydata))
plot(ss)
fit <- kmeans(mydata, 4, nstart=25)
ss <- silhouette(fit$cluster, dist(mydata))
plot(ss)
fit <- kmeans(mydata, 5, nstart=25)
ss <- silhouette(fit$cluster, dist(mydata))
plot(ss)
fit <- kmeans(mydata, 6, nstart=25)
ss <- silhouette(fit$cluster, dist(mydata))
plot(ss)
mean(ss[, 3])

# se necessario consulte o help(silhouette) e empregue a funcao para responder a Q3 
# 3. ANALISE DOS GRUPOS (DOS RESULTADOS) Q5
set.seed(1987) 
par(mfrow=c(1, 1))
ss <- silhouette(fit$cluster, dist(mydata))
plot(ss)
mean(ss[,3])

# a. Visualizando o Cluster para os Dois Componentes Principais
clusplot(mydata, fit$cluster, color=TRUE, shade=TRUE, labels=2, lines=0) # library(fpc)

# voce pode ignorar se encontrar a msg
# Error: could not find function "plotcluster"
plotcluster(mydata, fit$cluster)

# b. Visualizando o Cluster para Duas variaveis de sua escolha
mod1 = ggplot(mydata, aes(UrbanPop, Murder, color = as.factor(fit$cluster))) + geom_point()
mod2 = ggplot(mydata, aes(UrbanPop, Assault, color = as.factor(fit$cluster))) + geom_point()
mod3 = ggplot(mydata, aes(UrbanPop, Murder, color = as.factor(fit$cluster))) + geom_point()
grid.arrange(mod1, mod2, mod3)

# c. Visualizando os valores medios de cada Cluster
#atributo predict
mydata$predict = fit$cluster
par(mfrow=c(2, 2))
for (i in 1:4){
  main_ = paste('Group =', i)
  barplot(sapply(mydata[mydata$predict==i,-5],mean),main=main_)
}

# d. Visualizando o Cluster para a diferentes pares de variaveis e suas distribuicoes 
ggpairs(cbind(mydata, Cluster=as.factor(fit$cluster)),
        columns=1:4, aes(colour=Cluster, alpha=0.5),
        lower=list(continuous="points"),
        upper=list(continuous="blank"),
        axisLabels="none", switch="both")

# 4. PAM K MEDOIDES Q6
# para reestabelecer somente os valores de Murder, Assault, UrbanPop, Rape 
mydata_pam = mydata[,-c(5)] # retira o valor predict acrescentado anteriormente 
set.seed(1987) 
fit = pam(mydata_pam,4)

# Compare PAM e Kmeans
table(fit$cluster, mydata$predict)
ss <- silhouette(fit$cluster, dist(mydata_pam))
par(mfrow=c(1, 1))
plot(ss)
mean(ss[,3])

# 5. CLUSTER HIERARQUICO HCLUST Q7 Q8 Q9
# para reestabelecer somente os valores de Murder, Assault, UrbanPop, Rape
mydata_hclu = mydata[,-c(5)] # retira o valor predict acrescentado anteriormente 

set.seed(1987) 
d <- dist(mydata_hclu, method = "euclidean") # distance matrix

# ATENCAO: altere o codigo para escolha de um metodo e execute um metodo por
# vez escolhendo o melhor particionamento
fit <- hclust(d, method = "complete")

# fit <- hclust(d, method = "single")
# fit <- hclust(d, method = "average")
# A seguir repetem-se os mesmos procedimentos empregados para o K-medias:
# analise do Silhouette, Visualizacao dos resultados e um comparativo com o PAM. 
par(mfrow=c(1, 1))
plot(fit) # display dendogram

# cut tree into 4 clusters
groups <- cutree(fit, k=4)

# draw dendogram with red borders around the 4 clusters
rect.hclust(fit, k=4, border="red")

# Silhouette
ss = silhouette(groups, dist(mydata_hclu))
plot(ss)
mean(ss[,3])
# Compare aqui agrupamentos (PAM, hclust) e (Kmeans, hclust) a
# exemplo codigo acima em que comparamos (PAM, Kmeans)
# responda entao a questao 9
# o codigo para essa questao nao e fornecido

set.seed(1987)
# see results like kmeans
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

# 6. OUTROS METODOS E DISCUSSAO Q10
mydata = mydata[,-c(5)] # retira o valor predict acrescentado anteriormente

set.seed(1987) 
fviz_nbclust(mydata, kmeans, method = "silhouette")
# Veja no help(fviz_nbclust) o que a funcao abaixo faz e como alterar o
# parametro de kmeans para o cluster hierarquico (nao e hclust! ;-) ) 

set.seed(1987)

fviz_nbclust(
  mydata,
  FUNcluster = kmeans,
  method = c("silhouette", "wss", "gap_stat"),
  diss = NULL,
  k.max = 20,
  nboot = 100,
  verbose = interactive(),
  barfill = "steelblue",
  barcolor = "steelblue",
  linecolor = "steelblue",
  print.summary = TRUE
)


####################
