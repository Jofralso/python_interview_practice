# Inheritance

"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child Class is the class that inherits from another class, also called derived class.
"""


# Create a Parent Class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() 

print("------------------------------------------------")
####################################################################


# Create a Child Class

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

print("------------------------------------------------")
####################################################################


# Add the __init__() Function

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()


# Create a class named Person, use the Person class to create an object named p1, and call its printname method.

# Output:

# Mike Olsen

print("------------------------------------------------")
####################################################################


# Use the super() Function

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

print("------------------------------------------------")
####################################################################

# Add Properties

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")

print(x.graduationyear)

print("------------------------------------------------")
####################################################################


# Add Methods

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen")
x.welcome() 