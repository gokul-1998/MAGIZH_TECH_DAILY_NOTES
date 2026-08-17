# make this code more readable for a beginner


def isPalindrome( x: int) -> bool:
        return x >= 0 and str(x) == str(x)[::-1] # x should be positive and palindrome.


def isPalindrome1(x):
    if x<=0:
        return False
    else:
        return str(x)==str(x)[::-1]

    