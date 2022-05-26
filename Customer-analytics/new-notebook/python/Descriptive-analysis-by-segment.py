# Databricks notebook source
#!/usr/bin/env python
# coding: utf-8


# COMMAND ----------

# MAGIC %md # DESCRIPTIVE ANALYSIS BY SEGMENT

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ## LIBS

# COMMAND ----------




import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

import pickle

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()



# COMMAND ----------

# MAGIC %md ## DATA IMPORT

# COMMAND ----------




df = pd.read_csv('purchase_data.csv')
df.head()




df.isnull().sum()



# COMMAND ----------

# MAGIC %md ## DATA SEGMENTATION

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### IMPORT SEGMENTATION MODEL

# COMMAND ----------




scaler = pickle.load(open('scaler.pickle', 'rb'))
pca = pickle.load(open('pca.pickle', 'rb'))
kmeans_pca = pickle.load(open('kmeans_pca.pickle', 'rb'))



# COMMAND ----------

# MAGIC %md ### STANDARDIZATION

# COMMAND ----------


# In[ ]:




