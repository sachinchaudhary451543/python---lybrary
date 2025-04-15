# Indexing of one Dimention Array--------------------

# import numpy as np 
# var = np.array([1,2,3,4,5])

# print("Array dimention is: " , var.ndim, "D")
# print("Indexing: ", var[3])


# Indexing of two Dimention Array--------------------

# import numpy as np
# var1 = np.array([[1,2,3],
#                  [4,5,6]])
# print("Array Dimention is: ", var1.ndim, "D")
# print("Indexing: ", var1[0,2])
# print("Indexing: ", var1[1,2])




# Indexing of three Dimention Array--------------------

# import numpy as np
# var2 = np.array([[[1,2,3]
#                   ,[4,5,6]]])
# print("Array Dimention is: ", var2.ndim, "D")
# print("Indexing: ", var2[0,1,2])
# print("Indexing: ", var2[0,0,2])




# Indexing of four Dimention Array------------------
# import numpy as np
# var2 = np.array([[[[1,2,3]
#                   ,[4,5,6]]]])
# print("Array Dimention is: ", var2.ndim, "D")
# print("Indexing: ", var2[0,0,1,2])
# print("Indexing: ", var2[0,0,0,2])








# one dimention array sliciing-----------------------
# import numpy as np
# var = np.array([2,3,4,5,6,7,8,9,10,11,12])
# print("start to end access: ", var[:])
# print("start to 5th index access: ", var[:6])
# print("2nd index to end access: ", var[2:])
# print("random access 0 index to 5: ", var[0:5:2])







# 2dimention array slicing---------------------
# jab 2d ya 3d array me acces lena hota hai to , ka use karte hai
# import numpy as np
# var2 = np.array([[5,6,7,8,9],[11,12,13,14,15],[22,23,24,25,26]])
# print("get access to 1st array: ", var2[0,1:])
# print("get access to 2nd array: ", var2[1,2:])






# 2dimention array slicing---------------------
import numpy as np
var2 = np.array([[[5,6,7,8,9],[11,12,13,14,15],[22,23,24,25,26]]])
print("get access to 1st array: ", var2[0,0,1:])
print("get access to 2nd array: ", var2[0,1,2:])