from models.validated_score_list import ValidatedScoreList
from models.student_record import StudentRecord

print("\n--- Part 1: ValidatedScoreList ---")
scores = ValidatedScoreList([80, 90])
scores.append(70)
scores.extend([85, 95])

print("Scores:", scores)
print("Average:", scores.average())

print("\n--- Part 2: StudentRecord + Properties ---")
s1 = StudentRecord("Aina", 7, [80, 90])
s2 = StudentRecord("Ali", 8, [70, 75, 85])
s3 = StudentRecord("Mira", 7)

s3.add_score(88)
s3.add_score(92)

print("S1:", s1)
print("S2:", s2)
print("S3:", s3)

print("\n--- Part 3: Validation Tests ---")

try:
    s1.add_score(150)
except ValueError as e:
    print("Score error:", e)

try:
    s2.age = -1
except ValueError as e:
    print("Age error:", e)

try:
    s3.name = ""
except ValueError as e:
    print("Name error:", e)

print("\n--- Instance Count ---")
# all the instance of object share the same class variable
# here we have 3 because we have 3 instance
# if we add more then the class variable will be incremented

#How do you call a class method
# We call the class method from the CLASS not INSTANCE
# example of instance is s1,s2,s3
# example of class : StudentRecord, ValidateScoreList
print("Total StudentRecord instances:", StudentRecord.instance_count())
