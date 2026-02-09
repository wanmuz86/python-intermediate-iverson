def greet(name):
    return f"Hello, {name}!"

# This is the main of my module
# By adding this part, the module is executed if calling it directly

# Why is __name__ == "__main__" critical for reusable modules?
# It allows a module to be reusable:
# 1) To be called from another module or script file
# 2) Can work as standalone module
# Create unwanted side effect -> behaviourr
def main():
    print(greet("Direct User"))

if __name__ == "__main__":
    main()
