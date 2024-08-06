# Dictionaries

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

print("------------------------------------------------")
####################################################################

# Print All Items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict.items())

print("------------------------------------------------")
####################################################################

# Ordered or Unordered

"""
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
Changeable

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
Duplicates Not Allowed

Dictionaries cannot have two items with the same key:
"""

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) 

print("------------------------------------------------")
####################################################################

# Dictionary Length

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))

print("------------------------------------------------")
####################################################################

# Dictionary Items - Data Types

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) 

print("------------------------------------------------")
####################################################################

# The dict() Constructor

thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)

print("------------------------------------------------")
####################################################################

#Accessing Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x) # Mustang

x = thisdict.get("model")
print(x) # Mustang

print("------------------------------------------------")
####################################################################

# Get Keys

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change 

print("------------------------------------------------")


# Get Values

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "white"

print(x) #after the change 

print("------------------------------------------------")
####################################################################

# Get Items

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "white"

print(x) #after the change 

print("------------------------------------------------")
####################################################################

# Check if Key Exists

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

print("------------------------------------------------")
####################################################################

# Change Values

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

print(thisdict)

print("------------------------------------------------")
####################################################################

# Update Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)

print("------------------------------------------------")
####################################################################

# Add Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

print("------------------------------------------------")
####################################################################

# Remove Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

del thisdict["brand"]
print(thisdict)

del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.clear()
# print(thisdict) #this will output an empty dictionary

print("------------------------------------------------")
####################################################################

# Loop Through a Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)

print("------------------------------------------------")
####################################################################
for x in thisdict:
    print(thisdict[x])

print("------------------------------------------------")
####################################################################
for x in thisdict.values():
    print(x) 

print("------------------------------------------------")
####################################################################

for x in thisdict.keys():
  print(x) 

print("------------------------------------------------")
####################################################################
for x, y in thisdict.items():
    print(x, y)


print("------------------------------------------------")
####################################################################

# Copy a Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

print("------------------------------------------------")
####################################################################

# Nested Dictionaries

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

print("------------------------------------------------")
####################################################################


# Create a Dictionary that Contains Dicts

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

print("------------------------------------------------")
####################################################################

# Access Items in Nested Dictionaries


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child1"]["name"])

print("------------------------------------------------")
####################################################################

# Loop Through Nested Dictionaries

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    
    print(y + ':', obj[y])

print("------------------------------------------------")
####################################################################

# Dictionary Methods

"""

Method 	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

"""

