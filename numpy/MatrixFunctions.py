# 1>Transpose,2>Swapaxes,3>Inverse,4>Power,5>Determinate



# 1>Transpose---->we can use wo method to conver metrix to transpose
# np.transpose(variable) or var.T directly in the print
# transpose method converts the row to column , column to row
# import numpy as np
# var = np.matrix([[1,2,3],[4,5,6]])
# print(var)
# print("Transpose with np.transpose method: ", np.transpose(var))

# print("Transpose with var.T method: ", var.T)







# Swapaxes------>in this method we will use the np.swapaxes(var,axis=0,axis=1)
# it will function as transpose but it uses the axis=0,axis=1 to convert row to column
# import numpy as np
# var = np.matrix([[1,2,3],[4,5,6]])
# print(var)
# print("Swapaxes", np.swapaxes(var,0,1))









# Inverse ------> in this method we will make the matrix in inverse
# np.linalg.inv(var)

# import numpy as np
# var = np.matrix([[1,2],[3,4,]])
# print(np.linalg.inv(var))






# Power--->we can get the square of the metrix but it has the 3 ways of power metrix
# np.linalg.matrix_power(var,n)
# where n is the power which can be n>0,n<0 or n=0
# import numpy as np
# var = np.matrix([[1,2],[3,4,]])
# print("Normal array:\n", var)
# print()
# print("n=2 (means square) power metrix: \n", np.linalg.matrix_power(var,2))
# print()
# print("n=0 power metrix: \n", np.linalg.matrix_power(var,0))
# print()
# print("n= -2 (means negative square) power metrix: \n", np.linalg.matrix_power(var,-2))








# Determinant---> we can get the deminente of the metrix (A = |A|) formula -- np.linalg.det(var)
import numpy as np
var = np.matrix([[11,22,33],[33,44,55],[66,77,8]])
print("Normal array:\n", var)
print()


print("Determinante of the metrix: ", np.linalg.det(var))