# we can say this two dimention data
# import pandas as pd
# list = [1,2,3,4,5]
# var = pd.DataFrame(list)
# print(var)





# we can create also the dictnory with their column names
# we have to same length of the columns
# we can also print the columns or access columns sepratly

# import pandas as pd
# d = {"A":[11,22,33,44],"B":[11,22,33,44],"D":[11,22,33,44]}
# var = pd.DataFrame(d)
# var1 = pd.DataFrame(d,columns=["A","B"])
# print(var)
# print(type(var))
# print(var1)




# it provides the by default index starting from 0 but we can change them
# import pandas as pd
# d = {"A":[11,22,33,44],"B":[11,22,33,44],"D":[11,22,33,44]}
# var = pd.DataFrame(d)
# var1 = pd.DataFrame(d,columns=["A","B"],index=["i","ii","iii","iv"])
# print(var)
# print(type(var))
# print(var1)





# how to get the data from the dictonary
# print(var[column][index])
# import pandas as pd
# d = {"A":[11,22,33,44],"B":[21,32,43,54],"D":[61,72,83,94]}
# var = pd.DataFrame(d)

# print("data sheet:\n", var)


# e = input("Enter the column: ")
# f = input("Enter the index: ")


# dataName = var[str(e)][int(f)]
# print("here is the data of col:", e, "ind:", f,"-->",dataName)








#  we can also create the list with the data frame
# import pandas as pd
# list_1 = [[1,2,3,4,5,6],[7,8,9,11,12,13]]

# var = pd.DataFrame(list_1)
# print(var)






# we can also make the dataframe wit the series
# two eries can mae the dataframe
import pandas as pd
d = {"A":pd.Series([11,22,33,44]),"B":pd.Series([21,32,43,54]),"D":pd.Series([61,72,83,94])}
var = pd.DataFrame(d)

print(var)
