# part 1 & part 2
# import utils


# print("Add: ", utils.add(2,3))
# print("Multiply: ", utils.multiply(4,5))

# #part 2
# # variable of the same name to demonstrate isolation
# value = 20
# utils.show_value()

# #example with getting the variable directly with . notation
# print("utils value ", utils.value)
# print("main value: ", value)


# from utils import add, multiply, substract
from utils import *

print("Add : ", add(5,6))
print("Multiply: ", multiply(3,4))

print("Substract:", substract(10,3))

# import utils
# print(utils.add(5, 6))

import utils
# Return the module name
print(utils.__name__)
# Return the module metadata including ...
print(utils.__dict__)