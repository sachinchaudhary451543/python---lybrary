# we can join the two dataframe in to single dataframe
# import pandas as pd

# var1 = pd.DataFrame({"A":[111,112,113,114,115],"B":[21,22,23,24,25]})
# var2 = pd.DataFrame({"C":[11,12,13,14,16],"D":[121,232,343,454,565]})

# new_var = var1.join(var2)
# print(new_var)




# # also if our data does not have the same length still it can work but this will show the NAN cells
# import pandas as pd

# var1 = pd.DataFrame({"A":[111,112,113,114,115],"B":[21,22,23,24,25]})
# var2 = pd.DataFrame({"C":[11,12,13,],"D":[121,232,343]})

# new_var = var1.join(var2)
# print(new_var)


# ==============================================================================
# output
# #      A   B     C      D
# 0  111  21  11.0  121.0
# 1  112  22  12.0  232.0
# 2  113  23  13.0  343.0
# 3  114  24   NaN    NaN
# 4  115  25   NaN    NaN
# ==============================================================================










# if we wants to give index to any dataframe, at that time we have to give the indexes to all dataframes
# and remember that arrangethe dataframe to first column which is not having the blank spaces or less length 
# other then other dataframe



# when we will not give the indexes to all dataframe....
# import pandas as pd

# var1 = pd.DataFrame({"A":[111,112,113,114,115],"B":[21,22,23,24,25]},index=["i","ii","iii","iv","v"])
# var2 = pd.DataFrame({"C":[11,12,13,],"D":[121,232,343]})

# new_var = var1.join(var2)
# print(new_var)

# =========================================================
# # output
#        A   B   C   D
# i    111  21 NaN NaN
# ii   112  22 NaN NaN
# iii  113  23 NaN NaN
# iv   114  24 NaN NaN
# v    115  25 NaN NaN
# ==========================================================






# when we give indexes to all dataframe
# import pandas as pd

# var1 = pd.DataFrame({"A":[111,112,113,114,115],"B":[21,22,23,24,25]},index=["i","ii","iii","iv","v"])
# var2 = pd.DataFrame({"C":[11,12,13,],"D":[121,232,343]},index=["i","ii","iii"])

# new_var = var1.join(var2)
# print(new_var)


# ========================================
# output
#        A   B     C      D
# i    111  21  11.0  121.0
# ii   112  22  12.0  232.0
# iii  113  23  13.0  343.0
# iv   114  24   NaN    NaN
# v    115  25   NaN    NaN
# ===================================================











# when we use the second dataframe to first which is having he less length
# import pandas as pd

# var1 = pd.DataFrame({"A":[111,112,113,114,115],"B":[21,22,23,24,25]},index=["i","ii","iii","iv","v"])
# var2 = pd.DataFrame({"C":[11,12,13,],"D":[121,232,343]},index=["i","ii","iii"])

# new_var = var2.join(var1)
# print(new_var)
# ===================================================
# # output
#       C    D    A   B
# i    11  121  111  21
# ii   12  232  112  22
# iii  13  343  113  23
# the result will come according to the first data's length








# try with parameters like--->inner,outer,right,left
# import pandas as pd

# var1 = pd.DataFrame({"A":[111,112,113,114,115],"B":[21,22,23,24,25]},index=["i","ii","iii","iv","v"])
# var2 = pd.DataFrame({"C":[11,12,13,],"D":[121,232,343]},index=["i","ii","iii"])

# new_var = var2.join(var1,how="outer")
# print(new_var)
# # ===============================
# # output
#         C      D    A   B
# i    11.0  121.0  111  21
# ii   12.0  232.0  112  22
# iii  13.0  343.0  113  23
# iv    NaN    NaN  114  24
# v     NaN    NaN  115  25



# ====================================================================
# import pandas as pd

# var1 = pd.DataFrame({"A":[111,112,113,114,115],"B":[21,22,23,24,25]},index=["i","ii","iii","iv","v"])
# var2 = pd.DataFrame({"C":[11,12,13,],"D":[121,232,343]},index=["i","ii","iii"])

# new_var = var2.join(var1,how="right")
# print(new_var)
# ===============this will give the output according to the right side data length
#         C      D    A   B
# i    11.0  121.0  111  21
# ii   12.0  232.0  112  22
# iii  13.0  343.0  113  23
# iv    NaN    NaN  114  24
# v     NaN    NaN  115  25
# ======================================================================================



# if we are having the same data heading for the columns my output will give the error so we can use the suffix to give the diffrent names
# rsufficx-->means name for right side data.,lsuffix---> means name for the left side data
import pandas as pd

var1 = pd.DataFrame({"A":[111,112,113,114,115],"B":[21,22,23,24,25]},index=["i","ii","iii","iv","v"])
var2 = pd.DataFrame({"C":[11,12,13,],"B":[121,232,343]},index=["i","ii","iii"])

new_var = var2.join(var1,how="right",rsuffix="(Bold)")
print(new_var)

# ================================================
# output
#         C      B    A  B(Bold)
# i    11.0  121.0  111     21
# ii   12.0  232.0  112     22
# iii  13.0  343.0  113     23
# iv    NaN    NaN  114     24
# v     NaN    NaN  115     25