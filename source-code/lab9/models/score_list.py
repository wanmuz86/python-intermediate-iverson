# Creating a special List to store students score 
class ScoreList: 
    # The constructor will either take [90,80,70] or nothing
    def __init__(self, scores=None):
        self._scores = list(scores or [])

    # Add a method add to an an item at the end of it
    # I don't want to use append
    def add(self, score):
        self._scores.append(score)

    # Override len()
    def __len__(self):
        return len(self._scores)
    
    #Override []
    def __getitem__(self,index):
        return self._scores[index]
    
    def __iter__(self):
        return iter(self._scores)
    
    # It will return the top n scores
    def top(self, n=1):
        if n <= 0:
            raise ValueError("n must be positive")
        # sort the array scores, by reverse
        # [80,70,90,60, 100] => [100,90,80,70,60] -> Sort by reverse
        # After sort i slice it [100,90,80,70,60][0:n]
        # eg, if n = 3  - [100,90,80,70,60][0:3] -> [100,90,80]
        return sorted(self._scores, reverse=True)[:n]