"""
Static/Class Variable

- Static or Class Variables are ons that belong to th class and not to objects.
- Static Variables are shared amongst objects of the class.
- Python allows providing same variable name for a class/static variable and an instance variable. But it is
  recommended to not provide same name variables to these variables to avoid confusion.

Static Method

- These are the methods which are bound to the class rather than an object of the class and hence are called
  using the class name and not the objects of the class.

- As these methods are bound to the class, therefore, they cannot change the state of an object.

- There are 2 ways of defining a static method:
  Using the staticmethod()
  Using the @staticmethod

Use of Static Method

- When you need a utility function that doesn't access any properties of a class but makes sense that it
  belongs to the class, we use static functions.
- Static method are used when we don't want subclasses of a class change/override a specific implementation
  of a method.
"""


# Defining Static Method by using staticmethod()
# This way of creating static method is considered as non-pythonic

class Class1(object):

    def stat_method():
        print("It is a static method")


Class1.stat_method = staticmethod(Class1.stat_method)
Class1.stat_method()
print()


class Class2(object):

    @staticmethod   # This is a modern approach of defining static method
    def stat_method2():
        print("It is a static method 2")


Class2.stat_method2()
