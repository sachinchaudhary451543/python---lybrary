# we have any data with their column names but if any column have the multiple same names in that,we can make them in a group but the length should be same
import pandas as pd 
var = pd.DataFrame({"Name":["a","b","c","b","b","a","a","c"],
                    "s_1":[11,12,13,14,15,16,17,18],
                    "s_2":[2,22,222,222,3,33,333,4]})
new_var = var.groupby("Name")


for x,y in new_var:
    print(x)
    print(y)
    print()





# and now we can get the min,max,mean from this data


# we can access sepratly
print("here is the data of a: \n", new_var.get_group("a"))
# min,max,mean values of the whole data
print("here is the Min: \n", new_var.min())
print("here is the Max: \n", new_var.max())
print("here is the Mean: \n", new_var.mean())



# also we can convert this data in teh list

li = list(new_var)
print("data in teh ist formate: \n\n",li)