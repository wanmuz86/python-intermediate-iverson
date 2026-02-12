# REMEMBER Mixin normally is not initialized 
# -> Dont have  constructors
# REMEMBER  We don't store state (homework wht is this?) in Mixin
# -> Don't have properties

class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")