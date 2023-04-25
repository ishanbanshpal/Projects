#!/usr/bin/env python
# coding: utf-8

# In[151]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[153]:


fifa=pd.read_csv('players_20.csv')


# In[154]:


fifa.head()


# In[155]:


fifa.shape


# In[158]:


for col in fifa.columns:
       print(col)


# In[160]:


fifa['nationality'].value_counts()


# In[161]:


fifa['nationality'].value_counts()[0:10]


# In[163]:


fifa['nationality'].value_counts()[0:5].keys()


# In[165]:


plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()), list(fifa['nationality'].value_counts()[0:5]))


# In[166]:


player_salary=fifa[['short_name', 'wage_eur']]


# In[167]:


player_salary.head()


# In[169]:


player_salary=player_salary.sort_values(by=['wage_eur'], ascending=False)


# In[170]:


player_salary.head()


# In[172]:


plt.bar(list(player_salary['short_name'])[0:5], list(player_salary['wage_eur'])[0:5], color=['red', 'blue', 'green', 'yellow', 'indigo'])


# In[174]:


fifa=fifa['nationality']=='Germany'


# In[183]:


fifa.head()


# In[189]:


fifa=pd.read_csv('players_20.csv')
Germany= fifa[fifa['nationality']=='Germany']
Germany.head()


# In[190]:


fifa['nationality'].value_counts()[0:10]


# In[192]:


Germany.head(10)


# In[193]:


Germany.sort_values(by=['height_cm'], ascending=False).head(10)


# In[194]:


Germany.sort_values(by=['weight_kg'], ascending=False)


# In[198]:


Germany[['wage_eur', 'short_name']].sort_values(by=['wage_eur'],ascending=False)


# In[200]:


player_shooting=fifa[['short_name', 'shooting']]


# In[201]:


player_shooting.sort_values(by=['shooting'], ascending=False)


# In[202]:


player_defending=fifa[['short_name', 'nationality', 'defending','club']]


# In[203]:


player_defending.head()


# In[204]:


player_defending.sort_values(by=['defending'], ascending=False)


# In[206]:


real_madrid=fifa[fifa['club']=='Real Madrid']


# In[207]:


real_madrid.head()


# In[212]:


real_madrid.sort_values(by=['wage_eur'], ascending=False).head()


# In[215]:


real_madrid['nationality'].value_counts()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




