# join array--- joining means putting contents of two or more arrays in a single
# array.The number of data should be equal so that it can mearge
# their are two methods to mearge the 1D,2D,3D arrays
# var.concatinate--- we have give the axis=1 or 0 for 2dimentions and more to get rows or columns to concatinate
# var.stack----- can merge without or with axis to mere the hight,column,rows of 
# the arrays with--var.hstack---for rows,var.vstack---for columns,var.dstack---for height

# import numpy as np
# var = np.array([1,2,3,4,5,6])
# var0 = np.array([5,6,7,8,9,10])


# ar_merge = np.concatenate((var,var0))
# print(ar_merge)



# import numpy as np
# var = np.array([[11,12,13],[14,15,16]])
# var0 = np.array([[55,66,77],[88,99,10]])


# ar_merge = np.concatenate((var,var0),axis=0)
# print(ar_merge)







# import numpy as np
# var = np.array([[11,12,13],[14,15,16]])
# var0 = np.array([[55,66,77],[88,99,10]])


# ar_merge = np.stack((var,var0),axis=1)
# print(ar_merge)







# import numpy as np
# var = np.array([[11,12,13],[14,15,16]])
# var0 = np.array([[55,66,77],[88,99,10]])


# ar_merge = np.vstack((var,var0))
# arRow = np.hstack((var,var0))
# print(arRow)
# print(ar_merge)













# split_ array-----> splitting breaks onearray into multiple
# 1Dimentiion array splitting
# import numpy as np
# var = ([11,12,13,14,15,16])

# ar_split = np.array_split(var,3)

# print(var)
# print()
# print("split of array is: ", ar_split)





# 2dimention array splitting
import numpy as np
var =np.array([[11,12],[13,14],[15,16]])

ar_split = np.array_split(var,3)

ar_split1 = np.array_split(var,3,axis=1)

print("dimention of array is: ", var.ndim)
print()
print("split of array is: ", ar_split)
print("split of array with axis is: ", ar_split1)