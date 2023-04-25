#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df= pd.read_excel("salesdb.xlsx")


# In[3]:


df.info()


# In[4]:


df.head()


# In[5]:


import numpy as np


# In[6]:


df.describe()


# In[7]:


X = df.iloc[:,:-1].values


# In[11]:


Y = df.iloc[:,-1:].values


# In[8]:


X


# In[12]:


Y


# In[20]:


from sklearn.model_selection import train_test_split


# In[21]:


X_train,X_test,Y_train,Y_test=train_test_split(X,Y, test_size=0.25, random_state=0)


# In[23]:


from sklearn.preprocessing import StandardScaler


# In[24]:


Ss= StandardScaler()


# In[26]:


X_train = Ss.fit_transform(X_train)


# In[27]:


X_test= Ss.fit_transform(X_test)


# In[28]:


from sklearn.linear_model import LogisticRegression


# In[29]:


Lr= LogisticRegression()


# In[33]:


Lr.fit(X_train,Y_train)


# In[34]:


Y_pred=Lr.predict(X_test)


# In[35]:


Y_pred


# In[37]:


print(np.concatenate((Y_pred.reshape(len(Y_pred),-1),Y_test.reshape(len(Y_test),1)),1))


# In[40]:


age= int(input("age"))
sal= int(input("sal"))
newCust = [[age,sal]]
result = Lr.predict(Ss.transform(newCust))
print(result)
if result == 1:
    print("Buy")
else:
    print("Won't")


# In[ ]:




