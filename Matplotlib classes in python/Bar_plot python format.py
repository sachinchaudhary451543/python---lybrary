#!/usr/bin/env python
# coding: utf-8

# # BAR PLOT

# # we can give the label of data and title,coor,font size we can see all related codes in this code

# # we can give the width between 0 to 1 to the bars

# In[39]:


import matplotlib.pyplot as plt
x = ["python","c","c++","JAVA"]
y = [85,70,60,82]
plt.xlabel("Language",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("S.TECH.ANALYSIS",fontsize=15)
c = ["y","b","m","g"]
plt.bar(x,y,color=c,width=0.2)
plt.show()
           


# # we can align the names of the bars at the edge or center for the bars

# In[42]:


import matplotlib.pyplot as plt
x = ["python","c","c++","JAVA"]
y = [85,70,60,82]
plt.xlabel("Language",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("S.TECH.ANALYSIS",fontsize=15)
c = ["y","b","m","g"]
plt.bar(x,y,color=c,width=0.2,align="edge")
plt.show()
           


# In[ ]:





# # we can also give the borders to the bars also with the changing style of the border

# In[48]:


import matplotlib.pyplot as plt
x = ["python","c","c++","JAVA"]
y = [85,70,60,82]
plt.xlabel("Language",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("S.TECH.ANALYSIS",fontsize=15)
c = ["y","b","m","g"]
plt.bar(x,y,color=c,width=0.2,edgecolor="r",linewidth=4,linestyle=":")
plt.show()
           


# # we can make fade the graph with the alpha

# In[53]:


import matplotlib.pyplot as plt
x = ["python","c","c++","JAVA"]
y = [85,70,60,82]
plt.xlabel("Language",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("S.TECH.ANALYSIS",fontsize=15)
c = ["y","b","m","g"]
plt.bar(x,y,color=c,width=0.2,alpha=0.4)
plt.show()
           


# # we can give the label to the bar with the label="name" with plt.legend() parameter

# In[62]:


import matplotlib.pyplot as plt
x = ["python","c","c++","JAVA"]
y = [85,70,60,82]
plt.xlabel("Language",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("S.TECH.ANALYSIS",fontsize=15)
c = ["y","b","m","g"]
plt.bar(x,y,color=c,width=0.2,label="Prgramming_languages")
plt.legend()
plt.show()
           


# In[76]:


import matplotlib.pyplot as plt
import numpy as np

x = ["python","c","c++","Java"]
y = [85,80,65,82]
z = [20,30,40,50]

width  = 0.2
p = np.arange(len(x))
p1 = [j+width for j in p]

plt.xlabel("language",fontsize = 16)
plt.ylabel("No",fontsize = 16)
plt.title("Tech analysis",fontsize = 16)


plt.bar(p,y,width,color='r',label="popularity")
plt.bar(p1,z,width,color='y',label="popularity1")


plt.legend()
plt.show()


# In[ ]:




