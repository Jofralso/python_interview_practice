# Iterator vs Iterable

"""

An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

"""

# Create an Iterator

mylist = [1, 3, 5, 7, 9]

myit = iter(mylist)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Output: 1 3 5 7 9

print("------------------------------------------------")
####################################################################

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Output: b a n a n a

print("------------------------------------------------")
####################################################################


# Looping Through an Iterator

mylist = [1, 3, 5, 7, 9]

for x in mylist:
    print(x)

# Output: 1 3 5 7 9

print("------------------------------------------------")
####################################################################

# Create an Iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)) 

print("------------------------------------------------")
####################################################################


# StopIteration

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)