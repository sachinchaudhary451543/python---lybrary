# in the iteration we can get the array data seperatly
# we have to call the for loop to get this
# import numpy as np
# var = np.array([1,2,3,4,5,6])

# print(var)
# print()

# for i in var:
#     print(i)


# for 2d array we will use for loop in loop
# and also the loop in loop creates according to the dimentions

# import numpy as np
# var2D = np.array([[1,2,3],[4,5,6,]])
# print(var2D)
# print()

# for i in var2D:
#     for j in i:
#         print(j)





# 3d array iterations
# import numpy as np
# var3D = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print("Dimention is: ", var3D.ndim)
# print(var3D)
# print()

# for i in var3D:
#     for j in i:
#         for K in j:
#             print(K)





# when we don't want to use the multiple loops in array we can use the 
# nditer() and to conver data to other data type we can use flag= ['buffer'],op_dtypes=['s'] to conver in string
# import numpy as np
# var = np.array([[[1,2,3,4],[5,6,7,8]]])


# for i in np.nditer(var):
#     print(i)


# import numpy as np
# var = np.array([[[1,2,3,4],[5,6,7,8]]])
# print("Dimention of array is: ", var.ndim)

# for i in np.nditer(var,flags=['buffered'],op_dtypes=["S"]):
#     print(i)




# agar ham data ke sath indexing bhi show krna chahte hai to ndenumerate ka use krte hai 
# jese for i, d in np.ndenumerate(var)
# isme i used for index and d is used for data
import numpy as np
var = np.array([[[11,12,13,14],[55,34,3,23]]])
print("Dimention of array is: ", var.ndim)

for i,d in np.ndenumerate(var):
    print("Indexing is: ", i, " | data is: ", d)