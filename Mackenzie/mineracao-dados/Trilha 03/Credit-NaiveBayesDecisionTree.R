#
# Atividade de Aprofundamento 
# Tarefa 1 = Naive Bayes e Decision Tree Credit Approval
#
# Esse codigo executa os modelos de Naive Bayes e Decision Tree para o 
# dataframe de Credit Approval. Empregue ele para responder a questao 1 do 
# questionario e faca a alteracoes necessarias no treinamento da Decision
# Tree para responder a questao 2.
#
# NAO E NECESSARIO POSTAR ESSE CODIGO do Credit Approval 
#
# Tarefa 2 = Naive Bayes e Decision Tree Mushrooms
#
# Empregue esse codigo como base para execucao dos modelos Naive Bayes e Decision Tree para o 
# dataframe mushrooms.
#
# O arquivo pode ser obtido em:
# https://www.openml.org/data/get_csv/24/dataset_24_mushroom.arff
# 
# Em seguida responda as quest�es de 3 a 10 do question�rio. 
#
# ATENCAO: E NECESSARIO POSTAR ESSE CODIGO do mushrooms! 
#


# Verifique outras libraries necess�rias na sua execu��o
library(e1071)
library(party)

credit = read.csv("https://www.openml.org/data/get_csv/29/dataset_29_credit-a.arff",
                  header=T,
                  stringsAsFactors=TRUE) # atualiza��o dos pacotes e1071 e party

# MANTER O SEED PARA GARANTIR AS RESPOSTAS DO QUESTION�RIO 
RNGversion("3.5.2")
set.seed(1987)

# Elimina valores NA
credit[credit[]=="?"]=NA
credit=na.omit(credit)

# Gera Conjuntos de Treinamento e Teste
L <- sample(1:nrow(credit),round(nrow(credit)/3))
train <- credit[-L,]
test <- credit[L,]

# Naive Bayes 

fitBayes = naiveBayes(class~.,data=train,laplace=1)

# predict Output 
predBayes = predict(fitBayes, test)
predBayes

# matriz de confus�o
c_matrix = table(predBayes,test$class)
print(c_matrix)

cat('Accuracy Bayes: ', sum(diag(c_matrix))/sum(c_matrix)*100, ' %', "\n")

# Descision Tree 
fitTree = ctree(class~.,data=train)

# predict Output 
predTree = predict(fitTree, test)
predTree

# matriz de confus�o
c_matrix = table(predTree,test$class)
print(c_matrix)

cat('Accuracy Dtree: ', sum(diag(c_matrix))/sum(c_matrix)*100, ' %', "\n")

plot(fitTree)


######## Decision tree II

credit2 = read.csv("https://www.openml.org/data/get_csv/29/dataset_29_credit-a.arff",
                   header=T,
                   stringsAsFactors=TRUE)

credit2 = credit2[, c('A9', 'A5', 'A10', 'A14', 'class')]

# treino e teste
L <- sample(1:nrow(credit2),round(nrow(credit2)/3))
train <- credit2[-L,]
test <- credit2[L,]

#decision tree
fitTree = ctree(class~., data = train)

# predict Output 
predTree = predict(fitTree, test)
predTree

# matriz de confus�o
c_matrix = table(predTree,test$class)
print(c_matrix)

cat('Accuracy Dtree: ', sum(diag(c_matrix))/sum(c_matrix)*100, ' %', "\n")

plot(fitTree)
