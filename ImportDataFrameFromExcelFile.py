#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
# Read the data in the excel file located in the directory noted 
data = pd.read_excel(r'C:\Users\dperd\OneDrive\Desktop\AGE01.xls', sheet_name = 'Sheet1')
# Specify the DataFrame and the columns to display
df = pd.DataFrame(data, columns= ['Areaname','STCOU'])
# Display the DataFrame
print (df)


# In[ ]:




