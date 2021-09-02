base = read.csv("/Users/daianeklein/Documents/Mackenzie/Documentos/Disciplinas/Módulo 04/Mineração de Dados/Regressao Logistica/risco_credito.csv")

#separando risco moderado da base
base = base[base$c.risco != "moderado", ]

#regressao logistica
classificador = glm(formula = c.risco ~ ., family = binomial, data = base)

#prevendo
historia = c('boa', 'ruim')
divida = c('alta', 'alta')
garantias = c('nenhuma', 'adequada')
renda = c('acima_35', '0_15')
df = data.frame(historia, divida, garantias, renda)
df

probabilidades = predict(classificador, type = 'response', newdata = df)
probabilidades

resposta = ifelse(probabilidades > 0.5, 'baixo', 'alto')
resposta

#base de crédito
base = read.csv("/Users/daianeklein/Documents/Mackenzie/Documentos/Disciplinas/Módulo 04/Mineração de Dados/Regressao Logistica/credit_data.csv")
base

#removendo a coluna ID
base$i.clientid = NULL

# valores inconsistentes
base$age = ifelse(base$age < 0, 40.92, base$age)

#valores faltantes
base$age = ifelse(is.na(base$age), mean(base$age, na.rm = TRUE), base$age)

#escalonamento
base[, 1:3] = scale(base[, 1:3])

#divisao entre treinamento e teste
library(caTools)
set.seed(1)
divisao = sample.split(base$income, SplitRatio = 0.75)
base_treinamento = subset(base, divisao = TRUE)
base_teste = subset(base, divisao == FALSE)

classificador = glm(formula = c.default ~ ., family = binomial, data = base_treinamento)
classificador

probabilidades = predict(classificador, type = 'response', newdata = base_teste)
probabilidades

previsoes = ifelse(probabilidades > 0.5, 1, 0)
previsoes

matriz_confusao = table(base_teste[, 4], previsoes)
matriz_confusao

#install.packages('e1071', dependencies=TRUE)
library(caret)
library(e1071)


confusionMatrix(matriz_confusao)