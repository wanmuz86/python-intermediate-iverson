class BadCounter:
    """
    Demonstrates unintended shared state via a class attribute.
    """
    #BY DOING THIS, WE UNINTENDED CREATE A CLASS VARIABLE PROPERTY OF INSTANCE PROPERTY
    history = []  # ❌ shared mutable state across all instances

    def add(self, value):
        self.history.append(value)
