# CSV FILES___>
# A simple way to store big data sets is to use csv files (comma seprated files).
# CSV files contains plain text and is a well know format that can be read by everyone including pandas.
# if the path not works we can try the double back slash in the path
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv")

# print(var)






# we can access the rows from the big data with the help of the nrows=number
# it will  give the data till teh number you have provided to it.
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv",nrows=50)

# print(var)






# we can also get the colum data with the help of the usecols=["header name"] or can give the index number of the columns
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv",usecols=["Unit No."])

# print(var)




# we can also get the colum data with the help of the usecols=["header name"] or can give the index number of the columns
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv",usecols=[0,1,2])

# print(var)







# we can skip any column or row of the data
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv",skiprows=[1,2])

# print(var)






# we can make any column  as a index
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv",index_col=["Registration No."])

# print(var)




# we can make any row as a header withthe header= index
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv",header=3)

# print(var)





# we can also give the name to our header row but if the data is having already the header row in the data, this will add the new header at the top of the rows as a header 
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv",names=["col1","col12","col13","col14","col15","col16"])

# print(var)





# but when we want that my remove my old header from the data and add the new header at teh place of that
# we have to use the argument header= None, prifix= [names of the header]

# it's showing error for prefix 
# import pandas as pd
# var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv",header=None,prefix="col")

# print(var)





# we can chenge the data type of the data with the help of the dtype=
import pandas as pd
var = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\python & lybrary\\Book1.csv",dtype={"Unit No.":str,"Registration No.":"float","Name":str,"Address":str,"Phone No.":str,"Email":str})

print(var)
