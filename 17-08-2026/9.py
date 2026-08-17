# palindrome : eg: malayalam ,mom ,121, -121

def isPlaindrome(ip):
    return False if ip<0 else str(ip)==str(ip)[::-1] # compare original string with its reverse.

print(isPlaindrome(-121))
print(isPlaindrome(121))
