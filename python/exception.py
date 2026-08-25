# number = 10
# result = number / 0  --> ZeroDivisionError


# numbers = [10, 20, 30]
# print(numbers[0])   --> IndexError


# Try/except
# try:
#     number = 10 / 0
# except:
#     print("Something went wrong")

# Prefer catching the specific error
# try:
#     number = 10 / 0

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# Multiple exceptions
# try:
#     number = int(input("Enter number:"))
#     result = 10 / number 
# except ValueError:
#     print("please enter a valid number")    
# except ZeroDivisionError:
#     print("Number can't be zero")    
# else:
#     print("Valid Number")
# finally:
#     print("Run as default")    


# Getting an Error
# try:
#     number = int("hello")
# except ValueError as error:
#     print("Error:", error)


# Raising your own exception
# age = 15
# if age < 18:
#     raise ValueError("Age must be 18 or above")


