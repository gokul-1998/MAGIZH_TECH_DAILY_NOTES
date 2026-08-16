def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        
        result = func(*args, **kwargs)
        
        print(f"Finished {func.__name__}")
        
        return result
    
    return wrapper


@logger
def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b


@logger
def multiply(a, b):
    return a * b


print(add(10, 20))
print(multiply(5, 4))