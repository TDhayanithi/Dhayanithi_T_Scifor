#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[23]:


df = sns.load_dataset('iris')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[7]:


df.describe()


# In[9]:


import warnings
warnings.filterwarnings('ignore')


# In[10]:


# Bar Chart
plt.figure(figsize=(8,6))
sns.countplot(x = 'species', data = df)
plt.title('Bar chart of Species Count')
plt.show()


# In[12]:


# Pie Chart
palette = sns.color_palette('husl',n_colors=(len(df['species'].unique())))
plt.figure(figsize=(8,6))
df['species'].value_counts().plot.pie(autopct = '%1.1f%%',colors = palette)
plt.title('Pie Chart of Species')
plt.axis('equal')
plt.show()


# In[18]:


# Heatmap
plt.figure(figsize=(10, 8))
df1 = df.drop(['species'],axis = 1,)
corr = df1.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap of Feature Correlations in Iris Dataset')
plt.show()


# In[25]:


# Histogram with Matplotlib
plt.figure(figsize=(10, 6))
plt.hist(df['sepal_length'], bins=20, color='skyblue', edgecolor='black', density=True)
plt.title('Histogram of Sepal Length in Iris Dataset')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Density')
plt.show()


# In[26]:


# Scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species', palette='viridis')
plt.title('Scatterplot of Sepal Length vs. Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()


# In[27]:


# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='species', y='sepal_length', data=df)
plt.title('Boxplot of Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.show()


# In[ ]:




