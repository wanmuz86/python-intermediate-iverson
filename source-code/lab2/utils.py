def add(a,b):
    return a+b + 100

def multiply(a,b):
    return a*b

# to demonstrate isolation of variable/property
# in module

value = 10
def show_value():
    print("utils value: ", value)

def substract(a,b):
    return a-b