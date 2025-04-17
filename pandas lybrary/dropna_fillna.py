# we can remove the NaN filled cells with the help of dropna
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# print(var)
# var.dropna()




# we can remove the nan data from column or row by using the asix=0 or 1
import pandas as pd
var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")

print(var.dropna(axis=0))