# matrix and array are seems to be same but they both are having the diffrences 
# for calculations matrix follows the .Dot() to multiply any 2 variables
# but array can directly multiply
import numpy as np
var1 = np.matrix([[1,2,3],[2,3,4],[2,3,4]])
var2 = np.matrix([[1,2,3],[2,3,4],[2,3,4]])
print("Matrix Multiplication: ")
print(var1.dot(var2))
print("Without Dot:", var1*var2)

var3 = np.array([[1,2],[3,4]])
var4 = np.array([[1,2],[3,4]])
print("array multiplication: ", var3*var4)