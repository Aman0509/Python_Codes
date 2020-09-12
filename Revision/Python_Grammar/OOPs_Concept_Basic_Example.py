#  How to define a class

class Class0:
    """
    As soon as we define a class, a new class object is created with the same name. This class object allows
    us to access the different attributes as well as to instantiate new objects of that class.
    """
    # Class Variables
    a = 1
    b = 2
    c = 3


print("Class0.a = ", Class0.a)
print("Class0.a = ", Class0.b)
print("Class0.a = ", Class0.c)
print(Class0.__doc__)
print()


# ---------------------------------------------------------------------------------------------------

# Creating object and constructor in class

class Class1:
    """This is a default Constructor. In this case __init__ method is not defined in the class but still we are able to
     create object. This is because python implicitly inject constructor with no body, like below:
     def __init__(self):
        # no body, does nothing
     """

    def some_method(self):
        print("This is a method defined in a class where no constructor is present.")


ob = Class1()
ob.some_method()
print()


# ---------------------------------------------------------------------------------------------------


class Class2:
    # Class Variable
    a = 23

    def __init__(self):
        """This is a Non parameterized constructor as nothing is passed in init method"""
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
    # class variable
    temp = "Baba Yaga"
    def method1(self):
        print("This is a method1 of Class6")


class Class6Child(Class6):

    def method1(self):
        """If for some reason, you still want to access the overridden method of the parent class in the child class,
        you can call it using the super() function"""
        print(super().temp)  # By both ways, you can
        print(Class6.temp)   # call parent class variables or methods
        super().method1()
        Class6.method1(self)
        print("This is a method1 of Class6Child")


obj6 = Class6Child()
obj6.method1()
print()


# ---------------------------------------------------------------------------------------------------

# Constructor Overloading - It is not allowed in python

# Example 1 - More than one constructor

class Test1:

    def __init__(self):
        print("1st Constructor")

    def __init__(self):
        print("2nd Constructor")

    def __init__(self):
        print("3rd Constructor")


obj5 = Test1()


# Example 2 - Two different kind of Constructor

class Test2:

    def __init__(self):
        print("1st Constructor")

    def __init__(self, a):
        self.a = a
        print(f"2nd Constructor and {self.a}")


# obj6 = Test2() <-- This will throw error
obj6 = Test2(4)
print()


# Example 3 - Using default arguments is not considered as constructor overloading

class Test3:

    def __init__(self, a=5, b=6):
        print("Sum = ", a + b)


obj7 = Test3()
obj7 = Test3(3, 6)
print()

# ---------------------------------------------------------------------------------------------------

# Destructor in Python
"""
- Like destructor is counter-part of a constructor, function __del__ is the counter-part of __new__.
- __del__ method is called for ay object when the reference count for that object becomes zero.
- As a reference counting is performed, hence it is not necessary that for an object __del__ method will be called if it
  goes out of scope. The destructor method will only be called when the reference count becomes zero.
- Destructor is called after the program ended or when all the references to object are deleted.

Cases when destructor do not behave correctly
- Circular Referencing
- Exception in __init__ method

"""


class Destructor:

    def __init__(self):
        print("Inside init")
        print("init will initialise")

    def __del__(self):
        print("Inside del")
        print("It will free up memory be deleting the object when it's reference count is zero")
        print()


print("Creating Object..")
obj = Destructor()
print("End of creating object and it is not in use anymore")


# ---------------------------------------------------------------------------------------------------

# Method Overloading

class Overloading:

    def method(self, m = None, n = None, o = None):
        if m is not None and n is not None and o is not None:
            print("All three arguments were pass")
        elif m is not None and n is not None:
            print("2 arguments were pass")
        elif m is not None:
            print("Only one was passed")
        else:
            print("No arguments were passed")


obj = Overloading()
obj.method()
obj.method(2, 6)
obj.method(7, 2, 8)
print()
