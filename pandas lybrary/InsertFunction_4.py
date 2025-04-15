# we caninsert and delete th data
# we will use var.insert(index,name of col,data or var["a"](copy of any data))
# data length should be same as the older having
# import pandas as pd
# var = pd.DataFrame({"a":[1,2,3,4,5],"b":[1,2,3,4,5]})

# var.insert(1,"new", [11,22,12,12,13])

# print(var)
# var.insert(0,"zero",var["b"])
# print(var)






# we can copy teh spacific data from any column
# insert function have three parametres first index, second new data name, last the data which you want to insert
# this function will give us the data from "a" index 0 to 3 and insert in the var

# import pandas as pd
# var = pd.DataFrame({"a":[1,2,3,4,5],"b":[1,2,3,4,5]})
# print(var)
# var["newCopy"] = var["a"][:3]
# print(var)

# result
#    a  b  newCopy
# 0  1  1      1.0
# 1  2  2      2.0
# 2  3  3      3.0
# 3  4  4      NaN
# 4  5  5      NaN