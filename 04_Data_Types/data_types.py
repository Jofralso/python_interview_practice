# Built-in Data Types

"""
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Types:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""

# Get the Data Type

x = 5
y = "Hello, World!"
z = True
a = 5.0

print(type(x))
print(type(y))
print(type(z))
print(type(a))

print("------------------------------------------------")
###################################################################

# Setting the Data Type

x = "Hello" # str
y = 20 # int
z = 20.5 # float
a = 1j # complex
l = ["apple", "banana", "cherry"] # list
t = ("apple", "banana", "cherry") # tuple
s = {"apple", "banana", "cherry"} # set
f = frozenset({"apple", "banana", "cherry"}) # frozenset
d = {"name" : "John", "age" : 36} # dict
e = True # bool
g = b"Hello" # bytes
h = bytearray(5) # bytearray
i = memoryview(bytes(5)) # memoryview

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(l))
print(type(t))
print(type(s))
print(type(f))
print(type(d))
print(type(e))
print(type(g))
print(type(h))
print(type(i))

print("------------------------------------------------")
###################################################################

#Setting the Specified Data Type

x = str("Hello") # str
y = int(20) # int
z = float(20.5) # float
a = complex(1j) # complex
l = list(("apple", "banana", "cherry")) # list
t = tuple(("apple", "banana", "cherry")) # tuple
s = set(("apple", "banana", "cherry")) # set
f = frozenset(("apple", "banana", "cherry")) # frozenset
d = dict(name="John", age=36) # dict
e = bool(5) # bool
g = bytes(5) # bytes
h = bytearray(5) # bytearray
i = memoryview(bytes(5)) # memoryview

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(l))
print(type(t)) 
print(type(s))
print(type(f))
print(type(d))
print(type(e))
print(type(g))
print(type(h))
print(type(i))

print("------------------------------------------------")
####################################################################