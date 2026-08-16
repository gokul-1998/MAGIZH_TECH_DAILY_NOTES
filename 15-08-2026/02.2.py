def fun(x):
    def square(x):
        return x * x
    return square

print(fun(5))  # Output: 25
# print(square(5))  # This would cause a NameError since square is not accessible in this scope