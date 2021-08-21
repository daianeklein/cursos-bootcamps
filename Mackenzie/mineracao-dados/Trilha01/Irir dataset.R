library(datasets)
library(knitr)
library(class)
library(tidyverse)

#install.packages('GGally')
library(GGally)

#dataset
data("iris")
summary(iris)

head(iris)
tail(iris)

## split to test and train
set.seed(823)
split <- sample.split(iris, SplitRatio = 0.70)
train <- subset(iris, split == "TRUE")
test <- subset(iris, split == "FALSE")
str(train)
str(test)

