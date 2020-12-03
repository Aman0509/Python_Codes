#!/usr/bin/env python3


class Some:
    pass


Some.a = 5
Some.b = 'a'
print("Some.a = ", Some.a)
print("Some.b = ", Some.b)
print(vars(Some))
print(Some.__dict__)


# ----------------------------------------------------------------------------------------------------------------------


class Test:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Hello"


d = Test(3, 9)
print(d)


# ----------------------------------------------------------------------------------------------------------------------

def mem_test():
    x = 300
    y = 400
    print("id(x) = ", id(x))
    print("id(x) = ", id(y))
    print("x is y - ", x is y)


mem_test()


# ----------------------------------------------------------------------------------------------------------------------

class Test1:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = self.a + self.b

    def method(self):
        return self.a, self.b


obj = Test1("ABC", "DEF")  # Constructor is called when the object is instantiated
print(obj.c)
print(obj.method())
obj.a = "XYZ"  # Although value of 'a' is changing but it will not get updated in c because initialisation was done
# during constructor call and constructor is always call when new object is instantiated.
print(obj.a)
print(obj.c)
print(obj.method())

# ----------------------------------------------------------------------------------------------------------------------

# Fibonacci Series

a = 0
b = 1
temp = 0
num_of_ele = int(input("Enter the number of elements of Fibonacci Series - "))

if num_of_ele == 1:
    print(a)
elif num_of_ele <= 0:
    print("Enter the positive number")
else:
    print("Fibonacci Sequence:")
    while temp < num_of_ele:
        print(a)
        c = a + b
        a = b
        b = c
        temp += 1

d = {}


def fibonacci(n):
    if n in d:
        return d[n]

    if n <= 1:
        return n
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    d[n] = value
    return value


num = int(input("Enter the number of elements of Fibonacci Series - "))
if num <= 0:
    print("Zero or -ve values are not allowed")
else:
    print("Fibonacci Series")
    for i in range(num):
        print(fibonacci(i))


# ----------------------------------------------------------------------------------------------------------------------
print("\npadovan")
a, b, c = 1, 0, 0
print(a, b, c)
for i in range(3, 20):
    d = b + a
    a = b
    b = c
    c = d
    print(d)


# ----------------------------------------------------------------------------------------------------------------------
