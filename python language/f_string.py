# Interview Q&A on f-strings
# Q1: What is an f-string in Python?
# Ans: An f-string (formatted string literal) is a way to embed variables and expressions inside a string using {}. It is prefixed with f and was introduced in Python 3.6.

# Q2: How does an f-string improve performance?
# Ans: f-strings are faster than .format() and % formatting because they are evaluated at runtime and avoid additional function calls.

# Q3: Can we use expressions inside f-strings?
# Ans: Yes, f-strings allow calculations and function calls directly inside {}.
# example:
# a = 10
# b = 20
# print(f'The sum of {a} and {b} is {a+b}')
