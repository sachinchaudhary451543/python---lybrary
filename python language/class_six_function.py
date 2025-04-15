#formula;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# def func_name(parameter1 , parameter2):    #funtion definition
#     #some work
#     return Val

# func_name(argument1, argument2) #to function call





# examples !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def cal_sum(a,b):   #parameters
#     return a + b
# sum = cal_sum(2,3)        #argument
# print(sum)


# def print_hello():
#     print("hello")

# print_hello()
# print_hello()
# print_hello()
# print_hello()

# answer is =
# hello
# hello
# hello
# hello



# example 3 avrage function 
# def cal_avg(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg
# cal_avg (3, 4, 5)




# types of the functions :=================
#1) built n function => 
# print()
# len()
# type()
# range()


# 2) user define functions

# default parameters
# def cal_prod(a=1,b=1):
#     print(a*b)
#     return a*b
# cal_prod()


# practice questios------------------------
# 1> wap to print the length of a list.(list is the parameter)

# cities = ["noida","delhi","pune","haryana"]
# heroes = ["thor", "ironman","captain america","shaktiman"]
# def print_len(list):
#     print(len(list))
#     return len(list)
# print_len(cities)
# print_len(heroes)

# 2> wap to print the element of the list in a single line.(list is the parameter)
# heroes = ["thor", "ironman", "captain america", "shaktiman"]
# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(heroes)

# 3> wap to find the factorial of n. (n is the parameter)
# i>
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact) 


# ii>
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact) 

# cal_fact(6)




# 4> wap to convert USD TO INR.
# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD=", inr_val,"INR=")

# converter(2)    



# 5> wap to input a number and check if it is odd or even 
# def check(n):
#     if n % 2 == 0:
#         print("odd")
#     else:
#         print("even")

# check(int(input("enter the number=")))




# recursion------------------------------------------------------------------
# when a function cals itselfrepeatedly
# as> print n to 1 backwords

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n - 1)
# show(5)


# return n!
# def fact (n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n - 1)
    
# print(fact(5))



# write a recursive function to calculate the sum of first n natural numbers.........
# def cal_sum(n):
#     if(n == 0):
#         return 0
#     return cal_sum(n-1) + n
   
# sum = cal_sum(5)
# print(sum)


# write a recursive function to print all element in a list . hint: use list & index as parameters.
# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# fruits = ["mango", "orange","grapes","apple","banana"]

# print_list(fruits)
