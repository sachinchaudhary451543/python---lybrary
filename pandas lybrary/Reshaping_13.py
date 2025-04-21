# Pivot table and melt function

# melt---->we can make the data vartical or horizontal
# import pandas as pd
# var = pd.DataFrame({"days":[1,2,3,4,5,6,7],"English":[22,35,34,55,67,78,90],"Hindi":[22,35,34,55,67,78,90],"Maths":[22,35,34,55,67,78,90]})

# new_var = pd.melt(var)
# print(new_var)





# we can make any of the column as a index with the id_vars=["coll_head_name"] function
# import pandas as pd
# var = pd.DataFrame({"days":[1,2,3,4,5,6,7],"English":[22,35,34,55,67,78,90],"Hindi":[22,35,34,55,67,78,90],"Maths":[22,35,34,55,67,78,90]})

# new_var = pd.melt(var,id_vars=["days"])
# print(new_var)

# ==================================================================================
# output
#     days variable  value
# 0      1  English     22
# 1      2  English     35
# 2      3  English     34
# 3      4  English     55
# 4      5  English     67
# 5      6  English     78
# 6      7  English     90
# 7      1    Hindi     22
# 8      2    Hindi     35
# 9      3    Hindi     34
# 10     4    Hindi     55
# 11     5    Hindi     67
# 12     6    Hindi     78
# 13     7    Hindi     90
# 14     1    Maths     22
# 15     2    Maths     35
# 16     3    Maths     34
# 17     4    Maths     55
# 18     5    Maths     67
# 19     6    Maths     78
# 20     7    Maths     90





# we can give the names to the heads after the vertical reshaping of the data
# import pandas as pd
# var = pd.DataFrame({"days":[1,2,3,4,5,6,7],"English":[22,35,34,55,67,78,90],"Hindi":[22,35,34,55,67,78,90],"Maths":[22,35,34,55,67,78,90]})

# new_var = pd.melt(var,id_vars=["days"],var_name="subjects",value_name="marks")
# print(new_var)
# =========================================================================================
# output
#     days subjects  marks
# 0      1  English     22
# 1      2  English     35
# 2      3  English     34
# 3      4  English     55
# 4      5  English     67
# 5      6  English     78
# 6      7  English     90
# 7      1    Hindi     22
# 8      2    Hindi     35
# 9      3    Hindi     34
# 10     4    Hindi     55
# 11     5    Hindi     67
# 12     6    Hindi     78
# 13     7    Hindi     90
# 14     1    Maths     22
# 15     2    Maths     35
# 16     3    Maths     34
# 17     4    Maths     55
# 18     5    Maths     67
# 19     6    Maths     78
# 20     7    Maths     90
# ==========================================================
# ==========================================================





# pivot()--->we can short the data according to any column
# we have to give first index column name then give the column to short according with
# import pandas as pd
# var = pd.DataFrame({"days":[1,2,3,4,5,6,7],
#                     "student":["a","b","a","b","a","b","a"],
#                     "English":[22,35,34,55,67,78,90],
#                     "Hindi":[22,35,34,55,67,78,90],
#                     "Maths":[22,35,34,55,67,78,90]})

# new_var = var.pivot(index="days",columns="student")
# print(new_var)




# we can also show only one column of the value use-->value="column_name"
# import pandas as pd
# var = pd.DataFrame({"days":[1,2,3,4,5,6,7],
#                     "student":["a","b","a","b","a","b","a"],
#                     "English":[22,35,34,55,67,78,90],
#                     "Hindi":[22,35,34,55,67,78,90],
#                     "Maths":[22,35,34,55,67,78,90]})

# new_var = var.pivot(index="days",columns="student",values="English")
# print(new_var)














# we can do the mathemetical functions in this data
# --->aggfunc="sum"
# --->aggfunc="mean",margin="True" (to get the avrage)
import pandas as pd
var = pd.DataFrame({"days":[1,1,1,2,2,2,1],
                    "student":["a","b","a","b","a","b","a"],
                    "English":[22,35,34,55,67,78,90],
                    "Hindi":[22,35,34,55,67,78,90],
                    "Maths":[22,35,34,55,67,78,90]})

new_var = var.pivot_table(index="student",columns="days",
                        aggfunc="mean", margins="True")
print(new_var)