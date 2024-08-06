# Try Except

"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

"""

# Exception Handling

try:
  print(x)
except:
  print("An exception occurred") 

print("------------------------------------------------")


# Many Exceptions

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong") 

print("------------------------------------------------")

# The Else Statement

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") 

print("------------------------------------------------")
################################################################


# The Finally Statement

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") 

print("------------------------------------------------")
################################################################

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") 

# Output: Something went wrong when opening the file

print("------------------------------------------------")
################################################################


# Raise an Exception

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero") 