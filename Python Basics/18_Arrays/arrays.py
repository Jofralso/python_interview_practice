# Arrays

"""
An array is a special variable, which can hold more than one value at a time.

If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

The solution is an array!

An array can hold many values under a single name, and you can access the values by referring to an index number.


"""

#Accessing Array Items

cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x) # Ford

cars = ["Ford", "Volvo", "BMW"]

x = cars[2]

print(x) # BMW

print("------------------------------------------------")
####################################################################

# Loop Through an Array

cars = ["Ford", "Volvo", "BMW"]

for x in cars:
    print(x)

print("------------------------------------------------")
####################################################################    

# Add Items

cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars) # ['Ford', 'Volvo', 'BMW', 'Honda']

print("------------------------------------------------")
####################################################################

# Remove Items

cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars) # ['Ford', 'BMW']

print("------------------------------------------------")
####################################################################

# Remove Last Item

cars = ["Ford", "Volvo", "BMW"]

cars.pop()

print(cars) # ['Ford', 'Volvo']

print("------------------------------------------------")
####################################################################

# Remove First Item

cars = ["Ford", "Volvo", "BMW"]

cars.pop(0)

print(cars) # ['Volvo', 'BMW']

print("------------------------------------------------")
####################################################################

# Remove Specified Item

cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")

print(cars) # ['Ford', 'BMW']

print("------------------------------------------------")
####################################################################

# Remove All Items

cars = ["Ford", "Volvo", "BMW"]

cars.clear()

print(cars) # []

print("------------------------------------------------")
####################################################################

# Copy Array

cars = ["Ford", "Volvo", "BMW"]

x = cars.copy()

print(x) # ['Ford', 'Volvo', 'BMW'] 

print("------------------------------------------------")
####################################################################

# Length of an Array

cars = ["Ford", "Volvo", "BMW"]

x = len(cars)

print(x) # 3

print("------------------------------------------------")
####################################################################

# Array Methods


"""
append() - Adds an element at the end of the array

clear() - Removes all items from the array

copy() - Returns a copy of the array

count() - Returns the number of times an element is found in the array

extend() - Add the elements of a list (or any iterable), to the end of the current array

index() - Returns the index of the first element with the specified value

insert() - Adds an element at the specified position

pop()	Removes the element at the specified position

remove()	Removes the first item with the specified value

reverse()	Reverses the order of the list

sort()	Sorts the list
"""

