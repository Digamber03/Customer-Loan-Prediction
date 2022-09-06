#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import  matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv('data.csv')
df


# In[3]:


df.head(10)


# In[4]:


df.isnull().sum()


# In[5]:


# df['Self_Employed']=df['Self_Employed'].fillna('Self_Employed').mean()
# df['Self_Employed']


# In[6]:


df.isnull().sum()


# In[13]:


df['LoanAmount'].value_counts()


# In[ ]:





# In[ ]:



df.shape


# In[ ]:


df.describe()


# In[ ]:


df['Property_Area'].value_counts()


# In[ ]:


df['ApplicantIncome'].hist(bins=50)
plt.show()


# In[ ]:


df.boxplot(column='ApplicantIncome', by = 'Education')
plt.show()


# In[ ]:


df.boxplot()
plt.show()


# In[ ]:


df['LoanAmount'].hist(bins=50)
plt.show()


# In[ ]:


df.boxplot(column='LoanAmount')
plt.show()


# In[ ]:


temp1=df['Credit_History'].value_counts(ascending=True)


# In[ ]:


temp2=df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map({'y':1,'N':0}).mean())
print('Frequency Table for Credit History:')
print(temp1)
print('/nprobability of getting loan for each credit History class:')
print(temp2)


# In[ ]:


fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121)
ax1.set_xlabel('Credit_History')
ax1.set_ylabel('Count of Applicants')
ax1.set_title("Applicants by Credit_History")
temp1.plot(kind='bar')
plt.show()e


# In[ ]:


ax2 = fig.add_subplot(122)
ax2.set_xlabel('Credit_History')
ax2.set_ylabel('Probability of getting loan')
ax2.set_title("Probability of getting loan by credit history")
temp2.plot(kind = 'bar')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




