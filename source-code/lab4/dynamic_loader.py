import importlib

# math module, will be lazy-load
# loaded only when it is used
module_name = "math"
math_module = importlib.import_module(module_name)

#it will only be loaded here
print(math_module.sqrt(49))
