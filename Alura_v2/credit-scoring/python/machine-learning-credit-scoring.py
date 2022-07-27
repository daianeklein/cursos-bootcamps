# Databricks notebook source
#!/usr/bin/env python
# coding: utf-8


# COMMAND ----------

# MAGIC %md # Libs

# COMMAND ----------




import pandas as pd


# In[ ]:






# COMMAND ----------

# MAGIC %md # DATASET

# COMMAND ----------




df = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/credit_scoring/main/base_dados_traduzida.csv')
df.head()


# In[ ]:




