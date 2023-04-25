#!/usr/bin/env python
# coding: utf-8

# In[221]:


import pandas as pd
from matplotlib import pyplot as plt
marvel=pd.read_csv('charcters_stats.csv')


# In[222]:


marvel.head()


# In[223]:


marvel.shape


# In[225]:


marvel['Alignment'].value_counts()


# In[232]:


Good_Hero= marvel[marvel['Alignment']=='good']


# In[233]:


Good_Hero.head()


# In[238]:


Good_Hero.sort_values(by=['Total'],ascending=False)


# In[241]:


goodmaxpower=Good_Hero[Good_Hero['Power']==100]


# In[242]:


goodmaxpower.head()


# In[243]:


goodmaxpower.shape


# In[248]:


plt.bar(list(goodmaxpower['Name'])[0:5], list(goodmaxpower['Total'][0:5]))


# In[256]:


bad=marvel[marvel['Alignment']=='bad'].sort_values(by=['Total'], ascending=False)


# In[257]:


bad.head()


# In[258]:


plt.bar(list(bad['Name'])[0:5], list(bad['Total'])[0:5])


# In[260]:


plt.figure(figsize=(10,5))
plt.hist(Good_Hero['Speed'])
plt.title('Speed Distribution')
plt.xlabel('speed')


# In[261]:


plt.figure(figsize=(10,5))
plt.hist(bad['Combat'])
plt.title('bad-Combat')
plt.xlabel('Combat')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




