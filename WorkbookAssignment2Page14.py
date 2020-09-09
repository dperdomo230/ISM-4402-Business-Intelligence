#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine

# Connect to sqlite db
db_file = r'C:\Users\dperd\Downloads\datasets\datasets\salesdata.db'
engine = create_engine(r"sqlite:///{}"
 .format(db_file))
# This is a basic sql query
sql = "select * from sqlite_master;" 
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[ ]:





# In[ ]:




