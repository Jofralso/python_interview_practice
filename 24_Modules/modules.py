# Modules

"""
A module is a file containing Python definitions and statements.
"""

# Create Module

import mymodule

mymodule.greeting("Jonathan")

# Output: Hello Jonathan

print("------------------------------------------------")
####################################################################

# Variables in Module
import mymodule

a = mymodule.person1["age"]
print(a) 

# Output: 36

print("------------------------------------------------")
####################################################################

# Naming a Module

import mymodule as mx

a = mx.person1["age"]
print(a)

# Output: 36

print("------------------------------------------------")
####################################################################

# Built-in Modules

import platform

x = platform.system()
print(x) 

# Output: Linux

print("------------------------------------------------")
####################################################################

# Using the dir() Function

import platform

x = dir(platform)
print(x)

print("------------------------------------------------")
####################################################################

# Import From Module

from mymodule import person1

print (person1["age"])