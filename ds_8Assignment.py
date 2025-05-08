#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


# Step 1: Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')


# In[ ]:


titanic_df


# In[ ]:


titanic_df.describe(include = 'object')


# In[ ]:


titanic_df.shape


# In[ ]:


titanic_df.info()


# In[ ]:


titanic_df.isnull()


# In[ ]:


titanic_df.isnull().sum()


# In[ ]:


titanic_df['age'] = titanic_df['age'].fillna(titanic_df['age'].mean())


# In[ ]:


# deck_mode=titanic_df['deck'].mode()
# titanic_df['deck']=titanic_df['deck'].fillna(deck_mode)
titanic_df['deck']=titanic_df['deck'].dropna


# In[ ]:


# embark_town_mode=titanic_df['embark_town'].mode()
# titanic_df['embark_town']=titanic_df['embark_town'].fillna(embark_town_mode)
titanic_df['embark_town']=titanic_df['embark_town'].dropna


# In[ ]:


embarked_mode=titanic_df['embarked'].mode()
titanic_df['embarked']=titanic_df['embarked'].fillna(embarked_mode)


# In[ ]:


titanic_df.isnull().sum()


# In[ ]:


# Step 2: Visualize patterns in the data using Seaborn


# In[ ]:


# Scatter plot
sns.scatterplot(data=titanic_df, x='age', y='fare', hue='survived')
plt.title('Scatter Plot of Fare vs Age (Survived)')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()


# In[ ]:


# Bar plot
sns.barplot(data=titanic_df, x='sex', y='fare', hue='class')
plt.title('Bar Plot of Fare by Sex and Class')
plt.xlabel('Sex')
plt.ylabel('Fare')
plt.show()


# In[ ]:


# Grouped bar plot
sns.barplot(data=titanic_df, x='class', y='fare', hue='survived')
plt.title('Grouped Bar Plot of Fare by Class and Survival')
plt.xlabel('Class')
plt.ylabel('Fare')
plt.show()


# In[ ]:


# Step 3: Plot a histogram to show the distribution of ticket prices
plt.figure(figsize=(6, 4))
sns.histplot(data=titanic_df, x='fare', bins=20, kde=True)
plt.title('Histogram of Ticket Prices (Fare)')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()


# In[ ]:





# In[ ]:




