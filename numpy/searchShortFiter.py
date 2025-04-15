# Search Array--->
# Search an array for a certain value, and return teh indexes that get a match.
# we can also make the functional conditions inside the np.where()
# import numpy as np
# var = np.array([12,13,14,15,6,8,20])

# x = np.where((var == 6))
# print("the element is on index: ", x)



# we can also make the modulas function inside the where
# ((var%2)==0) means when we devide the data to 2 then how many place or elements will
# fully devide, refect the indexes of them
# import numpy as np
# var = np.array([12,13,14,15,6,8,20])

# x = np.where((var%2)==0)
# print("the element is on index: ", x)







# search Sorted Aray:---> which perform a binary search in the array,and returns the index where the apecified value would be in
# inserted to maintain the search order.
# we can also insert the fully list to the data or can search the sort for digt or left with side="right"
# import numpy as np
# var = np.array([11,12,14,15,17,18])
# x = np.searchsorted(var,[13,20,16])
# x1 = np.searchsorted(var,[21],side= 'left')

# print("search of sorted: ",x)
# print("search of sorted: ",x1)







# Sort Array-------> Ordered sequence is any sequence that has an
# order correspondence to elements,like numeri or alphabetical,
# ascending or descending.
# import numpy as np
# var = np.array([12,23,34,5,24,25,21])
# var2D = np.array([[5,4,3],[8,7,9]])
# print("dimention of array: ",var.ndim)
# print(var)
# print("Ascending order of array: ", np.sort(var))
# print() 
# print("dimention of array: ",var2D.ndim)
# print(var2D)
# print("Ascending order of array: ", np.sort(var2D))








# Filter Array---> Getting some elements out of an existing arry
# and creating a new array out of them
# to make the filter for those whom you want to show you have to give the true value
import numpy as np
var = np.array(["Ram","Krishna","Radha","Raghu","sachin"])
x = [True,True,True,False,False]
final_var = var[x]
print(final_var)
print(type(final_var))