#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns


# 
# # Create an “Academic performance” dataset of students and perform the following 
# # operations using Python.  

# In[ ]:


np.random.seed(42)# will always produce the same random array output. Without setting the seed, the output would differ with each run.
data={
    'Student_id':range(1,101),
    'Age':np.random.choice([18,19,20,21,22],100),
    'Gender':np.random.choice(['Male','Female', 100]),
    'ClassesMissed':np.random.randint(0,11, size=100),
    'Grade':np.random.normal(75,10,100) #mean, std, size
}


# In[ ]:


df = pd.DataFrame(data)
df


# In[ ]:


df['Age'][5]=np.nan
# df['ClassesMissed'][30:35]=20


# In[ ]:


df.head(10)


# In[ ]:


# null_index=df.index[df['Age'].isnull()]
# null_index.tolist() 


# # 1. Scan all variables for missing values and inconsistencies. If there are missing values 
# # and/or inconsistencies, use any of the suitable techniques to deal with them.  

# In[ ]:


df.isnull().sum()


# In[ ]:


df['Age'].fillna(df['Age'].median(), inplace=True)
df.head(10)


# In[ ]:


df.isnull().sum()


# ## Scan all numeric variables for outliers. If there are outliers, use any of the suitable 
# ## techniques to deal with them.  

# In[ ]:


plt.figure(figsize=(6, 6))
plt.boxplot(df['Age'], vert=True, patch_artist=True, flierprops=dict(markerfacecolor='red', marker='o'))
plt.title('Box Plot of Age')
plt.ylabel('Age')

# Display the plot
plt.show()


# In[ ]:


plt.figure(figsize=(6, 6))
plt.boxplot(df['ClassesMissed'], vert=True, patch_artist=True, flierprops=dict(markerfacecolor='red', marker='o'))
plt.title('Box Plot of ClassesMissed')
plt.ylabel('ClassesMissed')
# Display the plot
plt.show()


# In[ ]:


plt.figure(figsize=(6, 6))
plt.boxplot(df['Grade'], vert=True, patch_artist=True, flierprops=dict(markerfacecolor='red', marker='o'))
plt.title('Box Plot of Grade')
plt.ylabel('Grade')
# Display the plot
plt.show()


# In[ ]:


df.boxplot()


# In[ ]:


plt.figure(figsize=(6, 6))
plt.boxplot(df['Grade'], vert=True, patch_artist=True, flierprops=dict(markerfacecolor='red', marker='o'))
plt.title('Box Plot of Grade')
plt.ylabel('Grade')
# Display the plot
plt.show()


# In[ ]:


plt.figure(figsize=(6, 6))
plt.boxplot(df['ClassesMissed'], vert=True, patch_artist=True, flierprops=dict(markerfacecolor='red', marker='o'))
plt.title('Box Plot of ClassesMissed')
plt.ylabel('ClassesMissed')
# Display the plot
plt.show()


# # Handling the outlier

# In[ ]:


# Set limits for outliers (for 'MathScore', anything above 100 is an outlier)
df['Age'] = df['Age'].apply(lambda x: 21 if x > 21 else x)


# In[ ]:


df['ClassesMissed'] = df['ClassesMissed'].apply(lambda x: 5 if x > 7 else x)


# In[ ]:


df['Grade'] = df['Grade'].apply(lambda x:75 if x > 75 else x)


# In[ ]:


df['Grade'] = df['Grade'].apply(lambda x:65 if x < 65 else x)


# In[ ]:


plt.figure(figsize=(6, 6))
plt.boxplot(df['Grade'], vert=True, patch_artist=True, flierprops=dict(markerfacecolor='red', marker='o'))
plt.title('Box Plot of Grade')
plt.ylabel('Grade')
# Display the plot
plt.show()


# In[ ]:


plt.figure(figsize=(6, 6))
plt.boxplot(df['ClassesMissed'], vert=True, patch_artist=True, flierprops=dict(markerfacecolor='red', marker='o'))
plt.title('Box Plot of ClassesMissed')
plt.ylabel('ClassesMissed')
# Display the plot
plt.show()


#  ## Apply data transformations on at least one of the variables. The purpose of this 
# ## transformation should be one of the following reasons: to change the scale for better 
# ## understanding of the variable, to convert a non-linear relation into a linear one, or to 
# ## decrease the skewness and convert the distribution into a normal distribution. Reason 
# ## and document your approach properly.

# In[ ]:


# Visualize the distribution before transformation
plt.figure(figsize=(10, 6))
sns.histplot(df['ClassesMissed'], kde=True)  # 'kde=True' shows the density curve
plt.title('ClassesMissed Distribution Before Transformation')
plt.xlabel('ClassesMissed')
plt.show()

# Apply logarithmic transformation to ClassesMissed
df['LogClassesMissed'] = np.log(df['ClassesMissed'])

# Visualize the distribution after transformation
plt.figure(figsize=(8, 6))
sns.histplot(df['LogClassesMissed'], kde=True)  # Notice the difference
plt.title('ClassesMissed Distribution After Log Transformation')
plt.xlabel('Log of ClassesMissed')
plt.show()

