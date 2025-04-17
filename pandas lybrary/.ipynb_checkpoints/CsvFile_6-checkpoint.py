# DIFFRENCES between CSV and XLS(EXCEL) file formats:
# >CSV format is a plain text format in which values are seprated by commas(Comma seprated values).
# >XLS file format is an excel sheets binary file format which holds information about all the worksheets in a file,
# including both content and formatting.




# to create the csv file we will use the var.to_csv("file_name")
# if you want to remove the indexes from teh fle you can use the function argument

# import pandas as pd
# dis = pd.DataFrame({"a":[12,13,14,15,16,17,18,19,20],"b":[12,13,14,15,16,17,18,19,20],"c":[12,13,14,15,16,17,18,19,20]})

# dis.to_csv("demo_file.csv")
# print(dis)




# var.to_csv("file_name",index= False)
import pandas as pd
dis = pd.DataFrame({"a":[12,13,14,15,16,17,18,19,20],"b":[12,13,14,15,16,17,18,19,20],"c":[12,13,14,15,16,17,18,19,20]})

dis.to_csv("demo_Remove_Index.csv",index=False)
print(dis)





# we can also edit the header of the data(keys of the dictonary)
# with the header argument
# this will diractly update in your existing file
# import pandas as pd
# dis = pd.DataFrame({"a":[12,13,14,15,16,17,18,19,20],"b":[12,13,14,15,16,17,18,19,20],"c":[12,13,14,15,16,17,18,19,20]})

# dis.to_csv("demo_Remove_Index.csv",index=False,header=["col1","col2","col3"])
# print(dis)

