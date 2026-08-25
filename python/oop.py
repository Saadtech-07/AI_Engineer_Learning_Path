# Class & Object 
# class Student:
#     def study(self):
#         print("Student is Styding")
# student1 = Student()
# student2 = Student()
# student1.study()
# student2.study()


# Self - self refers to the current object.
# Student.study(student1)


# __init__
# class User:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# user1 = User("Saad",22)
# user2 = User("Anzar",35)

# print(user1.name, user1.age)
# print(user2.name, user2.age)


# Class with attributes + methods
# class User:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print("The Name is:", self.name)
#         print("Age:", self.age)
# user1 = User("Saad",22)
# user1.introduce()            


# Practice
# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def action(self):
#         print("Brand:",self.brand)
#         print("Model:",self.model)
#         print("Year:", self.year)
# car1 = Car("BMW","Q3",2026)            
# car1.action()



# Inheritance
# Child → can access parent things
# Parent → cannot access child-specific things

# class Animal:
#     def eat(self):
#         print("Animal is Eating")
# class Dog(Animal):
#     def bark(self):
#         print("Dog is Barking")
# dog1 = Dog()
# dog1.eat()
# dog1.bark()                

# animal = Animal()
# animal.eat()  --> Parent just access his own things


# Inheritance with __init__()
# class Animal:
#     def __init__(self,name):
#         self.name = name
# class Dog(Animal):
#     def bark(self):
#         print(self.name,"is barking")
# dog = Dog("Rocky")
# dog.bark()                


# Super() --> When the child needs to use the parent's constructor:

# class Animal:
#     def __init__(self,name):
#         self.name = name
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed
# dog = Dog("Rocky","Labrador")
# print(dog.name)
# print(dog.breed) 



# ENCAPSULATION --> bundling data and methods together and controlling access to internal data.
# class Employee:
#     def __init__(self,salary):
#         self.__salary = salary
#     def get_salary(self):
#         return self.__salary

# employee = Employee(50000)
# print(employee.get_salary())    



# POLYMORPHISM --> Same interface/method name, different behavior.
# class Dog:
#     def sound(self):
#         print("Bark")
# class Cat:
#     def sound(self):
#         print("Meow")
# dog = Dog()
# cat = Cat()
# dog.sound()
# cat.sound()        

# sound() --> same sound, different behaviour

# Polymorphism with inheritance
# class Animal:
#     def sound(self):
#         print("Animal Sound")
# class Dog(Animal):
#     def sound(self):
#         print("bark")
# class Cat(Animal):
#     def sound(self):
#         print("Meow")

# animal = Animal()
# dog = Dog()
# cat = Cat()

# animal.sound()
# dog.sound()
# cat.sound()


