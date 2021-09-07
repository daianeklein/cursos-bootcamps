### k-means
library(cluster)
par(mar=c(1,1,1,1))


idade = c(20, 27, 21, 20, 35, 55, 65, 42, 34, 56, 69, 18, 19, 21, 28, 32, 37, 42)
salario = c(1000, 1200, 2900, 1400, 4899, 5000, 3670, 1200, 5383, 7649,1000,
            4000, 4399, 2900, 3877, 9300, 9459, 1500)

base = data.frame(idade, salario)
plot(idade, salario)

kmeans = kmeans( x = base, centers = 3)

centroides = kmeans$centers
centroides

previsoes = kmeans$cluster
previsoes

clusplot(base,previsoes, xlab = "Salario", ylab = "Idade",
         main = "Agrupamento Salario x Idade",
         lines = 0, shape = TRUE, color = TRUE, labels = 2)


#############################################

### k-means
library(cluster)
par(mar=c(1,1,1,1))


idade = c(20, 27, 21, 20, 35, 55, 65, 42, 34, 56, 69, 18, 19, 21, 28, 32, 37, 42)
salario = c(1000, 1200, 2900, 1400, 4899, 5000, 3670, 1200, 5383, 7649,1000,
            4000, 4399, 2900, 3877, 9300, 9459, 1500)

base = data.frame(idade, salario)

base = scale(base)
plot(idade, salario)

kmeans = kmeans( x = base, centers = 3)

centroides = kmeans$centers
centroides

previsoes = kmeans$cluster
previsoes

clusplot(base,previsoes, xlab = "Salario", ylab = "Idade",
         main = "Agrupamento Salario x Idade",
         lines = 0, shape = TRUE, color = TRUE, labels = 2)

#############################################

lista = c(11, 11, 12, 12, 12, 12, 13, 13, 16, 17, 18, 19, 20)

kmeans2 = kmeans (x = lista, centers = 2)
kmeans2

#############################################

# IRIS
base = iris
#View(base)

base2 = base[1:2]
kmeans = kmeans(x = base2, centers = 3)

previsoes = kmeans$cluster

clusplot(base2, previsoes, color = TRUE)

table(base$Species, previsoes)

##############################################

path = "/Users/daianeklein/Downloads/Machine Learning e Data Science com R/Machine Learning e Data Science com R/agrupamento/credit_card_clients.csv"
base = read.csv(path, header = TRUE)
                   
dim(base)

#View(base3)

base$BILL_TOTAL = base$BILL_AMT1 + base$BILL_AMT2 + base$BILL_AMT3 + base$BILL_AMT4 + base$BILL_AMT5 + base$BILL_AMT6

X = data.frame(limite = base$LIMIT_BAL, gasto  = base$BILL_TOTAL)
X = scale(X)

# elbow method
set.seed(1)
wcss = vector()

for (i in 1:10){
  kmeans = kmeans(x = X, centers = i)
  wcss[i] = sum(kmeans$withinss)
  
}
wcss


plot(1:10, wcss, type = 'b', xlab = 'Clusters', ylab = 'WCSS')

## kmeans
set.seed(1)
kmeans = kmeans(x = X, centers = 5)
previsoes = kmeans$cluster

plot(X, col = previsoes)