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

# class
table(biopsy$class)

#checking missing values
sapply(biopsy, function(biopsy){ sum(is.na(biopsy)==T)/length(biopsy) })

# drop ID column
biopsy <- subset(biopsy, select = -c(ID))

# removing missing values
biopsy <- na.omit(biopsy)

dim(biopsy)

# train == 100
acc = c(1:100)*0
for (i in c(1:100)){
  L = sample(1:nrow(biopsy),round(nrow(biopsy)/3))
  train <- biopsy[-L, 1:9]
  test <- biopsy[L, 1:9]
  cl <- factor(biopsy[-L, 10])
  fit <- knn(train, test, cl, k = 5)
  c_matrix = table(fit[1:length(L)], factor(biopsy[L, 10]))
  acc[i] = sum(diag(c_matrix))/sum(c_matrix)
}

mean(acc)
# 0.9692544
# 0.969386
# 0.9701754
# 0.9724123


############
# MOD 02
############

df <- subset(biopsy, select = -c(V6))


# train == 100
acc = c(1:100)*0
for (i in c(1:100)){
  L = sample(1:nrow(df),round(nrow(df)/3))
  train <- df[-L, 1:8]
  test <- df[L, 1:8]
  cl <- factor(df[-L, 9])
  fit <- knn(train, test, cl, k = 5)
  c_matrix = table(fit[1:length(L)], factor(df[L, 9]))
  acc[i] = sum(diag(c_matrix))/sum(c_matrix)
}

mean(acc)


############
# MOD 03
############

df2 <- na.omit(biopsy)


# train == 100
# k =2
acc = c(1:100)*0
for (i in c(1:100)){
  L = sample(1:nrow(df2),round(nrow(df2)/3))
  train <- df2[-L, 1:9]
  test <- df2[L, 1:9]
  cl <- factor(df2[-L, 10])
  fit <- knn(train, test, cl, k = 2)
  c_matrix = table(fit[1:length(L)], factor(df2[L, 10]))
  acc[i] = sum(diag(c_matrix))/sum(c_matrix)
}

mean(acc) # 0.9603947

# train == 100
# k = 5
acc = c(1:100)*0
for (i in c(1:100)){
  L = sample(1:nrow(df2),round(nrow(df2)/3))
  train <- df2[-L, 1:9]
  test <- df2[L, 1:9]
  cl <- factor(df2[-L, 10])
  fit <- knn(train, test, cl, k = 5)
  c_matrix = table(fit[1:length(L)], factor(df2[L, 10]))
  acc[i] = sum(diag(c_matrix))/sum(c_matrix)
}

mean(acc) # 0.9725

# train == 100
# k = 12
acc = c(1:100)*0
for (i in c(1:100)){
  L = sample(1:nrow(df2),round(nrow(df2)/3))
  train <- df2[-L, 1:9]
  test <- df2[L, 1:9]
  cl <- factor(df2[-L, 10])
  fit <- knn(train, test, cl, k = 12)
  c_matrix = table(fit[1:length(L)], factor(df2[L, 10]))
  acc[i] = sum(diag(c_matrix))/sum(c_matrix)
}

mean(acc) #0.9662719


############
# MOD 04
############

df3 <- subset(biopsy, select = -c(V6))

# train == 100
# k =2
acc = c(1:100)*0
for (i in c(1:100)){
  L = sample(1:nrow(df3),round(nrow(df3)/3))
  train <- df3[-L, 1:8]
  test <- df3[L, 1:8]
  cl <- factor(df3[-L, 9])
  fit <- knn(train, test, cl, k = 2)
  c_matrix = table(fit[1:length(L)], factor(df3[L, 9]))
  acc[i] = sum(diag(c_matrix))/sum(c_matrix)
}

mean(acc) #0.9489912

# k = 5
acc = c(1:100)*0
for (i in c(1:100)){
  L = sample(1:nrow(df3),round(nrow(df3)/3))
  train <- df3[-L, 1:8]
  test <- df3[L, 1:8]
  cl <- factor(df3[-L, 9])
  fit <- knn(train, test, cl, k = 5)
  c_matrix = table(fit[1:length(L)], factor(df3[L, 9]))
  acc[i] = sum(diag(c_matrix))/sum(c_matrix)
}

mean(acc) #0.9592982

# k = 12
acc = c(1:100)*0
for (i in c(1:100)){
  L = sample(1:nrow(df3),round(nrow(df3)/3))
  train <- df3[-L, 1:8]
  test <- df3[L, 1:8]
  cl <- factor(df3[-L, 9])
  fit <- knn(train, test, cl, k = 12)
  c_matrix = table(fit[1:length(L)], factor(df3[L, 9]))
  acc[i] = sum(diag(c_matrix))/sum(c_matrix)
}

mean(acc) #0.959693
