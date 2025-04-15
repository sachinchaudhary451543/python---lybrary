# dictionary is used to store data value in key:value pairs they are unordered, mutable(changeable) & don't allow duplicate keys.
# # as   "key" : value
# dict = {
# "name" : "sachin",
# "cgpa" : 9.6,
# "marks": [98,97,95],
# }
# print(dict)
# result is ={'name': 'sachin', 'cgpa': 9.6, 'marks': [98, 97, 95]}
# dict["name"],dict["cgpa"],dict["marks"]

# dict["key"]="value"        to ad values or row
# ---------------------------------------------------------nested dict-------------------------------
# nested dictionary

# student = {
#     "name" : "rahul",

#     "subjects" : {
#         "phy" : 98,
#         "chem": 78,
#         "maths":60

#     }
# }

# # print(student)
# print(student["subjects"])
# result is = {'phy': 98, 'chem': 78, 'maths': 60}

# -----------------------------------------------------set-----------------------------------------------

# set in py= set is the collection of the unordered items. each element in the set must be unique & set elements immutable or set mutable.
# nums= {1,2,3,4 ,5}
# set2 ={ 1,2,3,2,2,2}
# repeated element stored only once, so it resolved to [1,2,3] 
# null_set = set() empty set syntex


# ----------------------------------------------------------methods----------------------------
# sets methods

# set.add(element)  add an element
# set.remove(element) remove an element
# set.clear() empties the set
# set.pop() remove a random Value

# ---------------------------------------------------------empty--------------------------



# example add in empty set
# collection=set()
# collection.add(1)
# collection.add("ram")
# print(collection)

# result is = {'ram', 1}




# ------------------------------------------------------add----------------------------------


# example  2 add
# set={1,2,4,5}
# set.add(3) #we can't add any list but we can add toples in this
# set.add("ram")
# print(set)
# result is ={1, 2, 3, 4, 5, 'ram'}

# ------------------------------------------------------------remove-----------------------


# example remove

# student={"ram","syam","ramesh",2,4,5}
# student.remove(2)
# print(student)
# result is ={'ramesh', 'syam', 5, 4, 'ram'}



# ---------------------------------------------------------------------------clear----------------

# example 3 clear we can also print length of any set in any methods
# student={"ram","syam","ramesh",2,4,5}
# student.clear()
# print(len(student))  
# result=0


# -----------------------------------------------------------pop-------------------------------------------

# example 4 pop it;s used to print random value of any set 
# student={"ram","syam","ramesh"     if we include integers in this set then print pop this will start from integer value}
# student.pop()
# print(student)
# result is syam (we can use this method multiple times)


# ------------------------------------------------------------------------------------------------------------

# set.union(set2) combines both the set values & returns new

# # example union set this will also take any value at once no duplicate value will be print in union
# set1={1,2,3,4,}
# set2={2,3,4,5,6}

# print(set1.union(set2))

# result is ={1, 2, 3, 4, 5, 6}


# -------------------------------------------------------------------------------------------------------------

# set.intersection(set2)  combines common values and returns new combined values

# set1={1,2,3,4,}
# set2={2,3,4,5,6}

# print(set1.intersection(set2))

# result is ={2, 3, 4}

# -------------------------------practice questions--------------------------------------------------------------
# 1> store following word meanings in python dictionary; 
# table:"a piece of furniture", "list of facts & figures" 
# cat: "a small animal"

# things={
#     "table": {"a piece of furniture","list of facts & figures"},
#     "cat":"a small animal"
# }

# print(things)
# result is ={'table': {'a piece of furniture', 'list of facts & figures'}, 'cat': 'a small animal'}


# 2>  you are given a list of subjects for students. assume one classrom is required for 1 subject. how many classrooms are needed by all students.  
# "python", "java", "c++", "javascript","java","python", "java", "c++", "c"

# class={ "python", "java", "c++", "javascript","java","python", "java", "c++", "c"}

# print(len(class)) 
# result is =5



# 3>   wap to enter marks of 3 subjects from the users and store them in a dictionary. start with an empty dictionary & add one by one. Use subject name as keys and marks as value.
# 1st method
# dictionary={
#     "subjects":{
#         "sub1":input("enter your sub.1 marks:"),
#         "sub2":input("enter your sub.2 marks:"),
#         "sub3":input("enter your sub.3 marks:")
#     }
# }

# print(dictionary)
# result is=enter your sub.1 marks:99
# enter your sub.2 marks:95
# enter your sub.3 marks:98
# {'subjects': {'sub1': '99', 'sub2': '95', 'sub3': '98'}}
# -----------------------------2nd method---------------

# actual way to solve this question
# marks={}

# x=int(input("enter physics:"))
# marks.update({"physics":x})

# x=int(input("enter english:"))
# marks.update({"english":x})

# x=int(input("enter maths:"))
# marks.update({"maths":x})

# print(marks)

# answer=enter physics:98 
# enter english:99
# enter maths:100
# {'physics': 98, 'english': 99, 'maths': 100}



# 4>   figure out a waay to store 9 & 9.0 as seprate values in the set. (you can take help of built-in dATa types)

# set={1,3,9,9.0,9.5,8,8.0}
# print(set)
# soution is {1, 3, 8, 9, 9.5}

#  so in this case we have to make string a value to print 

# set={1,3,9,"9.0",9.5,8,"8.0"}
# print(set)
#  now the actual answer is ={1, 3, '8.0', '9.0', 8, 9.5, 9}

# second way to this

# set={
#     ("float",9.0),
#     ("int",9)
# }

# print(set)

# answer is={('int', 9), ('float', 9.0)}
