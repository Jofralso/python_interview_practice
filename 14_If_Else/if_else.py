# Python Conditions and If statements

"""

Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

"""

a = 33
b = 200

if b > a:
  print("b is greater than a")

# Output: b is greater than a

print("------------------------------------------------")
####################################################################

# Indentation

"""
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
Other programming languages often use curly-brackets for this purpose. 
"""

# Elif

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Output: a and b are equal

print("------------------------------------------------")
####################################################################

# Else

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Output: a is greater than b

print("------------------------------------------------")
####################################################################

# Short Hand If

if a > b: print("a is greater than b")

# Short Hand If ... Else

a = 2
b = 330
print("A") if a > b else print("B")

# Output: B

print("------------------------------------------------")
####################################################################

# And

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# Output: Both conditions are True

print("------------------------------------------------")
####################################################################

# Or

a = 200
b = 33
c = 500

if a > b or a > c:
  print("At least one of the conditions is True")

# Output: At least one of the conditions is True

print("------------------------------------------------")
####################################################################

# Not

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Output: a is NOT greater than b

print("------------------------------------------------")
####################################################################

# Nested If

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Output: Above ten, and also above 20!

print("------------------------------------------------")
####################################################################

# The pass Statement

a = 33
b = 200

if b > a:
  pass

# Output: no output

print("------------------------------------------------")
####################################################################

