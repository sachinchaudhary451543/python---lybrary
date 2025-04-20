# var.replace(to_replace="value_from_data_toReplace",value="name_toreplace_with") wil replace the perticular cell data to that value we provde

# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# print(var.replace(to_replace="Mrs. Mitali Singh Thakur",value="RED_HAT"))






# we can replace the serial numbers

# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# print(var.replace([1,2,3,4,5,6],121))






# we can also change the data alphabetically
# var.replace("data_to_replace","data_after_replace",regex=True)
# in this example the small a to z alphabets will replace with &&& we can take any thing
# # but we have to pass the argument regex=True
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# print(var.replace("[a-z]","&&&",regex=True))







# we can replace with the dictionary method for the columns
# var.replace({"column_name":"[replaceable_data]"},"replace_with",regex=True)
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# print(var.replace({"Registration No.":"[A-Z]"},"&&&&",regex=True))








# WE can also fill any data with the forward or backword data in the column
# we will use the syntex for this--->
# var.replace(data_to_replace,method="ffill") for forward or method="bfill" for backword

# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# print(var.replace("SHOP-1",method="bfill"))






# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# print(var.replace(["SHOP-12","SHOP-1"],method="ffill"))










# note----> if we had the same type of cells filled with the same data but we want to replace some of cells 
# with forward or backward data, in this case we will use 
# var.replace(data_to_replace,method="ffill",limit=3)
# limit=any number(howmany cells you wants to replace)
# note_____> if we want to change the data in the original data we can pass the argument inplace=True
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")

# csv_1 =var.replace(["SHOP-12","SHOP-1"],method="ffill",inplace=True)
# print(csv_1)


# we can check inplace by access the original csv file
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")
# print(var)