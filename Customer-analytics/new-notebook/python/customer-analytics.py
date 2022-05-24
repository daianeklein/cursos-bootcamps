# Databricks notebook source
#!/usr/bin/env python
# coding: utf-8


# COMMAND ----------

# MAGIC %md # CUSTOMER ANALYTICS

# COMMAND ----------


# - Master beginner and advanced customer analytics
# 
# - Learn the most important type of analysis applied by mid and large companies
# 
# - Gain access to a professional team of trainers with exceptional quant skills
# 
# - Wow interviewers by acquiring a highly desired skill
# 
# - Understand the fundamental marketing modeling theory: segmentation, targeting, positioning, marketing mix, and price elasticity;
# 
# - Apply segmentation on your customers, starting from raw data and reaching final customer segments;
# 
# - Perform K-means clustering with a customer analytics focus;
# 
# - Apply Principal Components Analysis (PCA) on your data to preprocess your features;
# 
# - Combine PCA and K-means for even more professional customer segmentation;
# 
# - Deploy your models on a different dataset;
# 
# - Learn how to model purchase incidence through probability of purchase elasticity;
# 
# - Model brand choice by exploring own-price and cross-price elasticity;
# 
# - Complete the purchasing cycle by predicting purchase quantity elasticity
# 
# - Carry out a black box deep learning model with TensorFlow 2.0 to predict purchasing behavior with unparalleled accuracy
# 
# - Be able to optimize your neural networks to enhance results


# COMMAND ----------

# MAGIC %md # Libs

# COMMAND ----------




import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.preprocessing import StandardScaler

from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans

from sklearn.decomposition import PCA

import pickle



# COMMAND ----------

# MAGIC %md # Dataset

# COMMAND ----------




df_segmentation = pd.read_csv('data.csv')



# COMMAND ----------

# MAGIC %md # Analysis

# COMMAND ----------




df_segmentation.head()




df_segmentation.describe()



# COMMAND ----------

# MAGIC %md ### Correlation

# COMMAND ----------




df_segmentation.corr()




plt.figure(figsize = (12, 9))
s = sns.heatmap(df_segmentation.corr(),
               annot = True, 
               cmap = 'RdBu',
               vmin = -1, 
               vmax = 1)
s.set_yticklabels(s.get_yticklabels(), rotation = 0, fontsize = 12)
s.set_xticklabels(s.get_xticklabels(), rotation = 90, fontsize = 12)
plt.title('Correlation Heatmap')
plt.show()




# raw data
plt.figure(figsize = (12, 9))
plt.scatter(df_segmentation['Age'], df_segmentation['Income'])
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Visualization of raw data')



# COMMAND ----------

# MAGIC %md ## Standardization

# COMMAND ----------




scaler = StandardScaler()
segmentation_std = scaler.fit_transform(df_segmentation)



# COMMAND ----------

# MAGIC %md ## Hierarquical Clustering

# COMMAND ----------




hier_clust = linkage(segmentation_std, method = 'ward')




plt.figure(figsize = (12,9))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Observations')
plt.ylabel('Distance')
dendrogram(hier_clust,
           truncate_mode = 'level',
           p = 5,
           show_leaf_counts = False,
           no_labels = True)
plt.show()



# COMMAND ----------

# MAGIC %md ## K-means Clustering

# COMMAND ----------




wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(segmentation_std)
    wcss.append(kmeans.inertia_)




wcss




plt.figure(figsize = (10,8))
plt.plot(range(1, 11), wcss, marker = 'o', linestyle = '--')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('K-means Clustering')
plt.show()




kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
kmeans.fit(segmentation_std)



# COMMAND ----------

# MAGIC %md ### Results

# COMMAND ----------




kmeans.labels_




set(kmeans.labels_)




df_segm_kmeans = df_segmentation.copy()
df_segm_kmeans['Segment K-means'] = kmeans.labels_




df_segm_analysis = df_segm_kmeans.groupby(['Segment K-means']).mean()
df_segm_analysis




df_segm_analysis['N Obs'] = df_segm_kmeans[['Segment K-means','Sex']].groupby(['Segment K-means']).count()
df_segm_analysis['Prop Obs'] = df_segm_analysis['N Obs'] / df_segm_analysis['N Obs'].sum()




df_segm_analysis




# rename cluster
df_segm_analysis.rename({0:'well-off',
                         1:'fewer-opportunities',
                         2:'standard',
                         3:'career focused'})




df_segm_kmeans['Labels'] = df_segm_kmeans['Segment K-means'].map({0:'well-off', 
                                                                  1:'fewer opportunities',
                                                                  2:'standard', 
                                                                  3:'career focused'})




x_axis = df_segm_kmeans['Age']
y_axis = df_segm_kmeans['Income']
plt.figure(figsize = (10, 8))
sns.scatterplot(x = x_axis, y = y_axis, hue = df_segm_kmeans['Labels'], palette = ['g', 'r', 'c', 'm'])
plt.title('Segmentation K-means')
plt.show()



# COMMAND ----------

# MAGIC %md # PCA

# COMMAND ----------


# In[ ]:




