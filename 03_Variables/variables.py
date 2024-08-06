# Python Variables

# Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it.
x = 5
y = "John"

print(x)
print(y)

print("------------------------------------------------")
######################################################################

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
print("------------------------------------------------")
######################################################################

# Casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

print("------------------------------------------------")
#####################################################################

# Get the Type

x = 5
y = "John"
print(type(x))
print(type(y))

print("------------------------------------------------")
#####################################################################

# Single or Double Quotes?

a = "Hello"
b = 'Hello'
print(a)
print(b)

print("------------------------------------------------")
#####################################################################   

# Case Sensitivity

a = 4
A = "Sally"
print(a)
print(A)

print("------------------------------------------------")
#####################################################################

# Variable Names

myvar = "John" 
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# my-var = "John"   #SyntaxError: invalid syntax
# my var = "John"   #SyntaxError: invalid syntax
# 2myvar = "John"   #SyntaxError: invalid syntax


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

print("------------------------------------------------")
#####################################################################

# Multiple Words Variable Name

myVariableName = "John" # Camel Case
MyVariableName = "John" # Pascal Case
MYVARIABLENAME = "John" # Snake Case

print(myVariableName)
print(MyVariableName)
print(MYVARIABLENAME)

print("------------------------------------------------")
#####################################################################

# Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("------------------------------------------------")
#####################################################################

# One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

print("------------------------------------------------")
#####################################################################

# Unpack Variables

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)    

print("------------------------------------------------")
#####################################################################

# Output Variables

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Notice the space characters after the words, otherwise the result would be "Pythonisawesome".

# For numbers, the + character works as a mathematical operator.

x = 5
y = 10
print(x + y)    

# In the print() function, when you try to combine a string and a number with the + character, Python will give you an error:

#x = 5
#y = "John"
#print(x + y)    

# The best way to output multiple variables in the print() function is to separate them with commas, 
# which even support different data types:

x = 5
y = "John"
print(x, y)

print("------------------------------------------------")
#####################################################################   

# Global Variables

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# if you create a variable with the same name inside a function, 
# the variable will be local, and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 

print("------------------------------------------------")
#####################################################################

# The global Keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

# Also, use the global keyword if you want to change a global variable inside a function.

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

print("------------------------------------------------")
#####################################################################