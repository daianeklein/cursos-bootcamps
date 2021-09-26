library(e1071)
library(ggplot2) 

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

# missing values
sapply(wdbc, function(wdbc){ sum(is.na(wdbc)==T)/length(wdbc) })
any(is.na(wdbc))

# dtypes
unlist(lapply(wdbc,class))

## Q2
mybreast = wdbc[ , -which(names(wdbc) %in% c("patientid"))]
summary(mybreast) #Q3

# Observe as quantidades de registros Benignos e Malignos
summary(mybreast$outcome)

# Construa os dados de Treinamento e Teste (Teste com 30% dos dados (round))
T <- sample(1:nrow(mybreast),round(nrow(mybreast) * 0.30))

my_breast_train <- mybreast[-T,]
my_breast_test <- mybreast[T,]

dim(mybreast)
dim(my_breast_train)
dim(my_breast_test)

###############################

svm_radial = svm(formula = outcome ~ ., data = my_breast_train, 
          scale = TRUE, 
          kernel = 'radial')
print(svm_radial)
summary(svm_radial)

###############################

svm_polynomial = svm(formula = outcome ~ ., data = my_breast_train, 
                 scale = TRUE, 
                 kernel = 'polynomial')
print(svm_polynomial)
summary(svm_polynomial)

###############################

svm_linear = svm(formula = outcome ~ ., data = my_breast_train, 
                     scale = TRUE, 
                     kernel = 'linear')
print(svm_linear)
summary(svm_linear)

##
svm_sigmoid2 = svm(outcome ~ ., data = my_breast_train, 
                  scale = TRUE, 
                  kernel = 'sigmoid'
                  )
print(svm_linear)
print(svm_sigmoid2)

###############################

pred_radial = predict(svm_radial, newdata = my_breast_test$outcome)
cat('Radial:', table(pred_radial)[1]/sum(table(pred_radial))*100, ' %')

pred_polynomial = predict(svm_polynomial, my_breast_test$outcome)
cat('Polynomial:', table(pred_polynomial)[1]/sum(table(pred_polynomial))*100, ' %')

pred_linear = predict(svm_linear, my_breast_test$outcome)
cat('Linear:', table(pred_linear)[1]/sum(table(pred_linear))*100, ' %')

pred_sigmoid2 = predict(svm_sigmoid2, my_breast_test$outcome)
cat('Sigmoid:', table(pred_sigmoid2)[1]/sum(table(pred_sigmoid2))*100, ' %')

###############################


