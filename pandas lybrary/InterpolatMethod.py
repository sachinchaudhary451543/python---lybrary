# if we are having the blank cell in the numeric collumns
# the interpolat method can fill that linearly
import pandas as pd
var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\99 SACHIN 13APRIL.csv")

print(var.interpolate(time=5))