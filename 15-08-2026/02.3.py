def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        
        func()
        
        print("After the function runs")
    
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()

# A decorator in Python is a function that modifies or extends the behavior of another function without changing its original code.