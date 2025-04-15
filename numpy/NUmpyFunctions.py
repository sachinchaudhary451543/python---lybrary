# Arithmetic Functions
# shuffle,Unique,Risize,Flatten,Ravel



# suffle function-----> we can print the data random suffle like a playing cards
# np.random.suffle(var)
# import numpy as np
# var = np.array([1,2,3,4,5,6,7,8,9])
# np.random.shuffle(var)
# print(var)
# print("Zero index pr random element: ", var[0])





# Unique------->we can filter the data and remove duplicacy in the array data--with np.Unique(var)
# we can also print the indexing and number of duplicacy of element
# import numpy as np
# var = np.array([1,2,2,3,4,4,5,5,6,7,8,9,9])
# x = np.unique(var)
# indexOfVar = np.unique(var,return_index=True, return_counts=True)

# print("Filtered data removed duplicates: ", x)
# print("indexes and number of duplicate element: ", indexOfVar)









# Resize the array data make the one dimention array to 2 dimention
# import numpy as np
# var = np.array([1,2,3,4,5,6])
# y = np.resize(var,(2,3))
# x = np.resize(var,(3,2))
# z = np.resize(var,(2,2))


# print("x: ",x,"\n y: ",y,"\n z: ",z)







# flatter and ravel --> makes the two dimention data to one dimention and also can give them the direction ffrom row, column 
# "C" means to flatten in row-major order.
# "F" means to flatten in column-major order
# "A" means to flatten in column-major order if "a" is flatten *contiguous*
# in memory, row-major order otherwise.
# "K" means to flatten 'a' in the order otherwise.
# the default is 'c'.
import numpy as np
var = np.array([[1, 2],[3, 4],[5, 6]])

print("flatten without order: ", var.flatten())
print("flatten: ",var.flatten(order="F"))
print("Ravel: ",var.ravel(order="F"))