# The name of the class
# class Student:
#     # Defining the property of the class
#     # How we describe a class
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
    
#     #Defining the method of a class
#     def introduce(self):
#         # the keyword self refers to the attribute/property of the object
#         # eg: Ali
#         print(f"Hi, I am {self.name}")

from .person import Person
class Student(Person):
    def study(self):
        print(f"{self.name} is studying")