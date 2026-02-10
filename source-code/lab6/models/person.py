class Person:
    """Represents a person with a name and age."""

    def __init__(self, name, age):

        # Validation in constructor
        # if age is smaller than 0, throw an error
        if age <=0:
            raise ValueError("age must be positive")
        self.name = name
        self.age = age

    """This is method is used to present the name and age of the person"""
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")
