# File handling

"""
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

"""


# Open a File

f = open("demofile.txt", "r")
print(f.read())

f.close()

print("------------------------------------------------")
####################################################################

f = open("demofile.txt", "rt")
print(f.read())

f.close()


print("------------------------------------------------")
####################################################################

# Read Only Parts of the File

f = open("demofile.txt", "r")
print(f.read(5)) 

f.close()


print("------------------------------------------------")
####################################################################

#Read Line

f = open("demofile.txt", "r")
print(f.readline())

f.close()

print("------------------------------------------------")
####################################################################

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline()) 

f.close()


print("------------------------------------------------")
####################################################################

# Close Files

f = open("demofile.txt", "r")
print(f.readline())
f.close() 

print("------------------------------------------------")
####################################################################

# Write to an Existing File

"""

To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

"""

f = open("demofile1.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read()) 

print("------------------------------------------------")
####################################################################

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read()) 


print("------------------------------------------------")
####################################################################

# Create a New File

f = open("myfile.txt", "x")
f.close()


print("------------------------------------------------")
####################################################################


# Delete File
"""
import os
os.remove("demofile.txt")
"""
"""

The delete() function will delete the specified file path.

"""


print("------------------------------------------------")
####################################################################

# Check if File exist:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 



print("------------------------------------------------")
####################################################################

# Delete Folder


import os
os.rmdir("myfolder") 