class DisplayMixin:
    def display(self):
        attrs = vars(self) 
        # inspection method (to get the attributes)
        # get the class name as well 
        return f"{self.__class__.__name__}({attrs})"
