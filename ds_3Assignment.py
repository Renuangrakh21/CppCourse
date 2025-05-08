#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[ ]:


df=pd.read_csv('titanic_dataset.csv')


# In[ ]:


df


# In[ ]:


df.info()


# In[ ]:


df.shape


# In[ ]:


df.describe()


# In[ ]:


df.head()


# In[ ]:


df.tail()


# In[ ]:


df.mean()


# In[ ]:


df.median()


# In[ ]:


df.mode()


# In[ ]:


df.std()


# In[ ]:


df.groupby('Age').describe()


# In[ ]:


df['Age'].mean()


# In[ ]:


df['Age'].median()


# In[ ]:


df['Age'].std()


# In[ ]:


df['Age'].max()


# In[ ]:


df['Age'].min()


# In[ ]:


df.groupby('Age').count()


# In[ ]:


grouped_values = df.groupby('AgeGroup')['Fare'].apply(list).to_dict()

print("List of numeric values per age group:")
for group, values in grouped_values.items():
    print(f"{group}: {values}")


# In[ ]:


grouped=df.groupby('Pclass').describe()


# In[ ]:


# Calculate summary statistics for 'Age' and 'Fare' grouped by 'Pclass'
summary_statistics = grouped[['Age', 'Fare']].agg(['mean', 'median', 'min', 'max', 'std'])
summary_statistics


# In[ ]:


dff=pd.read_csv('iris.csv')


# In[ ]:


dff


# In[ ]:


dff.info()


# In[ ]:


dff.head()


# In[ ]:


dff.tail()


# In[ ]:


dff.shape


# In[ ]:


dff.species.unique()


# In[ ]:


dff.groupby('species').mean()


# In[ ]:


dff.groupby('species').median()


# In[ ]:


dff.groupby('species').std()

