# Databricks notebook source
#!/usr/bin/env python
# coding: utf-8


# COMMAND ----------

# MAGIC %md ## ${\textbf{Libraries}}$

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

# MAGIC %md ## ${\textbf{Data Import}}$

# COMMAND ----------




df_purchase = pd.read_csv('purchase data.csv')



# COMMAND ----------

# MAGIC %md ## ${\textbf{Data Exploration}}$

# COMMAND ----------




df_purchase.head()




df_purchase.isnull().sum()



# COMMAND ----------

# MAGIC %md ## ${\textbf{Data Segmentation}}$

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### ${\textbf{Import Segmentation Model}}$

# COMMAND ----------




scaler = pickle.load(open('scaler.pickle', 'rb'))




pca = pickle.load(open('pca.pickle', 'rb'))




kmeans_pca = pickle.load(open('kmeans_pca.pickle', 'rb'))



# COMMAND ----------

# MAGIC %md ### ${\textbf{Standardization}}$

# COMMAND ----------




features = df_purchase[['Sex', 'Marital status', 'Age', 'Education', 'Income', 'Occupation', 'Settlement size']]
df_purchase_segm_std = scaler.transform(features)



# COMMAND ----------

# MAGIC %md ### ${\textbf{PCA}}$

# COMMAND ----------




df_purchase_segm_pca = pca.transform(df_purchase_segm_std)



# COMMAND ----------

# MAGIC %md ### ${\textbf{K-means PCA}}$

# COMMAND ----------




purchase_segm_kmeans_pca = kmeans_pca.predict(df_purchase_segm_pca)




df_purchase_predictors = df_purchase.copy()




df_purchase_predictors['Segment'] = purchase_segm_kmeans_pca



# COMMAND ----------

# MAGIC %md ## ${\textbf{Descriptive Analysis by Segments}}$

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### ${\textbf{Data Analysis by Customer}}$

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

# MAGIC %md ### ${\textbf{Segment Proportions}}$

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



# COMMAND ----------

# MAGIC %md ### ${\textbf{Purchase Occasion and Purchase Incidence}}$

# COMMAND ----------




segments_mean = df_purchase_descr.groupby(['Segment']).mean()
segments_mean




segments_std = df_purchase_descr.groupby(['Segment']).std()




plt.figure(figsize = (9, 6))
plt.bar(x = (0, 1, 2, 3),
        tick_label = ('Standard', 'Career-Focused', 'Fewer-Opportunities', 'Well-Off'), 
        height = segments_mean['N_Visits'],
        yerr = segments_std['N_Visits'],
        color = ('b', 'g', 'r', 'orange'))
plt.xlabel('Segment')
plt.ylabel('Number of Store Visits')
plt.title('Average Number of Store Visits by Segment')




plt.figure(figsize = (9, 6))
plt.bar(x = (0, 1, 2, 3),
        tick_label = ('Standard', 'Career-Focused', 'Fewer-Opportunities', 'Well-Off'), 
        height = segments_mean['N_Purchases'],
        yerr = segments_std['N_Purchases'],
        color = ('b', 'g', 'r', 'orange'))
plt.xlabel('Segment')
plt.ylabel('Purchase Incidences')
plt.title('Number of Purchases by Segment')




plt.figure(figsize = (9, 6))
plt.bar(x = (0, 1, 2, 3), 
        tick_label = ('Standard','Career Focused','Fewer Opportunities','Well-off'),
        height = segments_mean['Average_N_Purchases'], 
        yerr = segments_std['Average_N_Purchases'], 
        color = ('b', 'g', 'r', 'orange'))
plt.xlabel('Segment')
plt.ylabel('Purchase Incidences')
plt.title('Average Number of Purchases by Segment')



# COMMAND ----------

# MAGIC %md ### ${\textbf{Brand Choice}}$

# COMMAND ----------




df_purchase_incidence = df_purchase_predictors[df_purchase_predictors['Incidence'] == 1]




brand_dummies = pd.get_dummies(df_purchase_incidence['Brand'], prefix = 'Brand', prefix_sep = '_')
brand_dummies['Segment'], brand_dummies['ID'] = df_purchase_incidence['Segment'], df_purchase_incidence['ID']
brand_dummies




temp = brand_dummies.groupby(['ID'], as_index = True).mean()




mean_brand_choice = temp.groupby(['Segment'], as_index = True).mean()




sns.heatmap(mean_brand_choice,
            vmin = 0, 
            vmax = 1,
            cmap = 'PuBu',
            annot = True)
plt.yticks([0, 1, 2, 3], ['Standard', 'Career-Focused', 'Fewer-Opportunities', 'Well-Off'], rotation = 45, fontsize = 9)
plt.title('Average Brand Choice by Segment')
plt.show()



# COMMAND ----------

# MAGIC %md ### ${\textbf{Revenue}}$

# COMMAND ----------




temp = df_purchase_predictors[df_purchase_predictors['Brand'] == 1]
temp.loc[:, 'Revenue Brand 1'] = temp['Price_1'] * temp['Quantity']
segments_brand_revenue = pd.DataFrame()
segments_brand_revenue[['Segment', 'Revenue Brand 1']] = temp[['Segment', 'Revenue Brand 1']].groupby(['Segment'], as_index = False).sum()
segments_brand_revenue




temp = df_purchase_predictors[df_purchase_predictors['Brand'] == 2]
temp.loc[:, 'Revenue Brand 2'] = temp['Price_2'] * temp['Quantity']
segments_brand_revenue[['Segment', 'Revenue Brand 2']] = temp[['Segment', 'Revenue Brand 2']].groupby(['Segment'], as_index = False).sum()




temp = df_purchase_predictors[df_purchase_predictors['Brand'] == 3]
temp.loc[:,'Revenue Brand 3'] = temp['Price_3']*temp['Quantity']
segments_brand_revenue[['Segment','Revenue Brand 3']] = temp[['Revenue Brand 3','Segment']].groupby(['Segment'], as_index = False).sum()




temp = df_purchase_predictors[df_purchase_predictors['Brand'] == 4]
temp.loc[:,'Revenue Brand 4'] = temp['Price_4']*temp['Quantity']
segments_brand_revenue[['Segment','Revenue Brand 4']] = temp[['Revenue Brand 4','Segment']].groupby(['Segment'], as_index = False).sum()




temp = df_purchase_predictors[df_purchase_predictors['Brand'] == 5]
temp.loc[:,'Revenue Brand 5'] = temp['Price_5']*temp['Quantity']
segments_brand_revenue[['Segment','Revenue Brand 5']] = temp[['Revenue Brand 5','Segment']].groupby(['Segment'], as_index = False).sum()




segments_brand_revenue['Total Revenue'] = (segments_brand_revenue['Revenue Brand 1'] +
                                           segments_brand_revenue['Revenue Brand 2'] +
                                           segments_brand_revenue['Revenue Brand 3'] +
                                           segments_brand_revenue['Revenue Brand 4'] +
                                           segments_brand_revenue['Revenue Brand 5'] )
segments_brand_revenue




segments_brand_revenue['Segment Proportions'] = segm_prop['Segment Proportions']
segments_brand_revenue['Segment'] = segments_brand_revenue['Segment'].map({0:'Standard',
                                                                           1:'Career-Focused',
                                                                           2:'Fewer-Opportunities',
                                                                           3:'Well-Off'})
segments_brand_revenue = segments_brand_revenue.set_index(['Segment'])
segments_brand_revenue

