#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


# Step 1: Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')


# In[ ]:


titanic_df


# In[ ]:


sns.boxplot(x=titanic_df['age']) 
plt.xlabel('age')
plt.show()


# In[ ]:


sns.boxplot(y=titanic_df['fare']) 
plt.ylabel('Fare')
plt.show()


# In[ ]:


sns.boxplot( x=titanic_df['sex'], y=titanic_df['age'])


# In[ ]:


# Step 2: Plot box plot for distribution of age with respect to each gender and survival status
plt.figure(figsize=(10, 6))
sns.boxplot(data=titanic_df, x='sex', y='age', hue='survived')
plt.title('Box Plot of Age with Respect to Gender and Survival')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.show()


# ## Observations and Inferences
# After plotting the box plot, you can draw several conclusions:
# 
# Age Distribution:
# The median age for both males and females who survived is lower than those who did not survive.
# The age range for those who did not survive is broader, with more outliers, indicating that people of varying ages failed to survive.
# Gender Differences:
# Females tend to have a smaller age range, with a higher concentration of survivors, indicating a higher survival rate among females.
# Males generally have a broader age distribution, with fewer survivors compared to females.
# Survival Rate:
# The box plot suggests a higher survival rate among females, especially those who are younger. This aligns with the "women and children first" principle.
# There are fewer outliers among those who survived, indicating that survivors generally belong to a narrower age range.

# In[ ]:


# Step 3: Observations from the statistics
# Display the first few rows of the dataset
print(titanic_df.head(10))


# In[ ]:


titanic_df.info()


# In[ ]:


# Display summary statistics for the 'age' column
print("\nSummary statistics for the 'age' column:")
print(titanic_df['age'].describe())


# In[ ]:




