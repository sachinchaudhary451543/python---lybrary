# we can check the row and column with the help of the shape and reshaping
# we can use the .shape to know the row and column
# we can use ndmin= to make he array dimentions
# we can create the two dimention array with row and columns by the .reshape(row,col)
# reshaping me ham column and row out of data nhi  le sakte
import numpy as np

# var = np.array([[3,4],[1,2]])

# print(var)
# print()
# print(var.shape)


# var1 = np.array([1,2,3,4,5],ndmin=4)
# print(var1)
# print()
# print(var1.ndim)
# print(var1.shape)











# var2 = np.array([1,2,3,4,5,6])
# print(var2)
# print(var2.ndim)
# print()

# x = var2.reshape(3,2)
# print(x)
# print(x.ndim)





# we can create the 3 dimention with reshaping
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(x)
print(x.ndim)
print()
x1 = x.reshape(2,3,2)

print(x1)
print(x1.ndim)



# again when we convert in to one dimention
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(x)
print(x.ndim)
print()
x1 = x.reshape(2,3,2)

print(x1)
print(x1.ndim)

one = x1.reshape(-1)
print(one)
print(one.ndim)