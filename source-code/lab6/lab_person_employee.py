from models.person import Person
from models.employee import Employee

p = Person("Aina", 20)
p.introduce()

e = Employee("Ali", 20, "E101", "IT")
e.introduce()
print(type(e)) # models.employee.Employee (Class name)

# I can override __str__ method to make it readable for debugging purpose
print(e) # Unreadable object information models.employee.Employee object at 0x104984200>

# Error validation test - we will learn about try catch in day 3/4
# e2 = Employee("James", -10, "E101", "IT")
# print(e2)

# Show the data as dict format / JSON (related to API)
print(e.to_dict())