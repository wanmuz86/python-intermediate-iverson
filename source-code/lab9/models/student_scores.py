from .score_list import ScoreList

# Class that has two properties
# Student name
# and their scores for exam/test using ScoreList (Special List)
class StudentScores:
    # constructor accept name , scores (ScoreList)

    def __init__(self, name, scores):
        self.name = name
        self.scores = ScoreList(scores)

    # Average method, that will return the average of scores in the list
    def average(self):
        # If it is empty , average is 0
        if len(self.scores) == 0:
            return 0.0
        # sum -> built-in list method that will sum up all values in the list
        # len -> length of the list
        return sum(self.scores) / len(self.scores)

    #Comparison method
    # self, and other (compared to who)
    def __eq__(self, other):
        # to verify both need to be an instanceof StudentScores class
        if not isinstance(other, StudentScores):
            return NotImplemented
        # compare the average if it is the same or not
        return self.average() == other.average()

     #Comparison method for <
    # self, and other (compared to who)
    def __lt__(self, other):
         # to verify the others need to be an instanceof StudentScores class
        if not isinstance(other, StudentScores):
            return NotImplemented
        # return true if i am < other (average)
        return self.average() < other.average()

    # To be called with repr (developer friendly log)
    # You can implement __str__ as well
    def __repr__(self):
        #.2f means two decimal point
        return f"StudentScores(name='{self.name}', avg={self.average():.2f})"
    
    

