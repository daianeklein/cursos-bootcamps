#
# Atividade de Aprofundamento 
# Tarefa 3 = Logit Japan Credit Bank
#
# Empregue a base
# http://archive.ics.uci.edu/ml/datasets/credit+approval
#
# Antes de iniciar explore a documenta��o da base de dados no site.
#
# Altere o c�digo abaixo para avaliar a acuracidade do modelo log�stico
# empregando 20 parti��es sobre os dados (com 5 repeti��es).
#
# Em seguida responda a quest�es de 5 a 10 do question�rio e POSTE SEU C�DIGO 
#
# As quest�es 5 a 7 correspondem a quest�es sobre prepara��o dos dados
# As quest�es 8 a 10 do modelo logistico e ROC
#
# dica: empregue o c�digo da tarefa 2 como exemplo 
#
install.packages("ROCR")
install.packages("dummies")
install.packages("caret") 
install.packages("e1071") 
library(ROCR)
library(dummies)
library(caret) # for Cross Validation functions
library(e1071)

# Leia os dados de 
# https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data
#
# dica: os dados n�o possuem cabe�alho
credit = read.table('https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data', header= F,
                sep = ',')
head(credit)

cat("credit - rows and columns dataset:", nrow(credit) ," rows ", ncol(credit), "columns ", "\n")

# Elimine as linha com valores ausentes "?"
# dica: primeiro troque os valores "?" por NA e em seguida use na.omit() 

# checando valores nulos
sapply(credit, function(credit){sum(is.na(credit) == T)/length(credit)})

is.null(credit)
dim(credit)

credit[credit[]=="?"] <- NA
credit = na.omit(credit)
dim(credit)

# Valores num�ricos com NA aparecem como caracteres. Converta esses valores
# para num�rico com as.numeric (V2, V14)  

# types
unlist(lapply(credit,class))

credit$V2 = sapply(credit$V2, as.numeric)
credit$V14 = sapply(credit$V14, as.numeric)

# types
unlist(lapply(credit,class))

# Converta o atributo de classe para valores 0 e 1
#
credit$V16 
credit$V16 = ifelse(credit$V16 == "+", 0, 1)
credit$V16 

cat("credit - rows and columns after NA omit:", nrow(credit) ," rows ", ncol(credit), "columns ", "\n")

# Aplique o dummy encode para todos os atributos categ�ricos
# 
# dica: empregue o comando dummy da library(dummies)
#

unlist(lapply(credit,class)) #V1, V3, V5, V6, V7, V9, V10, V12, V13

credit= dummy.data.frame(credit, sep = "_")
credit

cat("credit - rows and columns after dummy encode:", nrow(credit) ," rows ", ncol(credit), "columns ", "\n")

#
# Logit com Cross Validation 
# dica: empregue o c�digo da tarefa 2 como exemplo  
#

# Crie o arquivo de controle para 20 parti��es dos dados e 5 repeti�oes 
ctrl <- trainControl(method="repeatedcv", number= 20, repeats=5)

# Fa�a o treinamento logistico, nao esquecer de empregar preProcess = c("center", "scale")
fit <- train(V16 ~ ., data=credit,
             method="glm", 
             family="binomial",
             trControl=ctrl, 
             preProcess = c("center", "scale"))
fit

# Fa�a a predi��o para todos os valores de credit
predict_test = predict(fit, newdata=credit, type="raw")

# Converte predict_test para valores 0 e 1 
predict_test = ifelse(predict_test > 0.5, 1, 0)

# Construa a matriz de confus�o 
c_matrix = table(credit$V16, predict_test)
print(c_matrix)

# Calcula a acuracidade 
acc = sum(diag(c_matrix))/sum(c_matrix) * 100
cat('Accuracy: ', acc, ' %', "\n")

# Plot da curva ROC
pr=prediction(as.numeric(predict_test),credit$V16) 
prf=performance(pr, measure="tpr", x.measure="fpr")
plot(prf,colorize=TRUE)

# Calcule a �rea sob a curva ROC
auc=performance(pr, measure="auc")
auc=auc@y.values[[1]]
auc
