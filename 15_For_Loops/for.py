# For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("------------------------------------------------")
####################################################################

# Loop Through a String

for x in "banana":
  print(x)

print("------------------------------------------------")
####################################################################

# The break Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("------------------------------------------------")
####################################################################

# The continue Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("------------------------------------------------")
####################################################################

# The range() Function

for x in range(6):
  print(x)

print("------------------------------------------------")
####################################################################

for x in range(2, 6):
  print(x)

print("------------------------------------------------")
####################################################################

for x in range(2, 30, 3):
  print(x)

print("------------------------------------------------")
####################################################################

for x in range(6):
  print(x) # 0, 1, 2, 3, 4, 5
else:
  print("Finally finished!")

print("------------------------------------------------")
####################################################################

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") # 0, 1, 2

print("------------------------------------------------")
####################################################################

# Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) # red apple, red banana, red cherry, big apple, big banana, big cherry, tasty apple, tasty banana, tasty cherry

print("------------------------------------------------")
####################################################################

# The pass Statement

for x in [0, 1, 2]:
  pass


