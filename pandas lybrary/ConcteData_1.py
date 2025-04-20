# we can merge the data in teh seprate parts but data can't be merge
# import pandas as pd
# data_1 = pd.DataFrame({"A":[1,2,3]})
# data_2 = pd.DataFrame({"A":[1,2,3]})

# final_data= pd.concat([data_1,data_2])
# print(final_data)
# ======================================================================
# output
#   A
# 0  1
# 1  2
# 2  3
# 0  1
# 1  2
# 2  3
# ==========================================================================





# also we can merge that data with axis=0 will merge the data in colimns and axis=1 will merge ro wise
# import pandas as pd
# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]})
# var2 = pd.DataFrame({"A":[1,2,3,4,6],"B":[121,232,343,454,565]})


# var_merge = pd.concat([var1,var2],axis=0)
# print(var_merge)






# we can gve the key frames to the merged data to identify at axis=1
# import pandas as pd
# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]})
# var2 = pd.DataFrame({"A":[1,2,3,4,6],"B":[121,232,343,454,565]})


# var_merge = pd.concat([var1,var2],axis=1,keys=["d_1","d_2"])
# print(var_merge)



# import pandas as pd
# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]})
# var2 = pd.DataFrame({"A":[1,2,3,4,6],"B":[121,232,343,454,565]})


# var_merge = pd.concat([var1,var2],axis=0,keys=["d_1","d_2"])
# print(var_merge)








# we can mere the one dimention or two dimention data

import pandas as pd
var1 = pd.DataFrame({"D":[1,2,3,4,5],})
var2 = pd.DataFrame({"A":[1,2,3,4,6],"B":[121,232,343,454,565]})


var_merge = pd.concat([var1,var2],axis=1,keys=["d_1","d_2"])
print(var_merge)