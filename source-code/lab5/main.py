# Creating a student with dictionary

student = {
    "name":"Aina",
    "age":6,
     # lamda - create a function without specifying the name
    "introduce": lambda:print("Hi, I am Aina")
}
# () -> Execute the function
student["introduce"]()
print("Student name: ",student["name"])

student2 = {
    "name":"Ali",
    "age":7,
    "introduce":lambda:print("Hi, I'm Ali")
}
student2["introduce"]()
print("Student name: ", student2["name"])


# from models.student import Student

# # Creating an instance of Student

# s1 = Student("Aina", 6) # Aina is a student
# s2 = Student("Ali",7) # Ali is a student

# print("OOP example")

# s1.introduce()
# s2.introduce()

# print(f"{s1.name} is {s1.age} years old")

from models.teacher import Teacher
from models.student import Student

# Creating an instance
student = Student("Aina")
teacher = Teacher("Mr Adam")

student.introduce() # My name is Aina. # come from Person
student.study() # Aina is studying # Belong to Student

teacher.introduce() # My name is Mr Adam # come from Person
teacher.teach() # Mr Adam is teaching  # Belong to Student