#Local Scope

# def local():
#     message = "hello"
#     print(message)
# local()    

#Global Scope

# name = "Global"
# def greek():
#     print(name)
# greek()    

#Local scope have priority over global scope

# name = "Global"
# def scope():
#     name = "local"
#     print(name)
# scope()    

#Enclosing Scope

# def outer():
#     name = "Saad"
#     def inner():
#         print(name)
#     inner()
# outer()        

#Practice 1

# x = 100
# def test():
#     x = 200
#     print(x)
# test()
# print(x) 


#Practice 2

# x = "A"
# def outer():
#     x = "B"
#     def inner():
#         print(x)
#     inner()
# outer()


