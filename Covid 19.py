#!/usr/bin/env python
# coding: utf-8

# In[91]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime as dt
import numpy as np


# In[97]:


df= pd.read_csv('covid_19_india.csv')


# In[98]:


df.head()


# In[95]:


df= pd.read_csv('covid_19_india.csv', parse_dates=['Date'], dayfirst=True)


# In[ ]:





# In[96]:


df.head()


# In[99]:


df= df[['Date', "State/UnionTerritory",'Cured','Deaths', 'Confirmed']]


# In[100]:


df.head()


# In[102]:


df.columns=['date', 'state', 'cured','death', 'confirmed']


# In[103]:


df.head()


# In[110]:


df[df['state']=='Kerala']


# In[121]:


df[df['state']=='Maharashtra']


# In[127]:


delhi= df[df.state=='Delhi']


# In[129]:


delhi.head()


# In[123]:


df['date']=='2021-08-11'


# In[124]:


exactdate= df[df['date']=='2021-08-11']


# In[112]:


exactdate= df[df.date=='2021-08-11']


# In[125]:


exactdate.head()


# In[116]:


confirmedcaseonexactdate=exactdate.sort_values(by='confirmed', ascending=False)


# In[117]:


confirmedcaseonexactdate.head()


# In[138]:


sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state', y='confirmed', data=confirmedcaseonexactdate.head(), hue='state')


# In[137]:


plt.show


# In[ ]:





# In[ ]:





# In[139]:


exactdeath=exactdate.sort_values(by='death', ascending=False)


# In[140]:


exactdeath.head()


# In[144]:


sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state', y='death', data=exactdeath.head(),hue='state')
plt.show()


# In[145]:


cured=exactdate.sort_values(by='cured', ascending=False)


# In[146]:


cured.head()


# In[147]:


sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state',y='cured', data=cured.head(), hue='state')
plt.show


# In[148]:


Maha=df[df.state=='Maharashtra']


# In[149]:


Maha.head()


# In[152]:


sns.set(rc={'figure.figsize': (15,10)})
sns.lineplot(x='date', y='confirmed', data=Maha)
plt.show()


# In[153]:


sns.set(rc={'figure.figsize': (15,10)})
sns.lineplot(x='date', y='death', data=Maha)
plt.show()


# In[154]:


tests= pd.read_csv('covid_vaccine_statewise.csv')


# In[155]:


tests.head()


# In[165]:


#linear regression
from sklearn.model_selection import train_test_split


# In[286]:


Maha


# In[287]:


[Maha['date']]


# In[288]:


x= Maha[['date', 'cured', 'death']]


# In[289]:


y= Maha[['confirmed']]


# In[290]:


lr=LinearRegression

x
# In[291]:


x


# In[292]:


y


# In[293]:


y


# In[294]:


x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.3)


# In[295]:


y_train.head()


# In[296]:


from sklearn.linear_model import LinearRegression


# In[303]:


y_test


# In[2]:


y1=np.array(y_train).reshape(-1,1)


# In[ ]:





# In[299]:


lr3= LinearRegression


# In[1]:


lr3.fit(np.array(x_train).reshape(-1,1), np.array(y_train).reshape(-1,1))


# In[276]:


x1=np.array(x_train).reshape(-1,1)


# In[254]:


import numpy as np


# In[283]:


y_train


# In[301]:


lr3.fit(x1,y1)


# In[285]:


Maha.tail()


# In[281]:


lr.predict(np.array([[2021-8-21]]))


# In[ ]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime as dt
import numpy as np

df= pd.read_csv('covid_19_india.csv')

df.head()

df= pd.read_csv('covid_19_india.csv', parse_dates=['Date'], dayfirst=True)



df.head()

df= df[['Date', "State/UnionTerritory",'Cured','Deaths', 'Confirmed']]

df.head()

df.columns=['date', 'state', 'cured','death', 'confirmed']

df.head()

df[df['state']=='Kerala']

df[df['state']=='Maharashtra']

delhi= df[df.state=='Delhi']

delhi.head()

df['date']=='2021-08-11'

exactdate= df[df['date']=='2021-08-11']

exactdate= df[df.date=='2021-08-11']

exactdate.head()

confirmedcaseonexactdate=exactdate.sort_values(by='confirmed', ascending=False)

confirmedcaseonexactdate.head()

sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state', y='confirmed', data=confirmedcaseonexactdate.head(), hue='state')

plt.show





exactdeath=exactdate.sort_values(by='death', ascending=False)

exactdeath.head()

sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state', y='death', data=exactdeath.head(),hue='state')
plt.show()

cured=exactdate.sort_values(by='cured', ascending=False)

cured.head()

sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state',y='cured', data=cured.head(), hue='state')
plt.show

Maha=df[df.state=='Maharashtra']

Maha.head()

sns.set(rc={'figure.figsize': (15,10)})
sns.lineplot(x='date', y='confirmed', data=Maha)
plt.show()

sns.set(rc={'figure.figsize': (15,10)})
sns.lineplot(x='date', y='death', data=Maha)
plt.show()

tests= pd.read_csv('covid_vaccine_statewise.csv')

tests.head()

#linear regression
from sklearn.model_selection import train_test_split

Maha

[Maha['date']]

x= Maha[['date', 'cured', 'death']]

y= Maha[['confirmed']]

lr=LinearRegression

x

x

y

y

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.3)

y_train.head()

from sklearn.linear_model import LinearRegression

y_test

y1=np.array(y_train).reshape(-1,1)



lr3= LinearRegression

lr3.fit(np.array(x_train).reshape(-1,1), np.array(y_train).reshape(-1,1))

x1=np.array(x_train).reshape(-1,1)

import numpy as np

y_train

lr3.fit(x1,y1)

Maha.tail()

lr.predict(np.array([[2021-8-21]]))


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




