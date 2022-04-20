# Databricks notebook source
#!/usr/bin/env python
# coding: utf-8


# COMMAND ----------

# MAGIC %md # Árvores de Decisão: aprofundando em modelos de Machine Learning

# COMMAND ----------


# Faça esse curso de Data Science e:
# 
# - Identifique fraudes em cartões de crédito utilizando uma árvore de decisão
# - Entenda como funcionam as árvores de decisão
# - Crie diversos modelos de Machine Learning com o scikit-learn
# - Aprenda sobre as técnicas Bagging e Boosting
# - Explore o famoso algoritmo Random Forest por debaixo dos panos
# - Conheça o algoritmo AdaBoost em detalhes


# COMMAND ----------

# MAGIC %md # LIB'S

# COMMAND ----------




import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import StratifiedShuffleSplit
from sklearn import tree



# COMMAND ----------

# MAGIC %md # DATASET

# COMMAND ----------




df = pd.read_csv('/Users/daianeklein/Documents/DataScience/cursos-bootcamps/creditcard.csv')
df.head()



# COMMAND ----------

# MAGIC %md # DATA ANALYSIS

# COMMAND ----------




df.shape




# frauds
df['Class'].sum()




not_frauds = df[df['Class'] == 0].shape[0]
frauds = df[df['Class'] == 1].shape[0]

print(round((not_frauds / df.shape[0]) * 100, 2))
print(round((frauds / df.shape[0]) * 100,2))



# COMMAND ----------

# MAGIC %md # TRAIN AND TEST

# COMMAND ----------




def executar_validador(X, y):
    validador = StratifiedShuffleSplit(n_splits = 1,
                                    test_size = 0.1,
                                    random_state = 0)
    
    for treino_id, test_id in validador.split(X, y):
        X_train, X_test = X[treino_id], X[test_id]
        y_train, y_test = y[treino_id], y[test_id]
    
    return X_train, X_test, y_train, y_test




def executar_classificador(classificador, X_train,X_test, y_train):
    arvore = classificador_arvore_decisao.fit(X_train, y_train)
    y_pred = arvore.predict(X_test)
    return y_pred




def salvar_arvore(classificador, nome):
    plt.figure(figsize = (200, 100))
    tree.plot_tree(classificador, filled = True, fontsize = 14)
    plt.savefig(nome)
    plt.close()




#execucao do validador
X = df.drop('Class', axis = 1).values
y = df['Class'].values

X_train, X_test, y_train, y_test = executar_validador(X, y)

#execucao do classificador DecisionTreeClassifier
classificador_arvore_decisao = tree.DecisionTreeClassifier()

executar_classificador(classificador_arvore_decisao, X_train, X_test, y_train)
y_pred_arvore_decisao = executar_classificador(classificador_arvore_decisao, X_train, X_test, y_train)




salvar_arvore(classificador_arvore_decisao, 'arvore_decisao.png')


# In[ ]:




