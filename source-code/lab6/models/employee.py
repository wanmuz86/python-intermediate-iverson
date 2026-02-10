from .person import Person

class Employee(Person):
    """Reperesents an employee who is a person"""

    # In addition to name and age, it will have employee_id and department
    # Extending the parent properties
    
    def __init__(self, name, age, employee_id, department):
        # Calling the constructor from parent (super())
        super().__init__(name, age)
        
        # Intializing the additional properties
        self.employee_id = employee_id
        self.department = department
    
    def __str__(self):
        return f"Employee(name='{self.name}', department='{self.department}', employee_id='{self.employee_id}', age='{self.age}')"

    #Override the introduce method to include the department ID
    def introduce(self):
        print(
            f"Hi, I'm {self.name} ID: {self.employee_id} from department {self.department}, "
            f"and I am {self.age} years old"
        )

    # To transform an object in a Dictionary format
    # We normally use it when building an API server (Day 5)
    def to_dict(self):
        return {
            "name":self.name,
            "age":self.age,
            "employee_id":self.employee_id,
            "department":self.department
        }