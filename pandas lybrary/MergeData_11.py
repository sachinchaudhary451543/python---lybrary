# we can merge the common data 
# but the data length should be same 
# import pandas as pd
# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]})
# var2 = pd.DataFrame({"A":[1,2,3,4,5],"c":[111,222,333,444,555]})


# var_merge = pd.merge(var1,var2,on="A")
# print(var_merge)







# ie we don't have he same length of the two datasets we can pass left or right argument  or outer argument
# this will make the data length according to the left data or right data
# how="inner"--->takes the length of the data according to te common data length
# but, how="outer"---> takes the data according the indexing of the length of the common data set. 
# import pandas as pd
# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]})
# var2 = pd.DataFrame({"A":[1,2,3,4,6],"c":[111,222,333,444,555]})


# var_merge = pd.merge(var1,var2,how="inner")
# print(var_merge)








# we can pass the indicator=True to know that which data is common or whic is not
# import pandas as pd
# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]})
# var2 = pd.DataFrame({"A":[1,2,3,4,6],"c":[121,232,343,454,565]})


# var_merge = pd.merge(var1,var2,how="outer",indicator=True)
# print(var_merge)



# if we get the column with the same heading names then we can pass the argument left_index=True or right_index=True
# import pandas as pd
# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]})
# var2 = pd.DataFrame({"A":[1,2,3,4,6],"B":[121,232,343,454,565]})


# var_merge = pd.merge(var1,var2,left_index=True,right_index=True)
# print(var_merge)









# we can also give our data headings a suffix names with the suffix("names") function
import pandas as pd
var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]})
var2 = pd.DataFrame({"A":[1,2,3,4,6],"B":[121,232,343,454,565]})


var_merge = pd.merge(var1,var2,left_index=True,right_index=True,suffixes=("(head_1)","(head_2)"))
print(var_merge)