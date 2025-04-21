# when we use the append function ths will add the two same columns to single columns but it never merge the diffrent columns with diffrent heading name
# import pandas as pd
# var1 = pd.DataFrame({"A":[11,22,33,44,55],"B":[1,2,3,4,5]})
# var2 = pd.DataFrame({"C":[12,13,14,15,16],"B":[6,7,8,9,10]})


# new_var = var1._append(var2)
# print(new_var)


# ================================output
#       A   B     C
# 0  11.0   1   NaN
# 1  22.0   2   NaN
# 2  33.0   3   NaN
# 3  44.0   4   NaN
# 4  55.0   5   NaN
# 0   NaN   6  12.0
# 1   NaN   7  13.0
# 2   NaN   8  14.0
# 3   NaN   9  15.0
# 4   NaN  10  16.0


# ==========in this case the indexes are in the repeat format so we will use the ignore_index=True
import pandas as pd
var1 = pd.DataFrame({"A":[11,22,33,44,55],"B":[1,2,3,4,5]})
var2 = pd.DataFrame({"C":[12,13,14,15,16],"B":[6,7,8,9,10]})


new_var = var1._append(var2,ignore_index=True)
print(new_var)
# ==============================================
#       A   B     C
# 0  11.0   1   NaN
# 1  22.0   2   NaN
# 2  33.0   3   NaN
# 3  44.0   4   NaN
# 4  55.0   5   NaN
# 5   NaN   6  12.0
# 6   NaN   7  13.0
# 7   NaN   8  14.0
# 8   NaN   9  15.0
# 9   NaN  10  16.0