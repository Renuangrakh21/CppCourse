#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


data=pd.read_csv("iris.csv")
data.head()


# In[ ]:


data.shape


# In[ ]:


data.head()


# In[ ]:


data.tail()


# In[ ]:


data.info()


# In[ ]:


data.describe()


# In[ ]:


data.isnull().sum()


# In[ ]:


X=data.drop(['species'],axis=1)
y=data.drop(['sepal_length','sepal_width','petal_length','petal_width'],axis=1)
print(X)
print(y)
print(X.shape)
print(y.shape)


# In[ ]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


# In[ ]:


from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train, y_train)


# In[ ]:


y_pred=model.predict(X_test)
model.score(X_test,y_test)


# In[ ]:


from sklearn.metrics import accuracy_score, confusion_matrix
print(accuracy_score(y_test, y_pred))


# # Confusion Matrix

# In[ ]:


cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix:")
print(cm)


# In[ ]:


def get_confusion_matrix_values(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    return(cm[0][0], cm[0][1], cm[1][0], cm[1][1])


# In[ ]:


TP, FP, FN, TN = get_confusion_matrix_values(y_test, y_pred)
print("TP: ", TP)
print("FP: ", FP)
print("FN: ", FN)
print("TN: ", TN)


# # Accuracy,Precision,Recall,Error rate

# In[ ]:


print("The Accuracy is ", (TP+TN)/(TP+TN+FP+FN))
print("The precision is ", TP/(TP+FP))
print("The recall is ", TP/(TP+FN))
print("The Error rate is ",(FP+FN)/(TP+TN+FP+FN))


# In[ ]:




