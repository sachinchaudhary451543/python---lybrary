#!/usr/bin/env python
# coding: utf-8

# #Pandas Functions

# In[3]:


import pandas as pd
var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
var


# #we can get the number of row

# In[8]:


var.index


# #we can find the unique ,min,max from data 

# In[12]:


var.describe()


# #we can get the columns names

# In[14]:


var.columns


# #we can take the fix data from head to bottom

# In[22]:


var.head(2)


# #if we want to take the data from bottom

# In[28]:


var.tail()


# #we can use the slicing to get the data 

# In[37]:


var[6:11]


# #we can also get the data type

# In[42]:


print(type(var))


# #we can also print the indexes of the data in the pandas array

# In[45]:


var.index.array


# #we can make the data as numpy array

# In[48]:


var.to_numpy()


# In[56]:


import numpy as np
csv_1 = np.asarray(var)
csv_1


# #we can short our data as assending or decending formatt

# In[61]:


var.sort_index(axis=0,ascending = False)


# #we can change the data name of any cell in data this is not a right method it ll give the warnings so we can use the .loc[row_index,"column_name"]="New_name"

# In[67]:


var["Registration No."][0]="python"
var


# In[73]:


var.loc[0,"Registration No."]="Java"
var


# #we can use .loc to get the data by row and col var.loc[[row_index_from,row_index_to]["col1","col2"]]

# In[82]:


var.loc[[2,3],["Registration No.","Name",	"Mobile No."]]


# In[84]:


var.loc[:,["Registration No.","Name",	"Mobile No."]]


# In[88]:


var.loc[[2,3],:]


# #we have another function to get the things in data perticularly

# In[91]:


var.iloc[0,1]


# In[97]:


var.iloc[4,3]


# #we can drop any row or collumn from the whole data by the var.drop[index_row_or_col,axis=0]   axis=0 for row and axis=1 for col

# In[104]:


var.drop("Name",axis=1)


# In[106]:


var.drop(0,axis=0)


# In[ ]:





# In[ ]:




