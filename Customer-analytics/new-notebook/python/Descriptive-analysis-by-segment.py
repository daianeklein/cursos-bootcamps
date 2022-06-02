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




features = df[['Sex', 'Marital status', 'Age', 'Education', 'Income', 'Occupation', 'Settlement size']]
df_purchase_segm_std = scaler.transform(features)



# COMMAND ----------

# MAGIC %md ### PCA

# COMMAND ----------




df_purchase_segm_pca = pca.transform(df_purchase_segm_std)



# COMMAND ----------

# MAGIC %md ### K-Means PCA

# COMMAND ----------




purchase_segm_kmeans_pca = kmeans_pca.predict(df_purchase_segm_pca)




df_purchase_predictors = df.copy()




df_purchase_predictors['Segment'] = purchase_segm_kmeans_pca



# COMMAND ----------

# MAGIC %md ## DESCRIPTIVE ANALYSIS BY SEGMENTS

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### By Customer

# COMMAND ----------




df_purchase_predictors.head()




temp1 = df_purchase_predictors[['ID', 'Incidence']].groupby(['ID'], as_index = False).count()
temp1 = temp1.set_index('ID')
temp1 = temp1.rename(columns = {'Incidence': 'N_Visits'})
temp1.head()




temp2 = df_purchase_predictors[['ID', 'Incidence']].groupby(['ID'], as_index = False).sum()
temp2 = temp2.set_index('ID')
temp2 = temp2.rename(columns = {'Incidence': 'N_Purchases'})
temp3 = temp1.join(temp2)
temp3.head()




temp3['Average_N_Purchases'] = temp3['N_Purchases'] / temp3['N_Visits']
temp3.head()




temp4 = df_purchase_predictors[['ID', 'Segment']].groupby(['ID'], as_index = False).mean()
temp4 = temp4.set_index('ID')
df_purchase_descr = temp3.join(temp4)




df_purchase_descr.head()



# COMMAND ----------

# MAGIC %md ### Segment Proportions

# COMMAND ----------




segm_prop = df_purchase_descr[['N_Purchases', 'Segment']].groupby(['Segment']).count() / df_purchase_descr.shape[0]
segm_prop = segm_prop.rename(columns = {'N_Purchases': 'Segment Proportions'})
segm_prop.head()




plt.figure(figsize = (9, 6))
plt.pie(segm_prop['Segment Proportions'],
        labels = ['Standard', 'Career-Focused', 'Fewer-Opportunities', 'Well-Off'],
        autopct = '%1.1f#%%', 
        colors = ('b', 'g', 'r', 'orange'))
plt.title('Segment Proportions')


# In[ ]:




