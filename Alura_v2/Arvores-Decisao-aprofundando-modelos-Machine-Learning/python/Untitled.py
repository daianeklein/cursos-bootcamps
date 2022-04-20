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
import sklearn.model_selection 



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


# In[ ]:




