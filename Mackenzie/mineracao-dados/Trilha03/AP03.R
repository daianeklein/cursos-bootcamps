library(e1071)
library(party)

mu = read.csv("https://www.openml.org/data/get_csv/24/dataset_24_mushroom.arff",
                  header=T,
                  stringsAsFactors=TRUE)

head(mu)

RNGversion("3.5.2")
set.seed(1987)

# Elimina valores NA
mu[mu[]=="?"]=NA
mu=na.omit(mu)

# Missing values
any(is.na(mu))
is.null(mu)

# treinamento e teste
L <- sample(1:nrow(mu),round(nrow(mu)/3))
train <- mu[-L,]
test <- mu[L,]

# Naive Bayes 
fitBayes = naiveBayes(class~.,data=train,laplace=1)

# predict 
predBayes = predict(fitBayes, test)
predBayes

# matriz de confusao
c_matrix = table(predBayes,test$class)
print(c_matrix)

cat('Accuracy Bayes: ', sum(diag(c_matrix))/sum(c_matrix)*100, ' %', "\n")

########### Decision Tree

#Descision Tree 
fitTree = ctree(class~.,data=train)

# predict 
predTree = predict(fitTree, test)
predTree

# matriz de confus�o
c_matrix = table(predTree,test$class)
print(c_matrix)

cat('Accuracy Dtree: ', sum(diag(c_matrix))/sum(c_matrix)*100, ' %', "\n")

# visualizacao
plot(fitTree)
