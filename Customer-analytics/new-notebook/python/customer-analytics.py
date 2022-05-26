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


# In[ ]:


# raw data
plt.figure(figsize = (12, 9))
plt.scatter(df_segmentation['Age'], df_segmentation['Income'])
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Visualization of raw data')



# COMMAND ----------

# MAGIC %md ## Standardization

# COMMAND ----------


# In[ ]:


scaler = StandardScaler()
segmentation_std = scaler.fit_transform(df_segmentation)



# COMMAND ----------

# MAGIC %md ## Hierarquical Clustering

# COMMAND ----------


# In[ ]:


hier_clust = linkage(segmentation_std, method = 'ward')


# In[ ]:


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


# In[ ]:


wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(segmentation_std)
    wcss.append(kmeans.inertia_)


# In[ ]:


wcss


# In[ ]:


plt.figure(figsize = (10,8))
plt.plot(range(1, 11), wcss, marker = 'o', linestyle = '--')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('K-means Clustering')
plt.show()


# In[ ]:


kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
kmeans.fit(segmentation_std)



# COMMAND ----------

# MAGIC %md ### Results

# COMMAND ----------


# In[ ]:


kmeans.labels_


# In[ ]:


set(kmeans.labels_)


# In[ ]:


df_segm_kmeans = df_segmentation.copy()
df_segm_kmeans['Segment K-means'] = kmeans.labels_


# In[ ]:


df_segm_analysis = df_segm_kmeans.groupby(['Segment K-means']).mean()
df_segm_analysis


# In[ ]:


df_segm_analysis['N Obs'] = df_segm_kmeans[['Segment K-means','Sex']].groupby(['Segment K-means']).count()
df_segm_analysis['Prop Obs'] = df_segm_analysis['N Obs'] / df_segm_analysis['N Obs'].sum()


# In[ ]:


df_segm_analysis


# In[ ]:


# rename cluster
df_segm_analysis.rename({0:'well-off',
                         1:'fewer-opportunities',
                         2:'standard',
                         3:'career focused'})


# In[ ]:


df_segm_kmeans['Labels'] = df_segm_kmeans['Segment K-means'].map({0:'well-off', 
                                                                  1:'fewer opportunities',
                                                                  2:'standard', 
                                                                  3:'career focused'})


# In[ ]:


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


pca = PCA()


# In[ ]:


pca.fit(segmentation_std)


# In[ ]:


pca.explained_variance_ratio_


# In[ ]:


plt.figure(figsize = (12,9))
plt.plot(pca.explained_variance_ratio_.cumsum(), marker = 'o', linestyle = '--')
plt.title('Explained Variance by Components')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance');


# In[ ]:


pca = PCA(n_components = 3)


# In[ ]:


pca.fit(segmentation_std)



# COMMAND ----------

# MAGIC %md ## PCA RESULTS

# COMMAND ----------


# In[ ]:


pca.components_


# In[ ]:


df_pca_comp = pd.DataFrame(data = pca.components_,
                           columns = df_segmentation.columns.values,
                           index = ['Component 1', 'Component 2', 'Component 3'])
df_pca_comp


# In[ ]:


sns.heatmap(df_pca_comp,
            vmin = -1, 
            vmax = 1,
            cmap = 'RdBu',
            annot = True)
plt.yticks([0, 1, 2], 
           ['Component 1', 'Component 2', 'Component 3'],
           rotation = 45,
           fontsize = 9);


# In[ ]:


pca.transform(segmentation_std)


# In[ ]:


scores_pca = pca.transform(segmentation_std)



# COMMAND ----------

# MAGIC %md ## K-Means clustering with PCA

# COMMAND ----------


# In[ ]:


wcss = []
for i in range(1,11):
    kmeans_pca = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans_pca.fit(scores_pca)
    wcss.append(kmeans_pca.inertia_)


# In[ ]:


plt.figure(figsize = (10,8))
plt.plot(range(1, 11), wcss, marker = 'o', linestyle = '--')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('K-means with PCA Clustering')
plt.show()


# In[ ]:


kmeans_pca = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)


# In[ ]:


kmeans_pca.fit(scores_pca)



# COMMAND ----------

# MAGIC %md ## K-Means clustering with PCA

# COMMAND ----------


# In[ ]:


df_segm_pca_kmeans = pd.concat([df_segmentation.reset_index(drop = True), pd.DataFrame(scores_pca)], axis = 1)
df_segm_pca_kmeans.columns.values[-3: ] = ['Component 1', 'Component 2', 'Component 3']
df_segm_pca_kmeans['Segment K-means PCA'] = kmeans_pca.labels_


# In[ ]:


df_segm_pca_kmeans


# In[ ]:


df_segm_pca_kmeans_freq = df_segm_pca_kmeans.groupby(['Segment K-means PCA']).mean()
df_segm_pca_kmeans_freq


# In[ ]:


df_segm_pca_kmeans_freq['N Obs'] = df_segm_pca_kmeans[['Segment K-means PCA','Sex']].groupby(['Segment K-means PCA']).count()
df_segm_pca_kmeans_freq['Prop Obs'] = df_segm_pca_kmeans_freq['N Obs'] / df_segm_pca_kmeans_freq['N Obs'].sum()
df_segm_pca_kmeans_freq = df_segm_pca_kmeans_freq.rename({0:'standard', 
                                                          1:'career focused',
                                                          2:'fewer opportunities', 
                                                          3:'well-off'})
df_segm_pca_kmeans_freq


# In[ ]:


df_segm_pca_kmeans['Legend'] = df_segm_pca_kmeans['Segment K-means PCA'].map({0:'standard', 
                                                          1:'career focused',
                                                          2:'fewer opportunities', 
                                                          3:'well-off'})


# In[ ]:


x_axis = df_segm_pca_kmeans['Component 2']
y_axis = df_segm_pca_kmeans['Component 1']
plt.figure(figsize = (10, 8))
sns.scatterplot(x = x_axis, y= y_axis, hue = df_segm_pca_kmeans['Legend'], palette = ['g', 'r', 'c', 'm'])
plt.title('Clusters by PCA Components')
plt.show()


# In[ ]:


x_axis_1 = df_segm_pca_kmeans['Component 3']
y_axis_1 = df_segm_pca_kmeans['Component 1']
plt.figure(figsize = (12, 9))
sns.scatterplot(x = x_axis_1, y = y_axis_1, hue = df_segm_pca_kmeans['Legend'], palette = ['g', 'r', 'c', 'm'])
plt.title('Clusters by PCA Components' )
plt.show()


# In[ ]:


x_axis_1 = df_segm_pca_kmeans['Component 3']
y_axis_1 = df_segm_pca_kmeans['Component 2']
plt.figure(figsize = (12, 9))
sns.scatterplot(x = x_axis_1, y = y_axis_1, hue = df_segm_pca_kmeans['Legend'], palette = ['g', 'r', 'c', 'm'])
plt.title('Clusters by PCA Components' )
plt.show()



# COMMAND ----------

# MAGIC %md # DATA EXPORT

# COMMAND ----------


# In[ ]:


pickle.dump(scaler, open('scaler.pickle', 'wb'))


# In[ ]:


pickle.dump(pca, open('pca.pickle', 'wb'))


# In[ ]:


pickle.dump(kmeans_pca, open('kmeans_pca.pickle', 'wb'))

