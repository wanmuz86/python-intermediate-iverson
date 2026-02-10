from .person import Person

# (Person) means Teacher inherits person
class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching")