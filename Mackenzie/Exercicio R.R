require(dplyr)
library(plyr)

# dataset
train <- read.csv('/Users/daianeklein/Documents/Mackenzie/Documentos/Disciplinas/Módulo 03/Estatística/Aprofundamento 06/regr_logistica_titanic_dw_train.csv') 
test <- read.csv('/Users/daianeklein/Documents/Mackenzie/Documentos/Disciplinas/Módulo 03/Estatística/Aprofundamento 06/regr_logistica_titanic_dw_test.csv')

# Selecionando as variáveis de interesse
train <- select(train, c('PassengerId','Survived'	,'Pclass',	'Sex'	,'Age',	'SibSp'	,'Parch'	,'Fare',	'Embarked'))
test <- select(test, c('PassengerId','Pclass',	'Sex'	,'Age',	'SibSp'	,'Parch'	,'Fare',	'Embarked'))

# Tipos de variáveis
unlist(lapply(train,class))

# null values
colSums(is.na(train))
colSums(is.na(test))

#preenchendo valores nulos com a media - variáveis numéricas
train$Age[is.na(train$Age)] = mean(train$Age, na.rm = TRUE)
test$Age[is.na(test$Age)] = mean(test$Age, na.rm = TRUE)

train$Fare[is.na(train$Fare)] = mean(train$Fare, na.rm = TRUE)
test$Fare[is.na(test$Fare)] = mean(test$Fare, na.rm = TRUE)

# Contando qt. de vezes de cada elemento
table(train$Embarked)

#removendo os demais valores faltantes
train <- na.omit(train)
test <- na.omit(test)

# Regressão Logística
# Mod01
mod01 = glm(Survived~. - PassengerId, data = train, family = binomial(link="logit"))
summary(mod01)

# Regressão Logística
# Mod02
mod02 = glm(Survived~. - Parch - PassengerId , data = train, family = binomial(link="logit"))
summary(mod02)

# Regressão Logística
# Mod03
mod03 = glm(Survived~. - Fare - Parch - PassengerId, data = train, family = binomial(link="logit"))
summary(mod03)

# Regressão Logística
# Mod04
mod04 = glm(Survived~. - Fare - Parch - PassengerId -Embarked, data = train, family = binomial(link="logit"))
summary(mod04)

# Acurácia
# matriz
score01 = predict(mod04, type = 'response')
table(train$Survived, score01 >= 0.5)

acuracia = (228 + 473) / nrow(train)
s1 = 228 / (228 + 107)
s2 = 473 / (473 + 82)

acuracia

# Acurácia 04
# matriz
score01 = predict(mod01, type = 'response')
table(train$Survived, score01 >= 0.5)

acuracia04 = (232 + 473) / nrow(train)
s1 = 232 / (232 + 103)
s2 = 473 / (473 + 82)

acuracia04