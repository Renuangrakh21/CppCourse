#!/usr/bin/env python
# coding: utf-8

#  
# # Data Wrangling I 
# # Perform the following operations using Python on any open source dataset (e.g., 
# # data.csv)  
# # 1. Import all the required Python Libraries.  
# # 2. Locate open source data from the web. Provide a clear description of the data and its 
# # source (i.e., URL of the web site).  
# # 3. Load the Dataset into pandas dataframe. 
# # 4. Data Preprocessing: check for missing values in the data using pandas isnull (), 
# # describe () function to get some initial statistics. Provide variable descriptions. Types of 
# # variables etc. Check the dimensions of the # data frame.  
# # 5. Data Formatting and Data Normalization: Summarize the types of variables by 
# # checking the data types (i.e., character, numeric, integer, factor, and logical) of the 
# # variables in the data set. If variables are not in the correct data type, apply proper type 
# # conversions.  
# # 6. Turn categorical variables into quantitative variables in Python. In addition to the 
#  # codes and outputs, explain every operation that you do in the above steps and explain 
# # everything that you do to import/read/scrape the data set.

# ## 1. Import all the required Python Libraries. 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ## 2. Locate open source data from the web. Provide a clear description of the data and its source (i.e., URL of the web site). 

# ## 3. Load the Dataset into pandas dataframe. 

# In[2]:


df=pd.read_csv('titanic_dataset.csv') 


# In[3]:


df.head()


# ## 4. Data Preprocessing: check for missing values in the data using pandas isnull (), 
# ## describe () function to get some initial statistics. Provide variable descriptions. Types of 
# ## variables etc. Check the dimensions of the data frame. 

# In[4]:


df.describe()


# In[5]:


df.isnull()


# In[6]:


df.isnull().sum()


# In[22]:


df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])


# In[23]:


df.isnull().sum()


# In[9]:


df.shape


# In[10]:


df.info()


# In[11]:


df.ndim


# In[12]:


data_type=df.dtypes
data_type


# # Data Formatting and Data Normalization

# In[13]:


# data_type=df.dtypes

# Convert data types if needed
# Assuming 'Sex' is a categorical variable
df['Sex']=df['Sex'].astype('category')

# Ensure 'Pclass' (Passenger Class) is an integer
df['Pclass']=df['Pclass'].astype('float')


# # Convert Categorical Variables into Quantitative Variables

# In[14]:


from sklearn.preprocessing import LabelEncoder  #encode categorical data into integers.
label_encoder=LabelEncoder()
df['Sex']=label_encoder.fit_transform(df['Sex'])


# In[15]:


df


# In[ ]:




