# def greet():
#     print("Hello")
# greet()    


# def greet():
#     print("hello")
# say_hi = greet
# say_hi()    

# Function as an argument

# def greet():
#     print("Hello")
# def execute(function):
#     function()    
# execute(greet)    


# def cube(x):
#     return x ** 3
# def calculate(function,number):
#     return function(number)
# res = calculate(cube, 5)        
# print(res)


# def outer():

#     def inner():
#         print("Hello")
#     return inner()    
# res = outer()
# res()    