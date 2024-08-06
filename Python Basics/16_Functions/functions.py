# Creating a Function

def myFunction():
    print("Hello from a function")

# Calling a Function
myFunction()

print("------------------------------------------------")
####################################################################

# Passing Arguments

def myfunction(fname):
    print(fname + " Refsnes")

myfunction("Emil")
myfunction("Tobias")
myfunction("Linus")

print("------------------------------------------------")
####################################################################

# Number of Arguments

def myfunction(fname, lname):
    print(fname + " " + lname)

myfunction("Emil", "Refsnes")
myfunction("Tobias", "Refsnes")
myfunction("Linus", "Refsnes")

print("------------------------------------------------")
####################################################################

# Arbitrary Arguments, *args

def myfunction(*kids):
    print("The youngest child is " + kids[2])

myfunction("Emil", "Tobias", "Linus") 

print("------------------------------------------------")
###################################################################

# Keyword Arguments

# Arbitrary Keyword Arguments, **kwargs

def myfunction(**kid):
    print("His last name is " + kid["lname"])

myfunction(fname = "Tobias", lname = "Refsnes")

print("------------------------------------------------")
####################################################################

# Default Parameter Value

def myfunction(country = "Norway"):
    print("I am from " + country)

myfunction("Sweden")
myfunction("India")
myfunction()
myfunction("Brazil")

print("------------------------------------------------")
####################################################################

# Passing a List as an Argument

def myfunction(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

myfunction(fruits)

print("------------------------------------------------")
####################################################################

# Return Values

def myfunction(x):
    return 5 * x

print(myfunction(3))
print(myfunction(5))
print(myfunction(9))

print("------------------------------------------------")
####################################################################

# The pass Statement

def myfunction():
  pass

print("------------------------------------------------")
####################################################################

# Positional-Only Arguments

def my_function(x, /):
  print(x)

my_function(3) 

print("------------------------------------------------")
####################################################################

# Keyword-Only Arguments

def my_function(*, x):
  print(x)

my_function(x = 3)

print("------------------------------------------------")
####################################################################

# Combine Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8) 

print("------------------------------------------------")
###################################################################

# Recursion 

"""

Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. 
This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing 
a function which never terminates, or one that uses excess amounts of memory or processor power. 
However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). 
We use the k variable as the data, which decrements (-1) every time we recurse. 
The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
"""

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)