# python can be used to perform oprations on a file. (read & write data)
# types of all files 
# 1> text files: .txt,.docx, .og etc. 
# 2> binary files: .mp4,.mov, .png, .jpeg etc.


# open, read, close file
# f = open ("file_name", "mode") 
# data= f.read()
# print(data)
# f.close()
# mode -> r: if we do not define the mode of the file the it by default open in read mode /// or w: to open with write mode we have to use this write mode

# f = open("python language\demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()d


# create a new file "practice.txt" using python. add the following data in it.
# hii everyon 
# we are lerning file i/o 
# using java. 
# I like programming in java.


# with open("practice.txt","w") as f:
#     f.write("hii everyone\n we are learning file i/o \n using java\n I like programming in java")




# write a programme that replace call occurences of "Java" with "Python" in above file.
# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("java","Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)



# write a function to search if the word "learning" exists in the file or not.
# def check_for_word():
#     word = "Python"
#     with open("practice.txt","r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("found")
#         else:
#             print("not found")
# check_for_word()


# write a programme to search if the word "learning" exists in the file or not.
# word = "Python"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")




# waf to find in which line of the file does the word "learning" occurs first. print-1 if word not found.
# def check_for_line():
#     word = "Python"
#     data = True
#     line_no =1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no +=1

#     return -1
# check_for_line()



# from a file containing numbers sepratedby comma, print the count of even numbers.
# count = 0 
# with open("python language\demo.txt","r") as f:
#     data = f.read()

#     nums = data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1
# print(count)