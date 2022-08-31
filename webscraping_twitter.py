#!/usr/bin/env python
# coding: utf-8

# In[1]:


import twint
import nest_asyncio
nest_asyncio.apply()


# In[2]:


# Configure
c = twint.Config()
c.Search = "\"Booster shot\"" "Omicron"
c.Store_csv = True
c.Output = "Desktop/Assignment1.csv"
c.Lang = "en"
c.Limit = 300
twint.run.Search(c)


# In[3]:


import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("Desktop/Assignment1.csv")
final = data['tweet'].str.lower()


# In[4]:


omicron = []
se = []
booster = []
vaccine = []
for i in range (0,len(final)):
    omicron.append(final[i].count("omicron"))
    se.append(final[i].count("side effect"))
    booster.append(final[i].count("booster"))
    vaccine.append(final[i].count("vaccine"))
s_o = sum(omicron)
s_se = sum(se)
s_b = sum(booster)
s_v = sum(vaccine)


# In[5]:


x = ('side effect','omicron' , 'booster', 'vaccine' )
y = (s_se,s_o,s_b, s_v)
plt.bar(x,y,align='center') # A bar chart
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.50)
plt.title('Word Frequency Histogram')
plt.show()


# In[6]:


print(final)


# In[ ]:




