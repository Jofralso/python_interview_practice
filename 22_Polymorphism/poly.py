# Polymorphism

"""
Polymorphism is the ability of an object to take on many forms.
"""

# An example of a Python function that can be used on different objects is the len() function.

# String

x = "Hello World"

print(len(x))

print("------------------------------------------------")
####################################################################

# Tuple

x = ("Hello", "World")

print(len(x))

print("------------------------------------------------")
####################################################################

# List

x = ["Hello", "World"]

print(len(x))

print("------------------------------------------------")
####################################################################

# Dictionary

x = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(len(x))

print("------------------------------------------------")
####################################################################

# Class Polymorphism

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move() #Drive! Sail! Fly!

print("------------------------------------------------")
####################################################################

# Inheritance Class Polymorphism

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move() 

  
  
