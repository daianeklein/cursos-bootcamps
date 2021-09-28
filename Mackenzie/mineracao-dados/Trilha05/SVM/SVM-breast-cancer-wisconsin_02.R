library(e1071)
library(ggplot2) 
library(factoextra)



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
T <- sample(1:nrow(mybreast),round(nrow(mybreast) * 0.3))

my_breast_train <- mybreast[-T,]
my_breast_test <- mybreast[T,]

dim(mybreast)
dim(my_breast_train)
dim(my_breast_test)

###############################

svm_radial <- svm(formula = outcome ~ ., data = my_breast_train, 
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
svm_sigmoid = svm(outcome ~ ., data = my_breast_train, 
                  scale = TRUE, 
                  kernel = 'sigmoid'
                  )
print(svm_linear)
print(svm_sigmoid)

###############################

pred_radial = predict(svm_radial, newdata = my_breast_test)
matriz_confusao = table(my_breast_test$outcome, pred_radial)
acc_radial = sum(diag(matriz_confusao))/sum(matriz_confusao) * 100

pred_polynomial = predict(svm_polynomial, my_breast_test)
matriz_confusao = table(my_breast_test$outcome, pred_polynomial)
acc_polynomial = sum(diag(matriz_confusao))/sum(matriz_confusao) * 100

pred_linear = predict(svm_linear, my_breast_test)
matriz_confusao = table(my_breast_test$outcome, pred_linear)
acc_linear = sum(diag(matriz_confusao))/sum(matriz_confusao) * 100

pred_sigmoid = predict(svm_sigmoid, my_breast_test)
matriz_confusao = table(my_breast_test$outcome, pred_sigmoid)
acc_sigmoid = sum(diag(matriz_confusao))/sum(matriz_confusao) * 100

acc_radial
acc_polynomial
acc_linear
acc_sigmoid


###############################

# Construindo my_breast em PC

#A entrada tem de eliminar 
# o atributo "outcome". Ele nao numerico e a classe de treinamento, 
# nao eh portanto um atributo para reducao a componentes principais

# princomp class
breast_pc = princomp( mybreast[,-1] , cor=TRUE)

## variancia acumulada
## primeira variável == 44%, segunda 63% e assim por diante
get_eigenvalue(breast_pc)

## plotando % variance
## kaiser's rule
fviz_eig(breast_pc, addlabels = TRUE, linecolor = "Red", ylim = c(0, 50))

biplot(breast_pc)
summary(breast_pc)


# Os scores s�o os novos atributos com base em componentes principais.
# Construa agora a base com os componentes principais, adicionado o atributo classe 
breast_col_pc = data.frame(breast_pc$scores) 

# vamos readicionar o aributo classe "outcome" 
breast_col_pc = cbind(wdbc$outcome,breast_col_pc)
names(breast_col_pc)[1] = "outcome"

colnames(breast_col_pc)

# Passo 2. � classificar os dados com base nos Componentes Principais
# Vamos primeiramente empregar 3 componentes, em seguida 7 

# Construindo os conjuntos de treinamento e teste...
# Empregar a mesma sele��o de dados T empregada anteriormente 
my_breast_col_pc_train <- breast_col_pc[-T,] 
my_breast_col_pc_test <- breast_col_pc[T,]

my_breast_col_pc_train_3 = my_breast_col_pc_train[,c(1:4)]
colnames(my_breast_col_pc_train_3)

# Treinamento da SVM com os dados de treinamento para 3 componentes 
# Vamos empregar somente o kernel com base radial

svm_3 <- svm(outcome ~ ., data = my_breast_col_pc_train_3, 
             scale = TRUE, kernel ="radial")

print(svm_3)
summary(svm_3)

# predicao conjunto de teste
predict_teste = predict(svm_3, newdata = my_breast_col_pc_test)
matriz_confusao = table(my_breast_col_pc_test$outcome, predict_teste)
acc = sum(diag(matriz_confusao))/sum(matriz_confusao) * 100
print(acc)

#### 7 
my_breast_col_pc_train_7 = my_breast_col_pc_train[,c(1:8)]
colnames(my_breast_col_pc_train_7)

# Treinamento da SVM com os dados de treinamento para 3 componentes 
# Vamos empregar somente o kernel com base radial

svm_7 <- svm(outcome ~ ., data = my_breast_col_pc_train_7, 
             scale = TRUE, kernel ="radial")

print(svm_7)
summary(svm_7)

# predicao conjunto de teste
predict_teste = predict(svm_7, newdata = my_breast_col_pc_test)
matriz_confusao = table(my_breast_col_pc_test$outcome, predict_teste)
acc_2 = sum(diag(matriz_confusao))/sum(matriz_confusao) * 100
print(acc_2)

##10
print(acc - acc_2)
