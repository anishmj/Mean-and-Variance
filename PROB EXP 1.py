#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[1]:


L = [int(i) for i in input().split()]


# In[3]:


N = len(L);M = max(L)


# In[4]:


x = list();f = list()


# In[5]:


for i in range(M+1):
    c=0
    for j in range(N):
        if L[j]==i:
            c = c+1
    f.append(c)
    x.append(i)


# In[6]:


sf = np.sum(f)


# In[ ]:





# In[7]:


p = list()
for i in range(M+1):
    p.append(f[i]/sf)
    


# In[8]:


mean = np.inner(x,p)


# print(mean)

# In[9]:


print(mean)


# In[12]:


ex2 = np.inner(np.square(x),p)


# In[13]:


var = ex2-mean**2


# In[14]:


print(var)


# In[15]:


sd = np.sqrt(var)


# In[16]:


print(sd)


# In[17]:


print("the mean arrival rate is %.3f",mean)


# In[18]:


print("the variance of arrival from feeder is %.3f",var)


# In[20]:


print("the standard deviation of arrival from feeder is %.3f",sd)


# In[21]:


print(M)

