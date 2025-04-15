# # np.inert(var,index,element)----> we can insert only the integer data this will ignore the float
# import numpy as np
# var = np.array([11,22,33,55])

# x = np.insert(var,3,44)
# print(var)
# print(x)




# 2Dimention array inserting
# import numpy as np
# var2D = np.array([[11,22,33],[44,55,66]])
# x = np.insert(var2D,2,[77,88,99], axis=0)
# y = np.insert(var2D,2,[101,102], axis=1)
# print(var2D)
# print("Row wise", x)
# print("Column wise", y)





# np.append(var,index,element)----> also add the element in the array at the last
# import numpy as np
# var = np.array([11,22,33,44])
# x = np.append(var,55)
# print(var)
# print(x)





# 2D array append------------------
# import numpy as np
# var2D = np.array([[11,22,33],[44,55,66]])
# x = np.append(var2D,[[23,24,25]],axis=0)
# print(var2D)
# print(x)





# np.delete(var,index)-----------------------------
import numpy as np
var = np.array([11,22,33,44,55,66])

x = np.delete(var,3)
print(var)
print(x)