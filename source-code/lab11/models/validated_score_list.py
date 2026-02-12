
# This class will extend the Built-in list object in Python
# We are extending the list to create a list to score numbers
# between 0 to 100
# by adding validation in the list

class ValidatedScoreList(list):

    def _validate(self, score):
        if not isinstance(score, (int,float)):
            raise TypeError("Score must be a number")
        #related to the 1st test on Part 3 Test script
        if not 0 <= score <= 100:
            raise ValueError("score must be between 0 and 100")
        
    # Override built-in list append and extend 
    # append - add an item at the end of it
    # extend - add another list at then end of it
    def append(self, score):
        # VALIDATE FIRST before adding in List
        self._validate(score)
        super().append(score)
    
    def extend(self, scores):
        # go through all the item in list
        for s in scores:
            # validate first
            self._validate(s)
        #if all ok then only extend the list
        super().extend(scores)

    #Extra method
    def average(self)->float:
        return sum(self) / len(self) if len(self) > 0 else 0.0