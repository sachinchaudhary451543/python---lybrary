# np.min(x)--->minimum value
# np.max(x)--->max value
# np.argmin(x)---> this finds the index of the min, max value's
# np.sqrt(x)---.> square root
# np.sin(x)--->sinvalue
# np.cos(x)--->cosvalue
# np.cumsum(x)--->this adds their upcoming values in that


# examples for one dimentions
import numpy as np
var = np.array([1,2,3,4,5,6,7,8])
squareroot = np.array([81,4,9,16])
sinValues = np.array([0])
cosValues = np.array([0])
print("comunity sum: ",var, "-->", np.cumsum(var))
print("minimum value is: ",var, "-->", np.min(var), "value Index in the array: ", np.argmin(var))
print("maximum value is: ",var, "-->", np.max(var), "value Index in the array: ", np.argmax(var))
print("square root of array: ",squareroot, "-->", np.sqrt(squareroot))
print()
print("sin 0: ", np.sin(sinValues), "cos 0: ", np.cos(cosValues))




# when we try to get the arithmetic functions applied in the two dimention 
# array we have to give the axis=0 for column and axis=1 for the rows


# example
# import numpy as np
# var = np.array([[1,2,3,56,44],[1,2,3,4,5]])
# print("minimum value in the col: ", np.min(var, axis=0))
# print("max value in row", np.max(var, axis=1))