from models.score_list import ScoreList
from models.student_scores import StudentScores
scores = ScoreList([80,90,85])

scores.add(70)

print("Length: ", len(scores)) #4   __len__
print("Index 1 ", scores[1]) #90 __getitem__
print("Slice 0:2", scores[0:2]) # [80,90] __getitem__

print("Iterate")
for s in scores:   # __iter__
    print("-",s)

print("Student scores part")

s1 = StudentScores("Aina", [90, 85, 95])
s2 = StudentScores("Ali", [70, 75, 80])
s3 = StudentScores("Mira", [90, 85, 95])

print("Aina avg:", s1.average()) # custom method created by us
print("Ali avg:", s2.average())

print("Equality check (Aina == Mira):", s1 == s3)  # True - __eq__
print("Less-than check (Ali < Aina):", s2 < s1)    # True.  __lt___

students = [s1, s2, s3]  
print("Sorted students:", sorted(students)) # __lt__

print("\nTop scores:")
print("Top 1:", scores.top(1))
print("Top 2:", scores.top(2))
