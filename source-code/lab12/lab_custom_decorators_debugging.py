from decorators.log_decorator import log_call
from models.calculator import Calculator

@log_call
def greet(name):
    print(f"Hello, {name}!")

def test_function_decorator():
    print("\n -- Function Decorator Test --")
    greet("Aina") 
    # Decorator will change function, method, class behaviour
    #Observe that before and after the method call, you can see the log

test_function_decorator()

def test_method_decorator():
    print("\n--- Method Decorator Test ---")
    calc = Calculator()
    print("Add:", calc.add(2, 3))
    print("Multiply:", calc.multiply(4, 5))

test_method_decorator()
