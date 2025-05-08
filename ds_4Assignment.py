#!/usr/bin/env python
# coding: utf-8

# # Create a Linear Regression Model using Python to predict home prices using Boston
# # Housing Dataset.The Boston Housing dataset contains information about various
# # houses in Boston through different parameters.

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


data = pd.read_csv('HousingData.csv')
data.head()


# In[ ]:


data.tail()


# In[ ]:


print("The shape of the data is: ")
data.shape


# In[ ]:


data.isnull().sum()


# In[ ]:


data.info()


# In[ ]:


data['CRIM'] = data['CRIM'].fillna(data['CRIM'].mean())
data['ZN'] = data['ZN'].fillna(data['ZN'].mean())
data['INDUS'] = data['INDUS'].fillna(data['INDUS'].mean())
data['CHAS'] = data['CHAS'].fillna(data['CHAS'].mean())
data['AGE'] = data['AGE'].fillna(data['AGE'].mean())
data['LSTAT'] = data['LSTAT'].fillna(data['LSTAT'].mean())


# In[ ]:


data.isnull().sum()


# In[ ]:


data.head()


# In[ ]:


data.columns


# In[ ]:


data.info()


# In[ ]:


data.describe()


# In[ ]:


len(data['MEDV'])


# In[ ]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[ ]:


X = np.array(data['RM']).reshape(-1,1)
Y = np.array(data['MEDV']).reshape(-1,1)


# In[ ]:


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


# In[ ]:


print(X_train.shape, y_train.shape)


# In[ ]:


reg = LinearRegression().fit(X_train, y_train)


# In[ ]:


reg.score(X_train, y_train)


# In[ ]:


y_pred = reg.predict(X_test)


# In[ ]:


import matplotlib.pyplot as plt
# %matplotlib inline


# In[ ]:


plt.scatter(X_test, y_test, color='r')
plt.plot(X_test, y_pred, color='g')
plt.show()


# In[ ]:


from sklearn.metrics import r2_score
r2_score_val = r2_score(y_test, y_pred)


# In[ ]:


print(r2_score_val)


# In[ ]:


reg.score(X_test,y_test)


# In[ ]:





# In[ ]:




