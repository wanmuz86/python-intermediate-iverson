def log_call(func):
    def wrapper(*args, **kwargs):
        
        #INTERCEPT BEFORE THE METHOD CALL
        print(f"[LOG] Calling {func.__name__}")
        
        #METHOD CALL
        #*args, **kwargs -> Argument of the method
        # this line means execute the function without modifying the arguments
        result = func(*args, **kwargs)

        #INTERCEPT AFTER THE METHOD CALL
        print(f"[LOG] FINISHING {func.__name__}")
        
        return result
    
    return wrapper