# oops in python> to map with real world scenarios, we started using objects in code.
# # this is called object oriented programming.


# example of the class
# class car:
#     color = "blue"

# car1 = car()
# print(car1.color)

# constructor> __init__finction
# constructor
# all classes have a function called __init__(), which is always execute when the object is being initiated

# creating class
#     class student:
#         def __init__(self, fullnaname):
#             self.name = fullnaname
        

# creating object
# s1 = student("karan")
# print(s1.name)



# the self parameter is a refrence to the current instance of the class, 
# and is used to access variables that belongs to the class.


# class Student:

#     def __init__(self, name, marks,age):
#         self.name = name
#         self.marks = marks
#         self.age = age
#         print("adding a new student in database...")

# s1 = Student("karan", 98, 19)
# print(s1.name, s1.marks, s1.age)

# s2 = Student("arjun", 88, 20)
# print(s2.name, s2.marks,s2.age)

# s3 = Student("sachin", 99, 23)
# print(s3.name, s3.marks, s3.age)




# methods
# creating class
# class Student:
#     def __init__(self, fullname):
#         self.name = fullname

# def hello(self):
#     print("hello", self.name)

# # creating objects
# s1 = Student("karan")
# s1.hello()




# example
# class Student:
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome student")

#     def get_marks(self):
#         return self.marks

# s1 = Student("karan", 97)
# s1.welcome()
# print(s1.get_marks())



# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hii", self.name,"your avg score is :", sum/3)
# s1 = Student("sachin", [99,98,78])
# s1.get_avg()

# # we can change the name and attributes like this 
# s1.name = "chaudhary"
# s1.get_avg()


# static method
# methods that don't use self parameter(work at class level)

# class Student:
#     @staticmethod   #decorator
#     def college():
#         print("abc college")

# decoprator allow us to wrap another function in order to 
# extend the behaviour of the wrapped function, without permanently modifing it.


# oops>
# >abstraction
# >encapsulation
# >inheritance
# >polymorphism

# Abstraction>
# hiding the implementation details of a class and only showing 
# the essential features to the user.


# encapsulation>
# wrapping data and functions into a single unit(*objects).


# practice question
# create account class with 2 attribute- balance & account no. 
# create methods for debit, credit & printing the balance.


class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # Debit method
    def debit(self, amount):
        if amount > self.balance:
            print("\nError: Insufficient balance! You do not have enough funds to complete this transaction.")
            self.show_options()
        else:
            self.balance -= amount
            print(f"Rs. {amount} was debited successfully.")

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was credited successfully.")

    # Method to get balance
    def get_balance(self):
        return self.balance

    # Show options when insufficient balance error occurs
    def show_options(self):
        while True:
            print("\nOptions:")
            print("1. Check Balance")
            print("2. Try Again To Debit")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                print("Your current balance is Rs.", self.get_balance())
            elif choice == "2":
                amount = int(input("Enter the amount to debit: "))
                self.debit(amount)
                break  # Exit loop if transaction is successful
            elif choice == "3":
                print("Thank you for using our service.")
                break
            else:
                print("Invalid choice! Please select a valid option.")

# Creating account instance
acc1 = Account(10000, 451543)
print("Welcome! Your account number is:", acc1.account_no)

# Handling transactions
acc1.debit(int(input("\nEnter the amount to debit: ")))
acc1.credit(int(input("\nEnter the amount to credit: ")))

# Final balance check option
if input("\nDo you want to check your final balance? (yes/no): ").lower() == "yes":
    print("Your final balance is Rs.", acc1.get_balance())
