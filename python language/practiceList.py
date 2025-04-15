# a = [1,3,5,6]
# b = [2,5,6,9,7]
# for i in range(len(a)):
#     a[i] = a[i]*12
# for i in range(len(b)):
#     b[i] = b[i]-1
# print(a)
# print(b)


# find the length of a list without using len() function
# list = [1,2,3,4,5,6,7,8,9]
# count = 0
# for i in list:
#     count +=1
# print(count)

# access the first and the last element of a list
# list = [1,2,3,4,5,6,7,8,9]
# print(list[0])
# print(list[-1])




# slice a list to get the first 3 elements
# list = [1,2,3,4,5,6,7,8,9]
# print(list[0:3])



# check if "apple" exists in teh list: fruits = ["apple", "banana", "cherry"]
# fruits = ["apple", "banana", "cherry","orange"]
# if str(input("search the fruit availability in list: ")) in fruits:
#     print("yes, the fruit is available in the list")
# else:
#     print("no, the fruit is not available in the list")



# reverse a list using slicing and using a loop
# list = [1,2,3,4,5,6,7,8,9]
# print(list[::-1])
# list = [1,2,3,4,5,6,7,8,9]
# list.reverse()
# print(list)
# list = [1,2,3,4,5,6,7,8,9]
# for i in range(len(list)-1,-1,-1):
#     print(list[i], end=" ")



# find teh maximum and minimum values in a list
# list = [11,12,111,13,20,25,26,27,28,29]
# print(max(list))
# print(min(list))

# find the maximum and minimum values in a list without using max() and min()
# list = [11,12,111,13,20,25,26,27,28,29]
# max = list[0]
# min = list[0]

# for i in list:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
    
# print("max value is: ",max)
# print("min value is: ",min)



# concatinate  two lists without using +.
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]
# list1.extend(list2)
# print(list1)

# concatinate two lists using for loop.
# for i in list2:
#     list1.append(i)

# print(list1)


# remove duplicates from a list.
# list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
# new_list = []
# for i in list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)



# remove duplicates from list method 2
# my_list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
# my_list = list(set(my_list))
# print(my_list)


# short a list in ascending and descending order without using short() method
# ascending order
# list = [1,2,3,4,5,9,7,8,6,]
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i] > list[j]:
#             list[i],list[j] = list[j],list[i]
# print(list)

# # descending order
# list = [1,2,3,4,5,9,7,8,6,]
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i] < list[j]:
#             list[i],list[j] = list[j],list[i]
# print(list)





# advance level
# find the second largest number in a list
# list1 = [21,11,13,24,33,21,55,43]
# re_list = list(set(list1))
# re_list.sort()
# print(re_list)
# print("second largest number is: ",re_list[-3])
# print("second smallest number is: ",re_list[1])



# count the occurrences of an element in a list.
# list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
# print(list.count(1))



# convert a list of numbers into asingle integer: [1,2,3,4] -> 1234.
# THIS QUESTION HAVE THREE TUPES TO DO THIS.
# list = [1,2,3,4]
# str1 = ""
# for i in list:
#     str1 += str(i)
# print(str1)
# print(int(str1))
# print(int("".join(map(str,list))))



# find the common elements in two lists.
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,4,6,8,10,12,14,16,18]
new_list = list(set(list1) & set(list2))
print(new_list)
