# while loop



# questions
# ****************************************************************************************
# 1 print numbers 1 to 100

# i=1
# while i<=100:
#     print("GoodMorning",i)
#     i+=1
# *****************************************************************************************
# 2 print numbers from 100 to 1 in reverse
# i=100
# while i>=1:
#     print("GoodMorning",i)
#     i-=1
#-----------------------------------------------------------------------------------------
# 2 print multiplication table of a num n

# n=int(input("enter your table:"))
# i=1  #initialisation
# while i<=10:
#     print(i*n)
#     i+=1

# ***************************************************************************************
# 3 print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]
# nums= [1,4,9,16,25,36,49,64,81,100]

# i = 0
# while i < len(nums):
#     print(nums[i])
#     i+=1

# 4 search for a number x in this tuple using loop:(1,4,9,16,25,36,49,64,81,100)

# nums=(1,4,9,16,25,36,49,64,81,100)

# x=int(input("enter number:"))

# i=0
# while i < len(nums):
#     if (nums [i] == x):
#         print("foun at idx:",i)
#     else: 
#         print("founding...")
#     i += 1
#result # enter number:36
# founding...
# founding...
# founding...
# founding...
# founding...
# foun at idx: 5
# founding...
# founding...
# founding...
# founding...

# ****************************************************************************
# # break loop
# nums=(1,4,9,16,25,36,49,64,81,100)

# x=int(input("enter number:"))

# i=0
# while i < len(nums):
#     if (nums [i] == x):
#         print("foun at idx:",i)
#         break
#     else: 
#         print("founding...")
#     i += 1


# result--    enter number:36
# founding...
# founding...
# founding...
# founding...
# founding...
# foun at idx: 5



# ********************************continue loop*****************************

# i =0

# while i <=5:
#     if(i == 3):
#         i+=1
#         continue #means skip any think
#     print(i)
#     i+=1
# # result 0
# 1
# 2
# 4
# 5

#  even numbers by continue

# i = 1
# while i <= 10:
#     if(i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

#     result
#     1
# 3
# 5
# 7
# 9

# ****************************************************************************************
#  for loop
# formula for for loop

# list1 = [1,2,3,4,5,6,7,8,9,10]
# for i in list1:
#     print(i)

# result
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# for loop with else
# list1 = [1,2,3,4,5,6,7,8,9,10]

# for el in list1:
#     print(el)
# else:
#     print("end of list")

# result
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# end of list

# examples of for loop/ for loop with else

#  question 1
# print element of list1 = [1,4,9,16,25,36,49,64,81,100] using for loop

# list1 = [1,4,9,16,25,36,49,64,81,100]
# for el in list1:
#     print(el)



# question 2
# search for a number x in this tuple using loop:(1,4,9,16,25,36,49,64,81,100) it's called leinear search in programing laguage

# nums=(1,4,9,16,25,36,49,64,81,100)

# for el in nums:
#     if el ==36:
#         print("found")
#         break

# result
# found

# method 2 for this question
# nums=(1,4,9,16,25,36,49,64,81,100)
# x = 36
# idx = 0

# for el in nums:
#     if el == x:
#         print("found", idx)
#     idx += 1

# result
# found 5

# **********************************************************range()******************************

# range functions returns a sequence of numbers, starting from 0 by default, and increaments by 1(by default), and stops before a specified numbers.
# range(start?, stop,step?)
# as--->  
# method 1 of range writing
# for el in range(5):
#     print(el)

# method 2 of range wtiting
# for el in range(1, 5):
#     print(el)

# method 3 of range writing
# for el in range(1,5,2):
#     print(el)

            
# example- print even numbers till 20
# for even in range (2, 20, 2):
#     print(even) 

# solution-
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18


# print numbers from 1 to 100*************
# for i in range (1, 101):
#     print(i)


# print numbers from 100 to 1**********
# for i in range(100, 0, -1):
#     print(i)

#  printthe multiplication table of a number n***********

# n= int(input("enter the number to get the multiplication:"))

# for i in range(1,11):
#     print(n*i)

# solution---
# enter the number to get the multiplication:11
# 11
# 22
# 33
# 44
# 55
# 66
# 77
# 88
# 99
# 110




# ***************************pass statement*******************
# pass is a null statement that does nothing. it is used as a placeholder for future code.
# formula---
# for  el in range(10):
    #    pass


# questions  ------------
# write a program to find the sum of first n numbers. (using while)
# n = 5
# sum = 0

# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print(sum)

# answer is 15


# second method for ths question--------

# n = 5

# sum = 0

# for i in range (1, n+1):
#     sum += i


# print("total of the numbers=", sum)

# answer is -total of the numbers= 15

# --------------------------wap to find factorial of first n numbers. (using for )
# method one
# n = 5
# fact = 1

# for i in range (1,n+1):
#     fact *= i

# print(fact)

# answer is ---> 120
# second method
# n = 5
# fact = 1
# i = 1

# while i <= n:
#     fact *= i
#     i += 1

# print("factorial is =",fact)


# answer ->factorial is = 120





import math

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Compute GCD
gcd = math.gcd(a, b)

print(f"The GCD of {a} and {b} is {gcd}")
