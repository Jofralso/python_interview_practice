# Python Operators
print(10 + 5)

"""
Python divides the operators in the following groups:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators


"""

print("------------------------------------------------")
####################################################################

# Arithmetic Operators

print(10 + 5) # 15 addition
print(10 - 5) # 5 subtraction
print(10 * 5) # 50 multiplication
print(10 / 5) # 2.0 division
print(10 % 5) # 0 modulus
print(10 ** 5) # 100000 exponent
print(10 // 5) # 2 floor division

print("------------------------------------------------")
####################################################################

# Assignment Operators
"""
x = 10 # x = 10
x += 5 # x = x + 5
x -= 5 # x = x - 5
x *= 5 # x = x * 5
x /= 5 # x = x / 5
x %= 5 # x = x % 5
x **= 5 # x = x ** 5
x //= 5 # x = x // 5
x &= 5 # x = x & 5
x |= 5 # x = x | 5
x ^= 5 # x = x ^ 5
x >>= 5 # x = x >> 5 
x <<= 5 # x = x << 5
"""
print("------------------------------------------------")
####################################################################

# Comparison Operators

print(10 == 5) # False
print(10 != 5) # True
print(10 > 5) # True
print(10 < 5) # False
print(10 >= 5) # True
print(10 <= 5) # False

print("------------------------------------------------")
####################################################################

# Logical Operators

print(10 and 5) # 5
print(10 or 5) # 10
print(not 10) # False

print("------------------------------------------------")
####################################################################

# Identity Operators

print(10 is 5) # False
print(10 is not 5) # True

print("------------------------------------------------")
####################################################################    

# Membership Operators

print(10 in [1, 2, 3, 4, 5]) # True
print(10 not in [1, 2, 3, 4, 5]) # False

print("------------------------------------------------")
####################################################################

# Bitwise Operators

print(10 & 5) # 0
print(10 | 5) # 15
print(10 ^ 5) # 15
print(~10) # -11
print(10 << 5) # 160
print(10 >> 5) # 0

print("------------------------------------------------")
####################################################################

# Operator Precedence

print(10 + 5 * 3) # 25
print((10 + 5) * 3) # 50
print(10 + 5 * 3 / 2) # 17.5
print((10 + 5) * 3 / 2) # 22.5
print(10 + 5 * (3 / 2)) # 17.5

# The precedence order is described in the table below, starting with the highest precedence at the top:


# Operator Precedence Table
# Operator	Level
# **	5
# * / // %	4
# + -	3
# << >>	2
# &	1
# |	0
# = += -= *= /= //= %= ^= &= |= <<= >>=
# not
# and
# or

print("------------------------------------------------")
####################################################################
