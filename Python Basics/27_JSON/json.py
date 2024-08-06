# Python JSON

"""
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
"""

# JSON is often used when data is sent from a server to a web browser.

# JSON in python

import json

# Parse JSON - Convert from JSON to Python

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) 

# Output: 30

print("------------------------------------------------")
####################################################################


# Convert from Python to JSON

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y) 

# Output: {"name": "John", "age": 30, "city": "New York"}

print("------------------------------------------------")
####################################################################

# The json.dumps() method returns a JSON string,
# but you can convert Python objects of any type to a JSON string using the json.dumps() method.

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("------------------------------------------------")
####################################################################

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

print("------------------------------------------------")
####################################################################

# Format the Result

import json

json.dumps(x, indent=4)

json.dumps(x, indent=4, separators=(". ", " = "))

# Order the Result

json.dumps(x, indent=4, sort_keys=True)