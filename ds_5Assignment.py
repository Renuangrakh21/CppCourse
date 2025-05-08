#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


df=pd.read_csv("Social_Network_Ads.csv")
df.head(10)


# In[ ]:


df.info()


# In[ ]:


df.describe()


# In[ ]:


X=df.iloc[:,[2,3]].values
y=df.iloc[:,4].values


# In[ ]:


X


# In[ ]:


y


# ## Split the dataset into train and test

# In[ ]:


from sklearn.model_selection import train_test_split
X_train ,X_test ,y_train ,y_test=train_test_split(X,y,test_size=0.25,random_state=0)


# ## Preprocessing

#  ## Stanadrd Scalar

# In[ ]:


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)


# In[ ]:


# X_train


# ## Classification

# In[ ]:


from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(X_train,y_train)


# ## Prediction

# In[ ]:


y_pred=classifier.predict(X_test)


# In[ ]:


y_pred


# # Confusion Matrix

# In[ ]:


from sklearn.metrics import confusion_matrix,classification_report
cm=confusion_matrix(y_test,y_pred)


# In[ ]:


cm


# In[ ]:


c1_report=classification_report(y_test,y_pred)


# In[ ]:


c1_report


# In[ ]:


tp , fp ,fn ,tn=confusion_matrix(y_test,y_pred,labels=[0,1]).reshape(-1)
print('Outcome values : \n',tp ,fp,fn,tn)


# In[ ]:


accurancy_cm=(tp+tn)/(tp+fp+tn+fn)
precision_cm=tp/(tp+fp)
recall_cm=tp/(tp+fn)  
Error_rate=(fn+fp)/(tp+fp+tn+fn)
f1_score=2/((1/recall_cm)+(1/precision_cm))


# In[ ]:


print("Accurancy  : ",accurancy_cm)
print("Precision  : ",precision_cm)
print("Recall  : ",recall_cm)
print("F1-score : ",f1_score)
print("Error_rate : ",Error_rate)

