"""
Inheritance is the capability of one class to derive or inherit the properties from another class. The benefits of
inheritance are:

- It represents real-world relationships well.
- It provides reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add
  more features to a class without modifying it.
- It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B
  would automatically inherit from class A.

Types of Inheritance:-

- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Hierarchical Inheritance
- Hybrid Inheritance

"""


# Single Inheritance

class Employee:

    def __init__(self, id, fname, lname):
        self._id = id
        self.fname = fname
        self.lname = lname

    def email(self):
        return self.fname + '.' + self.lname + "@xyz.com"


class Department(Employee):
    """
    super() - it allows us to refer the superclass implicitly. In python 2.x versions, syntax of super was different:
    super(Parent Class name, self).__init__(variables) but from python version 3, it is defined like below as shown in
    below code
    """

    def __init__(self, id, fname, lname, dept):
        super().__init__(id, fname, lname)
        self.dept = dept

    def dept_checking(self):

        if 1 < self._id < 10:
            return f'{self.fname} {self.lname}\'s department detail is correct and his email is {self.email()}'

        elif 11 < self._id < 20:
            return f'{self.fname} {self.lname}\'s department detail is correct and his email is {self.email()}'

        else:
            return 'This ID is invalid'


obj = Department(14, 'Tom', 'Hanks', 'Finance')
print(obj.dept_checking())
obj = Department(23, 'Keanu', 'Reeves', 'IT')
print(obj.dept_checking())
print()


# Multiple Inheritance

# Example 1

class ClassA:

    def methodA(self):
        print("method A of classA")


class ClassB:

    def __methodB(self):
        print("method B of classB")


class ClassC(ClassA, ClassB):
    pass


c = ClassC()
c.methodA()
c._ClassB__methodB()
print()


# Example 2

class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    pass


obj = Class4()
obj.m()  # When you call obj.m() (m on the instance of Class4) the output is In Class2.
# If Class4 is declared as Class4(Class3, Class2) then the output of obj.m() will be In Class3.
print()


# Example 3 - Method Resolution Order(MRO) - When we search for an attribute in a class that is involved in python
# multiple inheritance, an order is followed. First, it is searched in the current class, if not found, the search moves
# to parent class. This is left-to-right, depth first.
# To get MRO of a class, you can either use the __mro__ attribute or mro() method
# __mro__ returns a tuple and mro() returns list


class X: pass;


class Y: pass;


class Z: pass;


class A(X, Y): pass;


class B(Y, Z): pass;


class M(B, A, Z): pass;


print(M.mro())
print(M.__mro__)
print()


# Multilevel Inheritance - When one class inherits from another, which in turn inherits from another.

class A1:
    x = 1


class A2(A1):
    pass


class A3(A2):
    pass


obj = A3()
print(obj.x)


# Hierarchical Inheritance - When more than one class inherits from a class.

class A2:
    pass


class A3(A2):
    pass


class A4(A2):
    pass


print(issubclass(A3, A2))
print(issubclass(A4, A2))


# Hybrid Inheritance - When it is a combination of any 2 kind of inheritance.

