"""
- Dunder methods are those whose names starts and ends with double underscores.


Ques - Can we create our own dunder method and accordingly create a function which calls that dunder method?
Ans - We can but inventing our own dunders is highly discouraged.
"""

import datetime
import random

# Basic Example to demonstrate the Dunder method

class SomeClass:

    def __init__(self):
        print("Inside init")

    def __len__(self):
        return 1000

    def __str__(self):
        return "Someclass's object"

    def __repr__(self):
        return "SomeClass()"


obj = SomeClass()
print(len(obj))
print(obj)
print(str(obj))  # str is implicitly calling __str__() method
print(repr(obj))  # repr is implicitly calling __repr__() method
print()


# str v repr

''' 
str - The goal of str is to be readable.
repr - The goal of repr is to unambiguous and mainly used for debugging purpose.
'''
a = datetime.datetime.utcnow()
b = str(a)

print("str(a) = ", str(a))
print("str(b) = ", str(b))

print("repr(a) = ", repr(a))
print("repr(b) = ", repr(b))
print()


# __getitem__ and __setitem__

class CustomList:

    def __init__(self, num):
        self.l = [random.randrange(1, 100, 10) for _ in range(num)]

    def __setitem__(self, key, value):
        self.l[key] = value

    def __getitem__(self, key):
        return self.l[key]

    def __str__(self):
        return str(self.l)


c = CustomList(6)
print(c)
print("c[3] = ", c[3])
c[3] = 56
print(c)
for i in c:
    print(i)
print("dir(CustomList) = ", print(dir(CustomList)))
print()


# __call__

class ClassCall:

    def __init__(self, a ,b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a, self.b


obj = ClassCall(45, 21)
print(obj())
print()

# Operator Overloading
""" Python Operator enables us to use the mathematical, logical and bitwise operators on python objects just like
    primitive datatype
    
    Mathematical Operators
    + --> __add__(self, other)
    - --> __sub__(self, other)
    * --> __mul__(self, other)
    / --> __truediv__(self, other)
    // --> __floordiv__(self, other)
    % --> __mod__(self, other)
    ** --> __pow__(self, other)
    & --> __and__(self, other)
    | --> __or__(self, other)
    ^ --> __xor__(self, other)
    
    Relational Operators
    > --> __gt__(self, other)
    >= --> __ge__(self, other)
    < --> __lt__(self, other)
    <= --> __le__(self, other)
    == --> __eq__(self, other)
    != --> __ne__(self, other)
"""


class Cartesian:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Cartesian(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Cartesian(self.a - other.a, self.b - other.b)

    def __str__(self):
        string = str(self.a)
        string = string + ', ' + str(self.b)
        return string


c1 = Cartesian(3, 6)
c2 = Cartesian(7, 8)
c3 = c1 + c2
c4 = c2 - c1
print("c1 = ", c1)
print("c2 = ", c2)
print("c3 = ", c3)
print("c4 = ", c4)

