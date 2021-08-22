library(datasets)
library(knitr)
library(class)
library(tidyverse)
library(MASS)
library(caTools)
library(caret)


#install.packages('GGally')
library(GGally)

#dataset
data("iris")
summary(iris)

head(iris)
tail(iris)

# checking missing values
sapply(iris, function(iris){ sum(is.na(iris)==T)/length(iris) })

## split to test and train
set.seed(823)
split <- sample.split(iris, SplitRatio = 0.70)
train <- subset(iris, split == "TRUE")
test <- subset(iris, split == "FALSE")
str(train)
str(test)

# feature scaling
trainknn <- train
testknn <- test
ind <- sapply(trainknn, is.numeric)
trainknn[ind] <- lapply(trainknn[ind], scale)
ind <- sapply(testknn, is.numeric)
testknn[ind] <- lapply(testknn[ind], scale)

head(trainknn)

# finding the right K Value
# k == 5
predictedSpeciesKnn = knn(train = subset(trainknn, select = - c(Species)),
                          test = subset(testknn, select = - c(Species)),
                          cl = trainknn$Species,
                          k = 5,
                          prob = TRUE)

misClassError <- mean(predictedSpeciesKnn != test$Species)
print(paste('Accuracy =',1-misClassError))

##k == 10
predictedSpeciesKnn = knn(train = subset(trainknn, select = - c(Species)),
                          test = subset(testknn, select = - c(Species)),
                          cl = trainknn$Species,
                          k = 10,
                          prob = TRUE)

misClassError <- mean(predictedSpeciesKnn != test$Species)
print(paste('Accuracy =',1-misClassError))

##k == 15
predictedSpeciesKnn = knn(train = subset(trainknn, select = - c(Species)),
                          test = subset(testknn, select = - c(Species)),
                          cl = trainknn$Species,
                          k = 15,
                          prob = TRUE)

misClassError <- mean(predictedSpeciesKnn != test$Species)
print(paste('Accuracy =',1-misClassError))

test$predictedSpecies <- predictedSpeciesKnn

# Confusion Matrix
cm <- confusionMatrix(table(test$Species,test$predictedSpecies))
test$predictedSpecies <- as.factor(test$predictedSpecies)
table <- data.frame(confusionMatrix(test$Species, test$predictedSpecies)$table)
print(cm)
