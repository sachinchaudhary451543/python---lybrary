# a+b ---> np.add(a,b)
# a-b ---> np.subtract(a,b)
# a*b ---> np.multiply(a,b)
# a/b ---> np.devide(a,b)
# a%b ---> np.mod(a,b)
# a**b ---> np.power(a,b)
# 1/a ---> np.reciprocal(a)


# let's practice these in one dimention array that's the method 1
# import numpy as np 
# var = np.array([1,2,3,4])

# Add = var + 3
# sub = var - 2
# dev = var / 3
# mod = var % 3
# mult = var * 10
# print("Add: ", Add, "\n\n", "sub: ", sub , "\n\n","dev: ", dev, "\n\n","mod: ",  mod,"\n\n","mult: ", mult, "\n\n")


# Add2 = np.add(var,5)
# sub2 = np.subtract(var,0.5)
# print("method 2nd for addition: ", Add2, "\n\n","method 2nd of subtract: ",sub2)




# second method with the oprations
import numpy as np
var1 = np.array([1,2,3,4])
var2 = np.array([1,2,3,4])

varAdd = np.add(var1, var2)
varRsiprocal = np.reciprocal(var1)
print(varRsiprocal, "\n")

print(varAdd)








# arithmetic oprations in 2D array
# import numpy as np
# var2D1 = np.array([[1,2,3,4],[1,2,3,4]])
# var2D2 = np.array([[1,2,3,4],[1,2,3,4]])


# varAdd2D = np.add(var2D1,var2D2)
# var2Add = var2D1 + var2D2
# print(var2Add, "\n")
# print(varAdd2D)