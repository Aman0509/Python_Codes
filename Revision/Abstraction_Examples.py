"""
- Abstraction means hiding the complexity and only showing the essential features of the object. So in a way,
  Abstraction means hiding the real implementation and we, as a user, knowing only how to use it.

- Abstraction can be achieved in 2 ways:
    - By using Abstract Class
    - By using Interface

- An abstract class is a class that generally provides incomplete functionality and contains one or more abstract
  methods. Abstract methods are the methods that generally don’t have any implementation, it is left to the sub classes
  to provide implementation for the abstract methods. Here note that in Python abstract method can have implementation
  in the abstract class too but the sub class inheriting that abstract class is still forced to override the abstract
  methods.

- In Python, abstract class is created by deriving from the meta class ABC which belongs to the abc (Abstract Base
  Class) module.
  Syntax for creating abstract class in Python
  from abc import ABC
  Class MyClass(ABC):
    pass

- Abstract class can have both concrete methods as well as abstract methods.

- Abstract class works as a template for other classes. Using an abstract class, you can define a generalized structure
  without providing complete implementation of every method. Methods which provide common functionality to be used for
  all derived classes are defined as concrete methods in abstract class whereas the methods where implementation may
  vary are defined as abstract methods.

- Abstract class can’t be instantiated, so it is not possible to create objects of an abstract class.

- Generally abstract methods defined in abstract class don’t have any body, but it is possible to have abstract methods
  with implementation in abstract class. Any sub class deriving from such abstract class still needs to provide
  implementation for such abstract methods.

- If any abstract method is not implemented by the derived class Python throws an error.

"""

from abc import ABC, abstractmethod

# Defining Abstract class in Python
'''For defining abstract methods in an abstract class method has to be decorated with @abstractmethod decorator.
   From abc module @abstractmethod decorator has to be imported to use that annotation
'''


class TestClass(ABC):

    # concrete method
    def conc_method(self):
        pass

    @abstractmethod
    def abstract_method(self):
        pass


# ======================================================================================================================

# Example 1 - Python Abstract Class
# In this example, we are just defining the method in abstract class and implementing it as well. Afterwards, we are
# also overriding it in subclasses. Please note, it is not an abstract method.

class Polygon(ABC):

    def noofsides(self):
        print("I am just a polygon with n sides")


class Triangle(Polygon):

    def noofsides(self):
        print("A triangle has 3 sides")


class Quadrilateral(Polygon):

    def noofsides(self):
        print("A quadrilateral has 4 sides")


class Pentagon(Polygon):

    def noofsides(self):
        print("A Pentagon has 5 sides")


obj1 = Polygon()  # You can create the object of abstract class, if there are no abstract method defined in it.
obj1.noofsides()
obj1 = Triangle()
obj1.noofsides()
obj1 = Quadrilateral()
obj1.noofsides()
obj1 = Pentagon()
obj1.noofsides()
print()


# ======================================================================================================================

# Example 2 - Defining Abstract method along with concrete method in an Abstract class
# We are not overriding the common method in this example. We are only implementing abstract method as per our desire.


class MainClass(ABC):

    # Concrete Method
    def common_method(self):
        print("This is common method and will be common to all derived/child classes")

    # Abstract method
    @abstractmethod
    def abstract_method(self):
        pass


class ChildClass1(MainClass):

    def abstract_method(self):
        print("I am in ChildClass1")


class ChildClass2(MainClass):

    def abstract_method(self):
        print("I am in ChildClass2")


# obj = MainClass() --> You cannot create instance of abstract class now as an abstract method is defined in it now.
obj = ChildClass1()
obj.abstract_method()
obj = ChildClass2()
obj.abstract_method()
print()


# ======================================================================================================================

# Example 3 - Python Abstract Class with abstract method implemented

class Parent(ABC):

    # Concrete Method
    def common_method(self):
        print("This is common method and will be common to all derived/child classes")

    # Abstract method
    @abstractmethod
    def abstract_method(self):
        print("This is abstract method defined and implemented also inside abstract method which can be invoked using "
              "super")


class Child1(Parent):

    def abstract_method(self):
        super().abstract_method()


class Child2(Parent):

    def abstract_method(self):
        print("I am in Child2")


# obj = Parent()

obj = Child1()
obj.abstract_method()  # <-- By usig super(), we are invoking abstract method of abstract class
obj = Child2()
obj.abstract_method()
print()


# ======================================================================================================================


# Example 4 - Not Implementing all abstract methods

class Greetings(ABC):

    def common(self):
        print("Common to all child class and can be overridden")

    @abstractmethod
    def vary1(self):
        pass

    @abstractmethod
    def vary2(self):
        pass


class Night(Greetings):

    def vary2(self):
        print("Sweet Dreams!!")


# obj = Night()  <-- This will throw error because vary1 is not implemented in Class Night. Therefore, all abstract
# methods must me implemented in all the derived classes.
print()

# ======================================================================================================================

# Interface in Python
"""
 - An Interface should just provide the method names without method bodies. Subclasses should provide implement for all
 the methods defined in an interface.
 
 - In python you can crate an interface using abstract class. If you crate an abstract class which contains only 
   abstract methods acts as an interface in python.
 
"""


class Payment(ABC):

    @abstractmethod
    def payment_method(self):
        pass


class InternetBanking(Payment):

    def payment_method(self):
        print("Payment was made via Internet banking")


class MobileBanking(Payment):

    def payment_method(self):
        print("Payment was made via Mobile Banking")


obj = InternetBanking()
obj.payment_method()
obj = MobileBanking()
obj.payment_method()
print()
