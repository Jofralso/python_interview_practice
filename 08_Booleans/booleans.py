# Booleans

print(10 > 9) # True
print(10 == 9) # False
print(10 < 9) # False

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Output: b is greater than a

print("------------------------------------------------")
####################################################################

# Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most values are true

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# Some values are false

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool({}))
print(bool([]))

# One more value, or object in this case, evaluates to False, 
# and that is if you have an object that is made from a class 
# with a __len__ function that returns 0 or False: 

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) 

# Functions can Return a Boolean

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") 

  #Python also has many built-in functions that return a boolean value, 
  # like the isinstance() function, which can be used to determine if 
  # an object is of a certain data type:

  print(isinstance(10, int))