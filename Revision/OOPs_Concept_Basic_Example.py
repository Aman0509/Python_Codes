#  How to define a class

class Class1:
    # Class Variables
    a = 1
    b = 2
    c = 3


print("Class1.a = ", Class1.a)
print("Class1.a = ", Class1.b)
print("Class1.a = ", Class1.c)
print()


# ---------------------------------------------------------------------------------------------------

# Creating object and constructor in class

class Class2:
    # Class Variable
    a = 23

    def __init__(self):
        """This is a default constructor"""
        # Instance Variable
        self.b = 24
        self.c = 25


obj2 = Class2()
print("obj2.a = ", obj2.a)
print("obj2.b = ", obj2.b)
print("obj2.c = ", obj2.c)
print()


# ---------------------------------------------------------------------------------------------------

# This is an example of parametrized constructor

class Class3:
    # Class Variable
    a = 33

    def __init__(self, b, c):
        """This is a parameterized constructor"""
        self.b = b
        self.c = c


obj3 = Class3(33, 34)
print("obj3.a = ", obj3.a)
print("obj3.b = ", obj3.b)
print("obj3.c = ", obj3.c)
print()


# ---------------------------------------------------------------------------------------------------

# Encapsulation - Private, Protected and Public

class Class4:
    """Demo of public, private and protected will be shown"""

    def __init__(self, var1):
        self.var1 = var1
        self._var2 = 'This is protected'
        self.__var3 = 'This is private'

    # Instance Methods
    def pub(self):
        print("This is public method")
        print("var1 = ", self.var1)
        print("var2 = ", self._var2)
        print("var3 = ", self.__var3)

    def _protect(self):
        print("This is protect method")
        print("var1 = ", self.var1)
        print("var2 = ", self._var2)
        print("var3 = ", self.__var3)

    def __private(self):
        print("This is private method")
        print("var1 = ", self.var1)
        print("var2 = ", self._var2)
        print("var3 = ", self.__var3)


obj4 = Class4('Passing while creating object')
print(dir(obj4))
obj4.pub()
obj4._protect()
# obj4.__private() <-- This will throw error
obj4._Class4__private()  # <-- In that way, you can access private attributes or methods. This is called Name Mangling.
print()

# ---------------------------------------------------------------------------------------------------

# Name Mangling is also helpful for letting subclasses override methods without breaking interclass method calls.

class Class5:
    def __init__(self):
        print("This is a parent class")
        self.__method1()

    def method1(self):
        print("This is a method defined in Class5")

    __method1 = method1  # Making private copy of method1 method


class Class5Child(Class5):
    def method1(self):
        print("This is a method defined in Class5_child")


obj5 = Class5Child()
obj5.method1()
print()

# ---------------------------------------------------------------------------------------------------

# Polymorphism


class Class6:

    def method1(self):
        print("This is a method1 of Class6")


class Class6Child(Class6):

    def method1(self):
        """If for some reason, you still want to access the overridden method of the parent class in the child class,
        you can call it using the super() function"""
        super().method1()
        print("This is a method1 of Class6Child")


obj6 = Class6Child()
obj6.method1()


