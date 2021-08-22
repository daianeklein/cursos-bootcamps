library(datasets)
library(knitr)
library(class)
library(tidyverse)
library(MASS)
library(caTools)
library(caret)

#install.packages("imputeTS")
library(imputeTS)

#install.packages('GGally')
library(GGally)

#dataset
data(biopsy)
summary(biopsy)

head(biopsy)
tail(biopsy)

# checking missing values
sapply(biopsy, function(biopsy){ sum(is.na(biopsy)==T)/length(biopsy) })
df <- na.omit(biopsy)

#checking classes
table(df$class)

## split to test and train
split <- sample.split(df, SplitRatio = 0.70)
train <- subset(df, split == "TRUE")
test <- subset(df, split == "FALSE")
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
predictedSpeciesKnn = knn(train = subset(trainknn, select = - c(class)),
                          test = subset(testknn, select = - c(class)),
                          cl = trainknn$class,
                          k = 5,
                          prob = TRUE)

misClassError <- mean(predictedSpeciesKnn != test$class)
print(paste('Accuracy =',1-misClassError))

##k == 10
predictedSpeciesKnn = knn(train = subset(trainknn, select = - c(class)),
                          test = subset(testknn, select = - c(class)),
                          cl = trainknn$class,
                          k = 10,
                          prob = TRUE)

misClassError <- mean(predictedSpeciesKnn != test$class)
print(paste('Accuracy =',1-misClassError))

##k == 12
predictedSpeciesKnn = knn(train = subset(trainknn, select = - c(class)),
                          test = subset(testknn, select = - c(class)),
                          cl = trainknn$class,
                          k = 12,
                          prob = TRUE)

misClassError <- mean(predictedSpeciesKnn != test$class)
print(paste('Accuracy =',1-misClassError))

## k == 20
predictedSpeciesKnn = knn(train = subset(trainknn, select = - c(class)),
                          test = subset(testknn, select = - c(class)),
                          cl = trainknn$class,
                          k = 20,
                          prob = TRUE)

misClassError <- mean(predictedSpeciesKnn != test$class)
print(paste('Accuracy =',1-misClassError))

# Confusion Matrix
cm <- confusionMatrix(table(test$Species,test$predictedSpecies))
test$predictedSpecies <- as.factor(test$predictedSpecies)
table <- data.frame(confusionMatrix(test$Species, test$predictedSpecies)$table)
print(cm)