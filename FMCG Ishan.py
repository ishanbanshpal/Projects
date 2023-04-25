#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df1= pd.read_csv('Raw Sales Data.csv')


# In[4]:


df1


# In[5]:


df1.describe


# In[9]:


df1["Month"].value_counts()


# In[46]:


MonthlyData= df1.groupby('Month')


# In[47]:


MonthlyData.head()


# In[15]:


print(df1.dtypes)


# In[25]:


print(df1.dtypes)


# In[29]:


df1['Month']= df1["Month"].astype('datetime64[ns]')


# In[30]:


print(df1.dtypes)


# In[41]:


grouped_month = df1.groupby('Month')


# In[43]:


grouped_month


# In[49]:


df1.dtypes


# In[52]:


df1= pd.to_numeric(df1['Qty'],errors="coerce")


# In[54]:


df1.head


# In[65]:


marchsale= df1[df1['2021-03-01']]


# In[66]:


df1.info


# In[69]:


df1["Qty"] = df1["Qty"].str.replace(",","").astype("int64")


# In[ ]:





# In[ ]:




