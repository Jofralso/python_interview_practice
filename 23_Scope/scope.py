# Scope

# Local Scope

def myfunc():
  x = 300
  print(x)

myfunc() 

# Output: 300

print("------------------------------------------------")
####################################################################

# Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc() # Output: 300

print("------------------------------------------------")
####################################################################

# Global Scope

x = 300

def myfunc():
  print(x)

myfunc()

print("------------------------------------------------")
####################################################################

# Naming Variables

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x) # Output: 300

print("------------------------------------------------")
####################################################################
# Global Keyword

def myfunc():
  global x
  x = 300

myfunc()

print(x) 

print("------------------------------------------------")
####################################################################

# Nonlocal Keyword

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())    # Output: hello

