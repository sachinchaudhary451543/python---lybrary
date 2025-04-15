# copy------------------------------------var.copy()
# the changes made in the copy data does not reflect in the original array.
# and te changes in the original data will not reflect in teh copy
# import numpy as np
# var = np.array([32,21,11,22,23])
# varCopy = var.copy()

# print("Copy of the array is: ", varCopy)
# var[3] = 59
# print("main data after edits: ", var)
# print("copy data afer edits in main: ", varCopy)











# var.view()------------------------------
# the view does not own teh data. any changes made to the view will
# afect the original array,and any changes made to the original may will affect the view
import numpy as np
var = np.array([32,21,11,22,23])
varView = var.view()

print("View of the array is: ", varView)
var[3] = 59
print("main data after edits: ", var)
print("View data afer edits in main: ", varView)
