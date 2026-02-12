from decorators.log_decorator import log_call

class Calculator:
    # Intercept the add method
    @log_call
    def add(self, a, b):
        return a + b

    # Intercept the multiply method
    @log_call
    def multiply(self, a, b):
        return a * b
