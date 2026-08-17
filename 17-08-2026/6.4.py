class Solution:
    def fun1(self): # object method
        print("hi from fun1")

    def fun2(): # class method.
        print("hi from fun2")


sol=Solution()
sol.fun1()
# sol.fun2() # TypeError: Solution.fun2() takes 0 positional arguments but 1 was given

Solution.fun2()

# self - represents the current instance of a class, allowing you to access and modify the specific object's attributes and methods