# Normal - single argument can be passed
# def sum(num):
#     return num
# print(sum(10))    

# args - multiple argument can be passed
# def add(*args):
#     return args
# print(add(10,20,30,40))    

# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# print(add(10,20,30))
# print(add(1,2,3))
# print(add(7,7,7))    


# keyword arguments
# def user(**kwargs):
#     print(kwargs)
# user(name= "Saad",age = 22, role = "Developer")    


# Key, value type keyword arguments
# def user(**kwargs):
#     for key, value in kwargs.items():
#         print(key, "=", value)
# user(name = "Saad", age = 22, role = "developer")


# def both(*args, **kwargs):
#     print("Agruments", args)
#     print("K Arguments", kwargs)
# both(10,20,30, name = "Saad", age = 22)    


# unpacking with multiple argument
# def add(a, b, c):
#     return a + b + c
# numbers = [10, 20, 30]
# print(add(*numbers))

# unpacking with dict

def introduce(name, age):
    print(name, age)
user = {
    "name": "Saad",
    "age": 22
}    
introduce(**user)