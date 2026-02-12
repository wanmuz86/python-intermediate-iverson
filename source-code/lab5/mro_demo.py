from models.student import Student
from models.school import School

s = Student("Aina")
print(s.name)  # Aina
 # class variable
 # check if there is a class variable call name
 # Since it is not there, this is an inheritence
 # look at parent
 # Parent has it -> show "Anak2U"
print(Student.name) #Anak2U
print(School.name) # Anak2U 

#Remove the instance attribute

del s.name # REMOVING Aina
# Look for Aina's name as an instance varibable
# It is not there -> Look as a Class Variable
# It is not there -> Look at parent Class varianle
# Parent has it -> Return Anak2U
# Does arrangement matters when you do the (A,B,C)
# Yes , arrangement matters because Python will look based on Arrangement
# A -> B -> C
# Mixins should be on the left, on Parent class the rightest
print(s.name)

print(Student.__mro__)