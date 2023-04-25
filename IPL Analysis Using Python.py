#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#IPL


# In[7]:


import pandas as pd


# In[9]:


from matplotlib import pyplot as plt


# In[10]:


import seaborn as sns


# In[12]:


ipl=pd.read_csv('data.csv')


# In[13]:


ipl.head()


# In[14]:


ipl.shape


# In[ ]:





# In[15]:


ipl['winner'].value_counts()


# In[16]:


ipl['player_of_match'].value_counts()


# In[21]:


ipl['player_of_match'].value_counts()[0:10]


# In[22]:


ipl['player_of_match'].value_counts()[0:5]


# In[29]:


list(ipl['player_of_match'].value_counts()[0:5].keys())


# In[30]:



plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()), list(ipl['player_of_match'].value_counts()[0:5]), color='r')


# In[34]:


plt.figure(figsize=(8,10))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()), list(ipl['player_of_match'].value_counts()[0:5]), color='y')


# In[35]:


ipl['result'].value_counts()


# In[37]:


ipl['toss_winner'].value_counts()


# In[38]:


batting_first= ipl[ipl['win_by_runs']!=0]


# In[39]:


batting_first.head()


# In[40]:


plt.hist(batting_first['win_by_runs'])


# In[41]:


batting_first['winner'].value_counts()


# In[47]:


l1=batting_first['winner'].value_counts()[0:5]


# In[53]:


plt.bar(batting_first['winner'].value_counts()[0:5].keys(),batting_first['winner'].value_counts()[0:5], color=['red','blue','yellow','green','orange'])


# In[66]:


plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')


# In[67]:


batting_second= ipl[ipl['win_by_wickets']!=0]


# In[68]:


batting_second.head()


# In[69]:


batting_second['winner'].value_counts()


# In[75]:


plt.pie(list(batting_second['winner'].value_counts()),labels=(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')


# In[95]:


ipl['season'].value_counts()


# In[96]:


ipl['city'].value_counts()


# In[97]:


import numpy as np


# In[98]:


np.sum(ipl['toss_winner']==ipl['winner'])


# In[99]:


ipl['result'].value_count()


# In[100]:


ipl.head()


# In[102]:


ipl['result'].value_counts()


# In[103]:


ipl['result'].shape


# In[105]:


deliveries=pd.read_csv('deliveries.csv')


# In[106]:


deliveries.head()


# In[112]:


deliveries['batsman'].value_counts()[0:10]


# In[113]:


deliveries['player_dismissed'].value_counts()


# In[114]:


deliveries['dismissal_kind'].value_counts()


# In[115]:


deliveries['total_runs'].value_counts()[0:10]


# In[116]:


deliveries['match_id'].unique()


# In[118]:


match_1=deliveries[deliveries['match_id']==1]


# In[119]:


match_1.shape


# In[120]:


match_1.head()


# In[122]:


kkr=match_1[match_1['inning']==1]


# In[123]:


kkr.head()


# In[124]:


kkr['batsman_runs'].value_counts()


# In[125]:


kkr['dismissal_kind'].value_counts()


# In[127]:


rcb=match_1[match_1['inning']==2]


# In[128]:


rcb.head()


# In[129]:


rcb['total_runs'].value_counts()


# In[130]:


rcb['batsman_runs'].value_counts()


# In[144]:


rcb['batsman'].value_counts().keys()


# In[136]:


List1=list(rcb['batsman'].value_counts())


# In[137]:


List2=list(rcb['batsman_runs'].value_counts())


# In[ ]:





# In[138]:


List1


# In[139]:


List2


# In[145]:


Players=list(rcb['batsman'].value_counts().keys())


# In[149]:


Players


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




