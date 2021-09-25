# library
library(e1071)
library(ggplot2)
library(caret)

#seed
RNGversion("3.5.2")
set.seed(1987)

# read breast-cancer-wisconsin
wdbc = read.csv(
  "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data",
  col.names=c(
    "patientid",
    "outcome",
    "radius_mean",
    "texture_mean",
    "perimeter_mean",
    "area_mean",
    "smoothness_mean",
    "compactness_mean",
    "concavity_mean",
    "concavepoints_mean",
    "symmetry_mean",
    "fractaldimension_mean",
    "radius_error",
    "texture_error",
    "perimeter_error",
    "area_error",
    "smoothness_error",
    "compactness_error",
    "concavity_error",
    "concavepoints_error",
    "symmetry_error",
    "fractaldimension_error",
    "radius_worst",
    "texture_worst",
    "perimeter_worst",
    "area_worst",
    "smoothness_worst",
    "compactness_worst",
    "concavity_worst",
    "concavepoints_worst",
    "symmetry_worst",
    "fractaldimension_worst"))

wdbc = as.data.frame(unclass(wdbc),stringsAsFactors=T)

head(wdbc)
summary(wdbc)
summary(wdbc$outcome)

# missing values
sapply(wdbc, function(wdbc){ sum(is.na(wdbc)==T)/length(wdbc) })
any(is.na(wdbc))

# dtypes
unlist(lapply(wdbc,class))

## Q2
mybreast = wdbc[ , -which(names(wdbc) %in% c("patientid"))]
summary(mybreast) #Q3

## Anomaly Detection
## outcome para numerico
mybreast$outcome = as.factor(as.numeric(mybreast$outcome) - 1)
summary(mybreast$outcome)

# benignos e malignos
mybreast_M = mybreast[mybreast$outcome %in% c(1), ]
mybreast_B = mybreast[mybreast$outcome %in% c(0), ]

summary(mybreast_B$outcome)
summary(mybreast_M$outcome)

nrow(mybreast_B) 
nrow(mybreast_M)

svm = svm(formula = outcome ~ ., data = mybreast_B, 
          scale = TRUE, 
          kernel = 'radial',
          type="one-classification")
print(svm)


########

svm02 = svm(outcome ~ ., data = mybreast_B, 
            scale = TRUE, 
            kernel = 'radial',
            type="one-classification")

print(svm02)


pred = predict(svm02, mybreast_M[,-c(1)])
matriz_confusao = table(mybreast_M$outcome,pred)
matriz_confusao

################

svm02 = svm(outcome ~ ., data = mybreast_B, 
            scale = TRUE, 
            kernel = 'linear',
            type="one-classification")

print(svm02)

predict_test = predict(svm02, mybreast_M[,-c(1)])
matriz_confusao = table(mybreast_M$outcome,predict_test)
matriz_confusao
cat('Anomaly Detected (FALSE):', table(predict_test)[1]/sum(table(predict_test))*100, ' %')

##radial: 99,052%
##sigmoid: 82,46%
## linear:20,37%


###########

svm02 = svm(outcome ~ ., data = mybreast, 
            scale = TRUE, 
            kernel = 'radial'
            )

print(svm02)

predict_test_2 = predict(svm02, mybreast_M[,-c(1)])
matriz_confusao = table(mybreast_M$outcome,predict_test_2)
matriz_confusao
cat('Anomaly Detected:', table(predict_test_2)[1]/sum(table(predict_test_2))*100, ' %')

###########



rm(list = ls())



