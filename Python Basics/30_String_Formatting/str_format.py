# String Format

# F-String

txt = f"The price is 49 dollars"
print(txt)

# Output: The price is 49 dollars

print("------------------------------------------------")
####################################################################

# Placeholders and Modifiers

price = 59
txt = f"The price is {price} dollars"
print(txt)

# Output: The price is 59 dollars

print("------------------------------------------------")
####################################################################

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Output: The price is 59.00 dollars

print("------------------------------------------------")
####################################################################

txt = f"The price is {95:.2f} dollars"
print(txt)

# Output: The price is 95.00 dollars

print("------------------------------------------------")
####################################################################

# Perform Operations in F-Strings

txt = f"The price is {20 * 59} dollars"
print(txt)

# Output: The price is 1180 dollars

print("------------------------------------------------")
####################################################################

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

# Output: The price is 89.94999999999999 dollars

print("------------------------------------------------")
####################################################################

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

# Output: It is very Cheap

print("------------------------------------------------")
####################################################################

# Execute Functions in F-Strings

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

# Output: I love APPLES

print("------------------------------------------------")
####################################################################

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)  

# Output: The plane is flying at a 9144.0 meter altitude

print("------------------------------------------------")
####################################################################

#More Modifiers

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

# Output: The price is 59,000 dollars

print("------------------------------------------------")
####################################################################

"""

Formatting Types
:< 	
Left aligns the result (within the available space)
:> 	
Right aligns the result (within the available space)
:^ 	
Center aligns the result (within the available space)
:= 	
Places the sign to the left most position
:+ 	
Use a plus sign to indicate if the result is positive or negative
:- 	
Use a minus sign for negative values only
:  	
Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:, 	
Use a comma as a thousand separator
:_ 	
Use a underscore as a thousand separator
:b 	
Binary format
:c 		Converts the value into the corresponding Unicode character
:d 	
Decimal format
:e 	
Scientific format, with a lower case e
:E 	
Scientific format, with an upper case E
:f 	
Fix point number format
:F 	
Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g 		General format
:G 		General format (using a upper case E for scientific notations)
:o 	
Octal format
:x 	
Hex format, lower case
:X 	
Hex format, upper case
:n 		Number format
:% 	
Percentage format

"""

# String format()


price = 49
txt = "The price is {} dollars"
print(txt.format(price))

txt = "The price is {:.2f} dollars"
print(txt.format(price))

print("------------------------------------------------")
####################################################################

#Multiple Values

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Output: I want 3 pieces of item number 567 for 49.00 dollars.

print("------------------------------------------------")
####################################################################

#Index Numbers

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Output: I want 3 pieces of item number 567 for 49.00 dollars.

print("------------------------------------------------")
####################################################################

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Output: His name is John. John is 36 years old.

print("------------------------------------------------")
####################################################################

# Named Indexes

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))