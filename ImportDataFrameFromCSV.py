#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# Read csv file and specify file directory
data = pd.read_csv(r'C:\Users\dperd\OneDrive\Desktop\all_040_in_12.P1.csv')
# Specify the columns in the csv file to display 
df = pd.DataFrame(data, columns= ['NAME', 'STATE', 'POP100'])
# Display the dataframe 
print (df)


# In[ ]:




