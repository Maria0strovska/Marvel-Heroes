#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Load the libraries
import pandas as pd
from matplotlib import pyplot as plt


# In[11]:


marvel=pd.read_csv('charcters_stats.csv')


# In[12]:


marvel.head()


# In[13]:


#How many chacters do we have? - 611
marvel.shape


# In[14]:


#How many good, bad and neutral characters do we have?
marvel['Alignment'].value_counts()


# In[15]:


#Create table only with good heroes
marvel[marvel['Alignment']=='good']


# In[16]:


good=marvel[marvel['Alignment']=='good']


# In[17]:


good.head()


# In[18]:


#Who among good heroes has the highest speed?
good.sort_values(by=['Speed'], ascending=False).head()


# In[19]:


max_speed_good=good[good ['Speed']==100]


# In[20]:


max_speed_good


# In[21]:


max_speed_good['Alignment'].value_counts()


# In[22]:


#Who among good heroes has the lowest speed?
min_speed_good=good[good ['Speed']==1]


# In[25]:


min_speed_good


# In[56]:


min_speed_good['Alignment'].value_counts()


# In[23]:


#Who among good heroes has the biggest power?
good.sort_values(by=['Power'], ascending=False).head()


# In[28]:


good_max_power_full=good[good['Power']==100]


# In[31]:


good_max_power_full.shape


# In[30]:


good_max_power_full


# In[26]:


good_max_power=good.sort_values(by=['Total'], ascending=False)


# In[27]:


good_max_power.head()


# In[ ]:





# In[33]:


#Create bar chart of the most powerful superheroes
plt.figure(figsize=(8,5))
plt.bar(list(good_max_power['Name'])[0:5], list(good_max_power['Total'])[0:5], color='g')


# In[34]:


#Create table of supervilliance
bad=marvel[marvel['Alignment']=='bad']


# In[35]:


bad.head()


# In[37]:


#Who among supervilliance has the highest speed?
bad.sort_values(by=['Speed'], ascending=False).head()


# In[39]:


#Who among supervilliance is the most intelligence?
bad.sort_values(by=['Intelligence'], ascending=False).head()


# In[40]:


bad.sort_values(by=['Total'], ascending=False).head()


# In[42]:


bad_max_power=bad.sort_values(by=['Total'], ascending=False)


# In[57]:


#Create bar chart of the most powerful supervilliance
plt.figure(figsize=(10,5))
plt.bar(list(bad_max_power['Name'])[0:5], list(bad_max_power['Total'])[0:5], color='r')


# In[51]:


#Histogram for speed of good superheroes
plt.figure(figsize=(10,5))
plt.hist(good['Speed'])
plt.title('Distribution of speed')
plt.xlabel('Speed')
plt.show()


# In[53]:


#Histogram for combat of  supervillians
plt.figure(figsize=(10,5))
plt.hist(bad['Combat'])
plt.title('Distribution of combat')
plt.xlabel('Combat')
plt.show()

