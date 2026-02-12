from .validated_score_list import ValidatedScoreList
class StudentRecord:

    # Class property to store how many students have been created
    # Define outside on init, initializer
    _count = 0

    #Initializer

    def __init__(self,name, age, scores=None):
        self.name = name
        self.age = age
        # Composition (has-a)
        self.scores = ValidatedScoreList(scores or [])
        # Changing/Mutating the class propery
        StudentRecord._count +=1

    # Add getter and setter
    # @property -> getter
    # @property.setter -> setter

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # We add validation before setting the property name of Student
        if not isinstance(value, str) or not value.strip() or len(value) < 3:
            raise ValueError("name must be a non-empty string or canot be less than 3")
        self._name = value.strip()
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        # Type and Positive Validation on the age
        if not isinstance(value, int):
            raise TypeError("age must be an integer")
        if value <= 0:
            raise ValueError("age must be positive")
        self._age = value
    
    def add_score(self,score):
        self.scores.append(score)

    # CLASS METHOD which is a getter to retrieve the current counter
    @classmethod
    def instance_count(cls):
        return cls._count
    
    def __repr__(self):
        return (
            f"StudentRecord(name='{self.name}', age={self.age}, "
            f"scores={list(self.scores)}, avg={self.scores.average():.2f})"
        )
