# Databricks notebook source
#!/usr/bin/env python
# coding: utf-8


# COMMAND ----------

# MAGIC %md ## ${\textbf{Libraries}}$

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

# MAGIC %md ## ${\textbf{Import Data}}$

# COMMAND ----------




df_segmentation = pd.read_csv('new-notebook/data.csv')



# COMMAND ----------

# MAGIC %md ## ${\textbf{Explore Data}}$

# COMMAND ----------




df_segmentation.head()




df_segmentation.describe()



# COMMAND ----------

# MAGIC %md ## ${\textbf{Correlation Estimate}}$

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



# COMMAND ----------

# MAGIC %md ## ${\textbf{Visualize Raw Data}}$

# COMMAND ----------




plt.figure(figsize = (12, 9))
plt.scatter(df_segmentation.iloc[:, 2], df_segmentation.iloc[:, 4])
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Visualization of raw data')



# COMMAND ----------

# MAGIC %md ## ${\textbf{Standardization}}$

# COMMAND ----------




scaler = StandardScaler()
segmentation_std = scaler.fit_transform(df_segmentation)



# COMMAND ----------

# MAGIC %md ## ${\textbf{Hierarchical Clustering}}$

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

# MAGIC %md ## ${\textbf{K-means Clustering}}$

# COMMAND ----------




wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(segmentation_std)
    wcss.append(kmeans.inertia_)




plt.figure(figsize = (10,8))
plt.plot(range(1, 11), wcss, marker = 'o', linestyle = '--')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('K-means Clustering')
plt.show()




kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)




kmeans.fit(segmentation_std)



# COMMAND ----------

# MAGIC %md ### ${\textbf{Results}}$

# COMMAND ----------




df_segm_kmeans = df_segmentation.copy()
df_segm_kmeans['Segment K-means'] = kmeans.labels_




df_segm_analysis = df_segm_kmeans.groupby(['Segment K-means']).mean()
df_segm_analysis




df_segm_analysis['N Obs'] = df_segm_kmeans[['Segment K-means','Sex']].groupby(['Segment K-means']).count()
df_segm_analysis['Prop Obs'] = df_segm_analysis['N Obs'] / df_segm_analysis['N Obs'].sum()




df_segm_analysis




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
sns.scatterplot(x_axis, y_axis, hue = df_segm_kmeans['Labels'], palette = ['g', 'r', 'c', 'm'])
plt.title('Segmentation K-means')
plt.show()



# COMMAND ----------

# MAGIC %md ### ${\textbf{PCA}}$

# COMMAND ----------




pca = PCA()




pca.fit(segmentation_std)




pca.explained_variance_ratio_




plt.figure(figsize = (12,9))
plt.plot(range(1,8), pca.explained_variance_ratio_.cumsum(), marker = 'o', linestyle = '--')
plt.title('Explained Variance by Components')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')




pca = PCA(n_components = 3)




pca.fit(segmentation_std)



# COMMAND ----------

# MAGIC %md ### ${\textbf{PCA Results}}$

# COMMAND ----------




pca.components_




df_pca_comp = pd.DataFrame(data = pca.components_,
                           columns = df_segmentation.columns.values,
                           index = ['Component 1', 'Component 2', 'Component 3'])
df_pca_comp




sns.heatmap(df_pca_comp,
            vmin = -1, 
            vmax = 1,
            cmap = 'RdBu',
            annot = True)
plt.yticks([0, 1, 2], 
           ['Component 1', 'Component 2', 'Component 3'],
           rotation = 45,
           fontsize = 9)




pca.transform(segmentation_std)




scores_pca = pca.transform(segmentation_std)



# COMMAND ----------

# MAGIC %md ### ${\textbf{K-means clustering with PCA}}$

# COMMAND ----------




wcss = []
for i in range(1,11):
    kmeans_pca = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans_pca.fit(scores_pca)
    wcss.append(kmeans_pca.inertia_)




plt.figure(figsize = (10,8))
plt.plot(range(1, 11), wcss, marker = 'o', linestyle = '--')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('K-means with PCA Clustering')
plt.show()




kmeans_pca = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)




kmeans_pca.fit(scores_pca)



# COMMAND ----------

# MAGIC %md ### ${\textbf{K-means clustering with PCA Results}}$

# COMMAND ----------




df_segm_pca_kmeans = pd.concat([df_segmentation.reset_index(drop = True), pd.DataFrame(scores_pca)], axis = 1)
df_segm_pca_kmeans.columns.values[-3: ] = ['Component 1', 'Component 2', 'Component 3']
df_segm_pca_kmeans['Segment K-means PCA'] = kmeans_pca.labels_




df_segm_pca_kmeans




df_segm_pca_kmeans_freq = df_segm_pca_kmeans.groupby(['Segment K-means PCA']).mean()
df_segm_pca_kmeans_freq




df_segm_pca_kmeans_freq['N Obs'] = df_segm_pca_kmeans[['Segment K-means PCA','Sex']].groupby(['Segment K-means PCA']).count()
df_segm_pca_kmeans_freq['Prop Obs'] = df_segm_pca_kmeans_freq['N Obs'] / df_segm_pca_kmeans_freq['N Obs'].sum()
df_segm_pca_kmeans_freq = df_segm_pca_kmeans_freq.rename({0:'standard', 
                                                          1:'career focused',
                                                          2:'fewer opportunities', 
                                                          3:'well-off'})
df_segm_pca_kmeans_freq




df_segm_pca_kmeans['Legend'] = df_segm_pca_kmeans['Segment K-means PCA'].map({0:'standard', 
                                                          1:'career focused',
                                                          2:'fewer opportunities', 
                                                          3:'well-off'})




x_axis = df_segm_pca_kmeans['Component 2']
y_axis = df_segm_pca_kmeans['Component 1']
plt.figure(figsize = (10, 8))
sns.scatterplot(x_axis, y_axis, hue = df_segm_pca_kmeans['Legend'], palette = ['g', 'r', 'c', 'm'])
plt.title('Clusters by PCA Components')
plt.show()




x_axis_1 = df_segm_pca_kmeans['Component 3']
y_axis_1 = df_segm_pca_kmeans['Component 1']
plt.figure(figsize = (12, 9))
sns.scatterplot(x_axis_1, y_axis_1, hue = df_segm_pca_kmeans['Legend'], palette = ['g', 'r', 'c', 'm'])
plt.title('Clusters by PCA Components' )
plt.show()




x_axis_1 = df_segm_pca_kmeans['Component 3']
y_axis_1 = df_segm_pca_kmeans['Component 2']
plt.figure(figsize = (12, 9))
sns.scatterplot(x_axis_1, y_axis_1, hue = df_segm_pca_kmeans['Legend'], palette = ['g', 'r', 'c', 'm'])
plt.title('Clusters by PCA Components' )
plt.show()



# COMMAND ----------

# MAGIC %md ### ${\textbf{Data Export}}$

# COMMAND ----------




pickle.dump(scaler, open('scaler.pickle', 'wb'))




pickle.dump(pca, open('pca.pickle', 'wb'))




pickle.dump(kmeans_pca, open('kmeans_pca.pickle', 'wb'))

