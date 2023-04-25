#!/usr/bin/env python
# coding: utf-8

# #### forecasting helps us to assess the risks

# In[ ]:


#Time-Series:(dependent,FUTURE) y=f(x)(independent v, PAST)(x=time in time series)(regular intervals)


# In[ ]:


#special features of time series data: data cannot be independent, ordering matters,no missing value


# In[ ]:


#time seies: Systematic component (trend,seasonality) & Irregular Component


# In[ ]:


# decomposition model: additive, multiplicative


# In[ ]:


# additive; y=t+s+i (when seasonality is constant) trend+seasonality+error


# In[ ]:


#sales=trend(business growth)+seasonality(whether)+error


# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose


# In[2]:


df1= pd.read_csv('AirPassengers.csv')


# In[3]:


df1.dtypes


# In[6]:


df1.dtypes


# In[15]:


df1=pd.read_csv('AirPassengers.csv', parse_dates=["Month"])


# In[21]:


df1.tail()


# In[27]:


df1=pd.read_csv('AirPassengers.csv', parse_dates=["Month"], index_col='Month')


# In[28]:


df1


# In[31]:


df1['1949-02-15':'1951-02-1']


# In[35]:


df1.loc['1951-02-1']


# In[36]:


df1.plot()


# In[48]:


#increase the figure size
from pylab import rcParams
rcParams['figure.figsize']=12,8
df1.plot()
plt.show()


# In[ ]:


#decompose the time series multiplicatively


# In[53]:


df1_mul_decompose= seasonal_decompose(df1, model='multiplicative')
df1_mul_decompose.plot()


# In[60]:


df1_log=df1.copy()


# In[67]:


df1_log['Passengers']=np.log(df1)


# In[68]:


df1_log.Passengers


# In[ ]:


#visualize the log transformed data-


# In[69]:


df1_log.plot()


# In[70]:


df1.plot()


# In[ ]:


#compare with original


# In[ ]:


#multiplicative; y=t*s*i(when seasonality is not constant)


# In[77]:


plt.subplot(2,1,1)
plt.title('orignal')
plt.plot(df1)

plt.subplot(2,1,2)
plt.title('log transformed')
plt.plot(df1_log)


plt.tight_layout
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




