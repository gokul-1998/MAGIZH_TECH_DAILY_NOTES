# reverse the integer

x=1234

# solution

# print(x[::-1]) # TypeError: 'int' object is not subscriptable
# [::-1] -> slicing ( or string slicing)

# x="1234" # TypeError: 'int' object is not iterable
x=1234 # TypeError: 'int' object is not iterable
for i in x:
    print(i)
