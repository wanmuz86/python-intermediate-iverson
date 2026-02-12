class GoodCounter:
    """
    Correct use of instance-specific attributes.
    """

    # Creating as an instance property not class property
    def __init__(self):
        self.history = []  # ✅ unique per instance

    def add(self, value):
        self.history.append(value)
