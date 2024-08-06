# Tuples

mytuple = ("apple", "banana", "cherry")
print(mytuple) # ('apple', 'banana', 'cherry')

"""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
"""
print("------------------------------------------------")

####################################################################
"""
Tuple Items

Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
Ordered

When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
Unchangeable

Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
Allow Duplicates

Since tuples are indexed, they can have items with the same value:
"""

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print("------------------------------------------------")
####################################################################

# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # 3

print("------------------------------------------------")
####################################################################

# Create Tuple With One Item

thistuple = ("apple",)
print(type(thistuple)) # <class 'tuple'>

thistuple = ("apple")
print(type(thistuple)) # <class 'str'>

print("------------------------------------------------")
####################################################################    

# Tuple Items - Data Types

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple4 = ("abc", 34, True, 40, "male")
print(tuple4) # ('abc', 34, True, 40, 'male')

print("------------------------------------------------")
####################################################################

# type()

# <class 'tuple'>

mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) # <class 'tuple'>

print("------------------------------------------------")
####################################################################

# The tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) # ('apple', 'banana', 'cherry')

print("------------------------------------------------")
####################################################################    

# Access Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # banana

print("------------------------------------------------")
####################################################################    

# Negative Indexing

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # cherry

print("------------------------------------------------")
####################################################################

# Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "mango")
print(thistuple[2:5]) # ('cherry', 'orange', 'kiwi')    

# Note: The search will start at index 2 (included) and end at index 5 (not included).

print(thistuple[:4])

print(thistuple[2:])

print("------------------------------------------------")
####################################################################

# Range of Negative Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "mango")
print(thistuple[-4:-1]) # ('orange', 'kiwi', 'mango')

print("------------------------------------------------")
####################################################################

# Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

print("------------------------------------------------")
####################################################################

# Changing Tuples

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) # ('apple', 'kiwi', 'cherry')
print(y) # ['apple', 'kiwi', 'cherry']

print("------------------------------------------------")
####################################################################

# Add Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple) # ('apple', 'banana', 'cherry', 'orange')

print("------------------------------------------------")
####################################################################

# Remove Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple) # ('banana', 'cherry')

print("------------------------------------------------")
####################################################################

# Using the "del" Keyword

thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) # NameError: name 'thistuple' is not defined

print("------------------------------------------------")
####################################################################

# Unpack Tuples

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green) # apple
print(yellow) # banana
print(red) # cherry

print("------------------------------------------------")
####################################################################

# Using * Operator

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) # apple
print(yellow) # banana
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

print("------------------------------------------------")
####################################################################

# Loop Tuples

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

print("------------------------------------------------")
####################################################################

# Loop Through the Index Numbers

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

print("------------------------------------------------")
####################################################################

# Using a While Loop

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

print("------------------------------------------------")
####################################################################

# Join Two Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) # ('a', 'b', 'c', 1, 2, 3)

print("------------------------------------------------")
####################################################################

# Multiply Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

print("------------------------------------------------")
###################################################################

# Multiply Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

print("------------------------------------------------")
####################################################################    

# Tuples Methods

mytuple = ("apple", "banana", "cherry")
print(mytuple.count("apple")) # 1
print(mytuple.index("cherry")) # 2
