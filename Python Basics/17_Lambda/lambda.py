# Python Lambda

x = lambda a : a + 10
print(x(5)) 

print("------------------------------------------------")
####################################################################

x = lambda a, b : a * b
print(x(5, 6))

print("------------------------------------------------")
####################################################################

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print("------------------------------------------------")
####################################################################

#  Why Use Lambda Functions?

"""
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number.

Use that function definition to make a function that always doubles the number you send in.

"""
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

print("------------------------------------------------")
####################################################################

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

# Output: 33

print("------------------------------------------------")
####################################################################

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))