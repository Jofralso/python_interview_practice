# Lists

mylist = ["apple", "banana", "cherry"]
print(mylist)

print("------------------------------------------------")
####################################################################

# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

####################################################################

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

# If you add new items to a list, the new items will be placed at the end of the list.

####################################################################

# Changeable
# The list is changeable, meaning that we can change, add or remove items in a list after it has been created

# Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) # ['apple', 'banana', 'cherry', 'apple', 'cherry']

print("------------------------------------------------")
####################################################################

# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # 3

print("------------------------------------------------")
####################################################################    

# List Items - Data Types
list1 = ["abc", 34, True, 40, "male"]
print(list1) # ['abc', 34, True, 40, 'male']

print("------------------------------------------------")
####################################################################

# type()

# <class 'list'>

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

print("------------------------------------------------")
####################################################################

# The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) # ['apple', 'banana', 'cherry']

print("------------------------------------------------")
####################################################################

# Python Collections (Arrays)

# There are four collection data types in the Python programming language:
# List is collection which is ordered and changeable. Allows duplicate members.
# Tuple is collection which is ordered and unchangeable. Allows duplicate members.
# Set is collection which is unordered and unchangeable. No duplicate members.
# Dictionary is collection which is unordered and changeable. No duplicate members.

# *Set items are unchangeable, but you can remove and/or add items whenever you like.

# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

####################################################################

# Access Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # banana

print("------------------------------------------------")
####################################################################

# Negative Indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # cherry

print("------------------------------------------------")
####################################################################

# Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist[2:5]) # ['cherry', 'orange', 'kiwi']

# Note: The search will start at index 2 (included) and end at index 5 (not included).

print(thislist[:4])

print(thislist[2:])

print("------------------------------------------------")
####################################################################

# Range of Negative Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist[-4:-1]) # ['orange', 'kiwi', 'mango']

print("------------------------------------------------")
####################################################################

# Check if Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

print("------------------------------------------------")
####################################################################

# Change Item

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # ['apple', 'blackcurrant', 'cherry']

print("------------------------------------------------")
####################################################################

# Change a Range of Items

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

print("------------------------------------------------")
####################################################################

# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # ['apple', 'banana', 'watermelon', 'cherry']

print("------------------------------------------------")
####################################################################

# Append Items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ['apple', 'banana', 'cherry', 'orange']

print("------------------------------------------------")
####################################################################

# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # ['apple', 'orange', 'banana', 'cherry']

print("------------------------------------------------")
####################################################################

# Extend List

thislist = ["apple", "banana", "cherry"]    
thislist.extend(["orange", "mango", "grapes"])
print(thislist) # ['apple', 'banana', 'cherry', 'orange', 'mango', 'grapes']

print("------------------------------------------------")
####################################################################

# Add Any Iterable

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # ['apple', 'banana', 'cherry', 'kiwi', 'orange']

print("------------------------------------------------")
####################################################################

# Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry']

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

print("------------------------------------------------")
####################################################################

# Remove Specified Index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # ['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

print("------------------------------------------------")
####################################################################

# Clear the List

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # []

print("------------------------------------------------")
####################################################################

# Loop Through a List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

print("------------------------------------------------")
####################################################################

# Loop Through the Index Numbers

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

print("------------------------------------------------")
####################################################################

# Using a While Loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1   

print("------------------------------------------------")
####################################################################

# Loop Through List Comprehension

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 

print("------------------------------------------------")
####################################################################

# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # ['apple', 'banana', 'mango']

####################################################################

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 

# Condition 

newlist = [x for x in fruits if x != "apple"]
print(newlist) # ['banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in fruits] # default condition
print(newlist) 

# Iterable

newlist = [x for x in range(10)] 
print(newlist) 
newlist = [x for x in range(10) if x < 5]
print(newlist) 

# Expression

newlist = [x.upper() for x in fruits]
print(newlist) 
newlist = ['hello' for x in fruits]
print(newlist) 
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) 

print("------------------------------------------------")
####################################################################

# Sort List Alphanumerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # [23, 50, 65, 82, 100]

# Sort Descending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) # [100, 82, 65, 50, 23]

print("------------------------------------------------")
####################################################################

# Customize Sort Function

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) # [50, 65, 23, 82, 100]

# Case Insensitive Sort

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # ['Kiwi', 'Orange', 'cherry', 'banana']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange']



print("------------------------------------------------")
####################################################################

# Reverse Order

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # ['cherry', 'Kiwi', 'Orange', 'banana']

print("------------------------------------------------")
####################################################################

# Copy a List

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) # ['apple', 'banana', 'cherry']

# Slice Operator

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
mylist = thislist[:]
print(mylist) # ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']

print("------------------------------------------------")
####################################################################

# Join Lists
# Join Two Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) # ['a', 'b', 'c', 1, 2, 3]

# Another way

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) 

# Extend method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) 