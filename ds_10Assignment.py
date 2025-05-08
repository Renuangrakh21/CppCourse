#!/usr/bin/env python
# coding: utf-8

# # Assignment No:10

# ## Data Visualization III

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Reading the CSV file

# In[ ]:


# Step 1: Load the Iris dataset
iris_df = pd.read_csv('iris.csv')


# In[ ]:


iris_df


# In[ ]:


iris_df.describe()


# In[ ]:


iris_df.head(5)


# In[ ]:


# Step 2: List down the features and their types
print("Features and their types:")
print(iris_df.info())


# In[ ]:


# Step 3: Create a histogram for each feature
iris_df.hist(figsize=(10, 8))
plt.title("Histogram for each feature")
plt.show()


# In[ ]:


#Step 4: Create a boxplot for each feature
iris_df.boxplot(figsize=(10, 6))
plt.title("Boxplot for each feature")
plt.show()


# In[ ]:


sns.boxplot(x='petal_length',y='species', data=iris_df)


# In[ ]:


sns.boxplot(x='sepal_length',y='species', data=iris_df)


# In[ ]:


sns.boxplot(x='sepal_width',y='species', data=iris_df)


# In[ ]:


sns.boxplot(x='petal_width',y='species', data=iris_df)

