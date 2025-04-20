# we can remove the NaN filled cells with the help of dropna
# dropna() will not make the changes in the original data, it will just show the data without NaN cells
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# print(var)
# var.dropna()




# we can remove the nan data from column or row by using the asix=0 or 1
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")

# print(var.dropna(axis=0))






# we can also use the dropna(how="any") this will remove the all blank/Na cells or rows
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")

# print(var.dropna(how= "any"))




# this function only removes the fully blank/Na row form the data

# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")

# print(var.dropna(how= "all"))





# we can remove the Na cells from columns with the help of dropna(subset="col_name")
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")

# print(var.dropna(subset="Mobile No."))






# this funcion will remove all the data of NaN (inplace=True) make the changes in the original data
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# var.dropna(inplace=True)
# print(var)





# we can also use the dropna(thresh= na numbers in the row) means when  row having the multiple Na cells in that we can pass the number how many 
# Na we can remove 
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# var.dropna(thresh=2)
# print(var)







# ---->var.fillna("any_name")
# we can fil the NaN cells with this function but never updaed in the original data
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# print(var.fillna("sp.chaudhary"))

# the every NaN cell will filled with this name








# we can also fill the cells by the column wise by passing the keywords in the dictionary var.fillna({"column_name":"data_name"})
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# print(var.fillna({"Registration No.":"mistake replace1","Name":"spchaudhary"}))









# we can fill the NaN cells with their nearby forward or backword data cells 
# we will use the function var.fillna(method="bfill") and var.fillna(method="ffill")
# also we ca give the axis in these methods axis = 0 for column wise
# and axis= 1 for row wise 
# these functions will never make the changes to the original data
# -------------------------------------------------------------
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# print(var.fillna(method= "bfill", axis=0))

# ==================================================================
# result_in this the first row filled with the data of second because we used there axis=0 for column
# and method="bfill" filled the forward data to the frst row
# # same thing goes for method="ffill"
# 0          PD000721  Mrs. Mitali Singh Thakur  ...  SHOP(411 Sq Ft)    SHOP-1        
# 1          PD000721  Mrs. Mitali Singh Thakur  ...  SHOP(411 Sq Ft)    SHOP-1        
# 2          PD000727         Mrs. Kavita Saini  ...  SHOP(280 Sq Ft)   SHOP-10   






# method="ffill"
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# print(var.fillna(method= "ffill", axis=0))
# print(var)











# function___> var.fillna(value,inplace=True)===>wil replace the NaN with the value given in the inplace function
# this makes the changes to original data
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# var.fillna(121,inplace=True)
# print(var)
# all the NaN cells will be replaced with the value--121 we can also give the string for the value.





#--------------function__> var.fillna(value,limit = 1)
# limit will also replace the column NaN cells with the values
# but limit=1 or any number what ever we pass in this function means that it will replace only that numbers of the first NaN in the column
# will only be replaced not all that's why it's limited function

import pandas as pd
var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
print(var.fillna("sachin",limit=1))
print(var) 