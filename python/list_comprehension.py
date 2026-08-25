#Normal
# num = [10,20,30,40,50]
# square = []
# for x in num:
#     square.append(x ** 2)
# print(square) 


#List Comprehension
# num = [11,20,33,40,53]
# square = [x ** 2 for x in num]
# print(square) 

# In Condition
# square = [x for x in num if x % 2 == 0]
# print(square)

# Dictonary Comprehension

# num = [10,20,30,40,50]
# square = {x: x ** 2 for x in num}
# print(square)


# num = [11,20,33,40,53]
# square = {x: x ** 2 for x in num if x % 2 == 0}
# print(square)



# Normal
# def cube(x):
#     return x ** 3
# print(cube(3))    


# Lambda
# square = lambda x: x ** 2
# print(square(5))

# add = lambda a, b: a + b
# print(add(3,4))


# Map
# numbers = [1, 2, 3, 4]
# result = map(lambda x: x * 3, numbers)
# print(list(result))

#Filter
# num = [1,2,3,4,5]
# fil = filter(lambda x: x % 2 == 0, num)
# print(list(fil))

# Zip
# names = ["saad","madhan","dhayal"]
# age = [22,23,24]
# result = zip(names,age)
# print(list(result))


# Enumerate()
# names = ["saad","madhan","dhayal"]
# for index, name in enumerate(names):
#     print(index, name)

# for index, name in enumerate(names, start = 1):
#     print(index, name)


# Unpacking
# person = ("Saad", 22, "Developer")
# name, age, role = person
# print(name, age, role)

# numbers = [1, 2, 3, 4, 5]
# first, *middle, last = numbers
# print(first, middle, last)

numbers = [10, 20, 30]

def add(a, b, c):
    return a + b + c

print(add(*numbers))