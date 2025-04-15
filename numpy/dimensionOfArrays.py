# numpy ko import karne ke liye import numpy as np ka use hota hai
# array create karne ke liye np.array() we will use this
# import numpy as np
# a = np.array([1,2,3])
# print(a)
# print(type(a))


# array input and apend in the list formate
# list = []

# for i in range(1,5):
#     int_1 = int(input("enter :"))
#     list.append(int_1)

# print(np.array(list))



# type of arrays->
# 1D-Arrays,2D-Arrays,3D-Arrays,High Dimensional Arrays
# dimensins ka pata lagane ke liye square brackets ko count karte hai and **ndim** se bhi pata aga sakte hai 
# and n terms ke liye dimensions banane ho to **ndmin**ka use karte hai.
# data length should be same in the list of 2D.([1,2,3],[2,4,5])
import numpy as np
x = np.array([1,2,3])
ar2 = np.array([[1,2,3], [2,3,4]])
ar3 = np.array([[[1,3,4,5], [1,2,3,4]]])
print(ar3)
print(ar3.ndim)
print(ar2)
print(ar2.ndim)
print(x)
print(x.ndim)

arn = np.array([1,2,3],ndmin = 10)
print(arn)
print(arn.ndim)


