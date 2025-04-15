# data structure in Python Pandas
# The pandas provides two data structures for processing the data.
# Series & DataFrame and Panel


# Series data structure
# it is defines as a one dimentional array that is capable of storing varios data types
# import pandas as pd
# a = pd.Series()
# print(a)




# import pandas as pd
# x = [1,2,3,4,5]
# var = pd.Series(x)
# print(var)



# we can also change the indexing of the series
import pandas as pd
x = [1,2,3,4,5]
var = pd.Series(x,index=['a','b','c','d','e'],dtype="float",name="Python")
print(var)



# we can create the dicsnory
# import pandas as pd
# var =  {"pragrammes":["python","Java","c","c++","PHP"],"Creits":[8,4,2,2,2],"ranking":[1,2,3,4,5]}
# x = pd.Series(var)
# print(x)