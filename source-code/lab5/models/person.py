# THis is the base class / parent class to define a Person
# We will have Teacher and Student class
# That will inherits the base class

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")