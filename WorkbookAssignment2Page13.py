#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
# Import the glob library
import glob

# Set all_data to an empty dataframe
all_data = pd.DataFrame()
# This line will loop through all files that match the pattern 
for f in glob.glob(r'C:\Users\dperd\Downloads\datasets\datasets\weekly_call_data\weekdata*.xlsx'):
 # Load the Excel file in f into one dataframe df
 df = pd.read_excel(f)
 # Append the contents of df to the dataframe all_data
 all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[ ]:





# In[ ]:




