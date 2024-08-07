"""
This code defines a function `palindrome_checker` 
that checks if a string `s` is a palindrome 
by comparing it to its reverse. 
It returns `True` if `s` is a palindrome and `False` 
otherwise.
"""

def palindrome_checker(s: str) -> bool:
    return s==s[::-1]


print(palindrome_checker("racecar"))
print(palindrome_checker("hello"))