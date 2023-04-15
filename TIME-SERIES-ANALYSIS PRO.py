#!/usr/bin/env python
# coding: utf-8

# In[21]:


import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm


# In[22]:


import matplotlib
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'


# In[23]:


df = pd.read_excel("C:\\Users\\ANESTHESIA\\Desktop\\Sample - Superstore.xls")
furniture = df.loc[df['Category'] == 'Furniture']


# In[24]:


furniture['Order Date'].min(), furniture['Order Date'].max()


# In[25]:


cols = ['Row ID', 'Order ID', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State', 'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name', 'Quantity', 'Discount', 'Profit']
furniture.drop(cols, axis=1, inplace=True)
furniture = furniture.sort_values('Order Date')


# In[26]:


furniture.isnull().sum()


# In[27]:


furniture = furniture.groupby('Order Date')['Sales'].sum().reset_index()


# In[28]:


furniture = furniture.set_index('Order Date')
furniture.index


# In[29]:


y = furniture['Sales'].resample('MS').mean()


# In[30]:


y['2017':]


# In[31]:


y.plot(figsize=(15, 6))
plt.show()


# In[32]:


from pylab import rcParams
rcParams['figure.figsize'] = 18, 8
decomposition = sm.tsa.seasonal_decompose(y, model='additive')
fig = decomposition.plot()
plt.show()


# In[ ]:





# In[ ]:




