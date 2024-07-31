# Strings

print("Hello")
print('Hello')

print("------------------------------------------------")
####################################################################

# Quotes inside Quotes

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print("He is called \"Johnny\"")

print("------------------------------------------------")
####################################################################

# Assign String to a Variable

a = "Hello"
print(a)

print("------------------------------------------------")
####################################################################

# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# or use three single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

print("------------------------------------------------")
####################################################################

# Strings are Arrays

a = "Hello, World!"
print(a[1])

print("------------------------------------------------")
####################################################################

# Looping Through a String

for x in "banana":
    print(x)

print("------------------------------------------------")
####################################################################

# String Length

a = "Hello, World!"
print(len(a))

print("------------------------------------------------")
####################################################################

# Check String

txt = "The best things in life are free!"
print("free" in txt)

print("------------------------------------------------")
####################################################################

# Check if NOT

txt = "The best things in life are free!"
print("expensive" not in txt)

print("------------------------------------------------")
####################################################################

# Slicing

a = "Hello, World!"
print(a[2:5]) # from 2 to 5
print(a[:5]) # from 0 to 5
print(a[2:]) # from 2 to end
print(a[-5:-2]) # from -5 to -2

print("------------------------------------------------")
####################################################################

# Modify String

# Uppercase

a = "Hello, World!"
print(a.upper())

# Lowercase

a = "Hello, World!"
print(a.lower())   

# Replace String

a = "Hello, World!"
print(a.replace("H", "J"))

# Split String

a = "Hello, World!"
print(a.split(","))

print("------------------------------------------------")
####################################################################   

# String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c) 

print("------------------------------------------------")
####################################################################

# String Format

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print("------------------------------------------------")
####################################################################

# F-Strings

age = 36
txt = f"My name is John, and I am {age}"
print(txt)

print("------------------------------------------------")
####################################################################

# Placeholder and Modifiers

price = 59
txt = f"The price is {price} dollars"
print(txt)

"""
A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, 
like .2f which means fixed point number with 2 decimals:
"""

txt = f"The price is {price:.2f} dollars"
print(txt)

"""A placeholder can contain Python code, like math operations:"""

txt = f"The price is {20 * 59} dollars"
print(txt)


print("------------------------------------------------")
####################################################################

# Escape Character

"""To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
"""

txt = "We are the so-called \"Vikings\" from the north."
print(txt)


# Escape Characters

# Other escape characters used in Python:

# \' = Single Quote
# \" = Double Quote
# \\ = Backslash
# \n = New Line
# \t = Tab
# \r = Carriage Return
# \b = Backspace
# \f = Form Feed
# \ooo = Character with octal value ooo
# \xhh = Character with hex value hh




print("------------------------------------------------")
####################################################################


# String Methods

"""Python has a set of built-in methods that you can use on strings."""
""""
capitalize() -	Converts the first character to upper case
casefold()-	Converts string into lower case
center()-	Returns a centered string
count()-	Returns the number of times a specified value occurs in a string
encode()-	Returns an encoded version of the string
endswith()-	Returns true if the string ends with the specified value
expandtabs()-	Sets the tab size of the string
find()-	Searches the string for a specified value and returns the position of where it was found
format()-	Formats specified values in a string
format_map()-	Formats specified values in a string
index()-	Searches the string for a specified value and returns the position of where it was found
isalnum()-	Returns True if all characters in the string are alphanumeric
isalpha()-	Returns True if all characters in the string are in the alphabet
isascii()-	Returns True if all characters in the string are ascii characters
isdecimal()-	Returns True if all characters in the string are decimals
isdigit()-	Returns True if all characters in the string are digits
isidentifier()-	Returns True if the string is an identifier
islower()-	Returns True if all characters in the string are lower case
isnumeric()-	Returns True if all characters in the string are numeric
isprintable()-	Returns True if all characters in the string are printable
isspace()-	Returns True if all characters in the string are whitespaces
istitle()- 	Returns True if the string follows the rules of a title
isupper()-	Returns True if all characters in the string are upper case
join()-	Joins the elements of an iterable to the end of the string
ljust()-	Returns a left justified version of the string
lower()-	Converts a string into lower case
lstrip()-	Returns a left trim version of the string
maketrans()-	Returns a translation table to be used in translations
partition()-	Returns a tuple where the string is parted into three parts
replace()-	Returns a string where a specified value is replaced with a specified value
rfind()-	Searches the string for a specified value and returns the last position of where it was found
rindex()-	Searches the string for a specified value and returns the last position of where it was found
rjust()-	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()-	Splits the string at the specified separator, and returns a list
rstrip()-	Returns a right trim version of the string
split()-	Splits the string at the specified separator, and returns a list
splitlines()-	Splits the string at line breaks and returns a list
startswith()-	Returns true if the string starts with the specified value
strip()-	Returns a trimmed version of the string
swapcase()-	Swaps cases, lower case becomes upper case and vice versa
title()-	Converts the first character of each word to upper case
translate()-	Returns a translated string
upper()-	Converts a string into upper case
zfill()-	Fills the string with a specified number of 0 values at the beginning
"""



s1 = "hello"
s2 = "  hello"
s3 = "hello  "
s4 = "hello world"
s5 = "hello_world"
s6 = "hello world"
s7 = "2345"
s8 = "HelLo wOrld"
s9 = "Hello {name}"

print(s1.capitalize()) # Hello
print(s8.casefold()) # hello world
print(s3.center(10)) #  hello  
print(s4.count("l")) # 3
print(s4.encode()) # b'hello world'
print(s4.endswith("world")) # True
print(s3.expandtabs(10)) # h   e   l   l   o
print(s4.find("world")) # 6
print(s9.format(name="John")) # hello John
print(s9.format_map({"name":"John"})) # hello John
print(s4.index("world")) # 6
print(s4.isalnum()) # False
print(s4.isalpha()) # False
print(s4.isascii()) # True
print(s7.isdecimal()) # True
print(s7.isdigit()) # True
print(s6.isidentifier()) # True
print(s1.islower()) # True
print(s7.isnumeric()) # True
print(s3.isprintable()) # True
print(s2.isspace()) # False
print(s6.istitle()) # True
print(s1.isupper()) # False
print(s4.join(["hi", "there"])) # hi world there
print(s3.ljust(10)) # hello  
print(s1.lower()) # hello
print(s2.lstrip()) # hello  
print(str.maketrans("aeiou", "12345", "AEIOU")) # {49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 97: '1', 98: '2', 99: '3', 100: '4', 101: '5', 65: '1', 66: '2', 67: '3', 68: '4', 69: '5', 103: '1', 104: '2', 105: '3', 106: '4', 107: '5'}
print(s4.partition("world")) # ('hello ', 'world', '')
print(s4.replace("world", "there")) # hello there
print(s4.rfind("world")) # 6
print(s4.rindex("world")) # 6
print(s4.rjust(10)) #    hello
print(s4.rpartition("world")) # ('', 'world', '')
print(s4.rsplit("world")) # ['hello', '']
print(s3.rstrip()) # hello
print(s4.split("world")) # ['hello', '']
print(s4.splitlines()) # ['hello world']
print(s4.startswith("hello")) # True
print(s3.strip()) # hello
print(s1.swapcase()) # HELLO
print(s6.title()) # Hello World

print(s4.translate(str.maketrans("aeiou", "12345", "AEIOU"))) # h1ll0 w0rld

print(s1.upper()) # HELLO
print(s7.zfill(10)) # 0000002345

