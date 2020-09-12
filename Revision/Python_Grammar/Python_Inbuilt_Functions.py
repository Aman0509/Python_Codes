r"""
Python Inbuilt functions are:
1 - abs()               11 - chr()              21 - eval()         31 - help()         41 - len()
2 - all()               12 - classmethod()      22 - exec()         32 - hex()          42 - list()
3 - any()               13 - compile()          23 - filter()       33 - id()           43 - locals()
4 - ascii()             14 - complex()          24 - float()        34 - input()        44 - map()
5 - bin()               15 - delattr()          25 - format()       35 - int()          45 - max()
6 - bool()              16 - dict()             26 - frozenset()    36 - isinstance()   46 - memoryview()
7 - breakpoint()        17 - dir()              27 - getattr()      37 - issubclass()   47 - min()
8 - bytearray()         18 - divmod()           28 - globals()      38 - iter()         48 - next()
9 - bytes()             19 - enumerate()        29 - hasattr()      39 - len()          49 - object()
10 - callable()         20 - eval()             30 - hash()         40 - list()         50 - oct()

51 - open()             61 - setattr()          71 - zip()
52 - ord()              62 - slice()            72 - __import__()
53 - pow()              63 - sorted()
54 - print()            64 - staticmethod()
55 - property()         65 - str()
56 - range()            66 - sum()
57 - repr()             67 - super()
58 - reversed()         68 - tuple()
59 - round()            69 - type()
60 - set()              70 - vars()

"""
import math

# abs(int or float)
print("abs()".center(30, "*"))
print("abs(-4) = ", abs(-4))
print("abs(4) = ", abs(4))
print("abs(-4.6) = ", abs(-4.6))
print("abs(4.6) = ", abs(4.6))
print("abs(3+6j) = ", abs(3 + 6j))
print()

# -------------------------------------------------------------------------------------

# all(iterable)
print("all()".center(30, "*"))
print("all([]) = ", all([]))
print("all([1,2,3]) = ", all([1, 2, 3]))
print("all(['a',2,0]) = ", all(['a', 2, 0]))
print("all(['a', 3, ' ']) = ", all(['a', 3, ' ']))
print("all(['a', 3, '']) = ", all(['a', 3, '']))
print()

# -------------------------------------------------------------------------------------

# any(iterable)
print("any()".center(30, "*"))
print("any([]) = ", any([]))
print("any([1,2,3]) = ", any([1, 2, 3]))
print("any(['a',2,0]) = ", any(['a', 2, 0]))
print("any(['a', 3, ' ']) = ", any(['a', 3, ' ']))
print("any(['a', 3, '']) = ", any(['a', 3, '']))
print()

# -------------------------------------------------------------------------------------

# ascii(object) - returns the printable representation of object passed in it
print("ascii".center(30, "*"))
print("ascii('¥') = ", ascii("¥"))
print("ascii('µ') = ", ascii("µ"))
print("ascii('Ë') = ", ascii("Ë"))
print("ascii('a') = ", ascii('a'))
print("ascii(1) = ", ascii(1))
print()

# -------------------------------------------------------------------------------------

# bin(int) - returns binary representation of passed integer.
print("bin()".center(30, "*"))
print("bin(23) = ", bin(23))
print("bin(-23) = ", bin(-23))
print("You can get binary of a number using format() and f{}")
print("format(23, #b) = ", format(23, '#b'))
print("format(23, #b) = ", format(23, 'b'))
print("f'{23, #b} = ", f"{23, '#b'}")
print("f'{23, #b} = ", f"{23, 'b'}")
print()

# -------------------------------------------------------------------------------------

# bool(x)
print("bool()".center(30, "*"))
print("bool('') = ", bool(''))
print("bool('a') = ", bool('a'))
print("bool(1) = ", bool(1))
print("bool(0) = ", bool(0))
print()

# -------------------------------------------------------------------------------------

# breakpoint()

# -------------------------------------------------------------------------------------

# bytearray(source, encoding, errors) & byte(source, encoding, errors)

# -------------------------------------------------------------------------------------

# callable(object)
print("callable()".center(30, "*"))
# Example 1 --> object of type which indicates callability such functions, methods
x = 'abcd'


def foo():
    print("callable")


print("callable(x) = ", callable(x))  # It's obivious that x is not callable
print("callable(foo) = ", callable(foo))  # It's a function and it is callable


# Example 2 --> A class with a __call__ method

class Test:

    def __call__(self):
        print('Hello There!')


# Suggests that the Test class is callable
print("callable(Test) = ", callable(Test))

# This proves that class is callable
obj = Test()
obj()


# Example 3 --> Class defined without a __call__ method

class Test1:

    def test_method(self):
        print('Hello There Again !')


# Suggests that the Geek class is callable
print("callable(Test) = ", callable(Test))

# This will throw error
# obj1 = Test1()
# obj1()
print()

# -------------------------------------------------------------------------------------

# chr(int)
print("chr()".center(30, "*"))
print('chr(45) = ', chr(45))
print('chr(113) = ', chr(113))
print('chr(1200) = ', chr(1200))
print()

# -------------------------------------------------------------------------------------

# classmethod()

# -------------------------------------------------------------------------------------

# compile(source, filename, mode, flags = 0, dont_inherit=False, optimize=-1)
print("compile()".center(30, "*"))
code_in_string = 'a = 5\nb = 6\ns = a+b\nprint("s = ", s)'
code_in_object = compile(code_in_string, 'sum', 'exec')
exec(code_in_string)

with open('code_file', 'r') as f_read:
    f = f_read.read()
    code_in_object_2 = compile(f, 'code_file', 'exec')
    exec(code_in_object_2)
print()

# -------------------------------------------------------------------------------------

# complex(real, imaginary)
print("complex()".center(30, '*'))
print("complex(5, 6) = ", complex(5, 6))
print("complex(1) = ", complex(1))
print("complex() = ", complex())
print("complex('2+9j') = ", complex('2+9j'))  # If you're passing complex no as string, no need to pass 2nd arg
print()

# -------------------------------------------------------------------------------------

# delattr(object, name)
print("delattr()".center(30, "*"))

# Example 1
print("Example 1\n")


class SomeClass:
    a, b, c = 23, 54, 89


obj_3 = SomeClass()

print("Before deleting attribute of class")
print("obj_3.a = ", obj_3.a)
print("obj_3.b = ", obj_3.b)
print("obj_3.c = ", obj_3.c)
delattr(SomeClass, 'c')
try:
    print("After deleting attribute 'c' of class")
    print("obj_3.a = ", obj_3.a)
    print("obj_3.b = ", obj_3.b)
    print("obj_3.c = ", obj_3.c)

except AttributeError:
    print("Attribute c has been deleted")

# Example 2
print("\nExample 2\n")


class SomeClass1:
    x = 'I'
    y = 'Am'
    z = 'Batman'

    def __init__(self):
        self.x = 'I'
        self.y = 'Am'
        self.z = 'Ironman'


obj_2 = SomeClass1()
print("Before deleting attribute of class")
print("obj_2.x = ", obj_2.x)
print("obj_2.y = ", obj_2.y)
print("obj_2.z = ", obj_2.z)
delattr(obj_2, 'z')  # Look closely, I am deleting the instance variable here and not the class variable
try:
    print("After deleting attribute 'z' of class")
    print("obj_2.x = ", obj_2.x)
    print("obj_2.y = ", obj_2.y)
    print("obj_2.z = ", obj_2.z)

except AttributeError:
    print("Attribute z has been deleted")
print()

# -------------------------------------------------------------------------------------

# dict() and dir()

# -------------------------------------------------------------------------------------

# divmod(number1, number2)
print("divmod()".center(30, "*"))
print("divmod(24, 7) = ", divmod(24, 7))
print("divmod(7.5, 2.5) = ", divmod(7.5, 2.5))
print()

# -------------------------------------------------------------------------------------

# enumerate(iterable, start = 0)
print("enumerate()".center(30, "*"))
print("enumerate([1,5,3,8,9], start = 'a') = ", enumerate([1, 5, 3, 8, 9], start=100))
print("list(enumerate([1,5,3,8,9], start = 'a')) = ", list(enumerate([1, 5, 3, 8, 9], start=100)))
print()

# -------------------------------------------------------------------------------------

# eval(expression, globals, locals)
print("eval()".center(30, "*"))
a_global = 34
eval('print("1000+23 =", 1000+23)')
eval('print(a_global)', {'__builtins__': None, 'print': print, 'a_global': a_global})
exec('print(a_global)', {'__builtins__': None, 'print': print, 'a_global': a_global})


def func1():
    import math
    a_local = 34
    print('Inside Function')
    eval('print(dir())', {'print': print}, {'sqrt': math.sqrt, 'pow': math.pow, 'a_local': a_local})
    exec('print(dir())', {'print': print}, {'sqrt': math.sqrt, 'pow': math.pow, 'a_local': a_local})


func1()
print()

# ------------------------------------------------------------------------------------

# exec(object, globals, locals)
""" exec's working is same as eval but there are 2 differences:
    - eval is used to evaluate a single dynamically generated Python Expression and exec is used to execute dynamically
      generated Python Code
    - eval returns the value of given expression whereas exec ignores the return value from its code and always returns 
      None """
print("exec()".center(30, '*'))
code = '''tmp_a, tmp_b = 34,78\nprint('tmp_a+tmp_b = ', tmp_a+tmp_b)'''
exec(code)
print()

# ------------------------------------------------------------------------------------

# filter(function, sequence)
print("filter()".center(30, '*'))
tmp_list = [133, 353, 8655, 133, 223, 65, 580]
print(f"Number divisible by 5 in this {tmp_list} = ", list(filter(lambda i: i % 5 == 0, tmp_list)))
print()
# ------------------------------------------------------------------------------------

# float(), format() and frozenset()

# ------------------------------------------------------------------------------------

# getattr(object, name, default)
print("getattr".center(30, "*"))


# Example 1


class TempClass:
    name = 'XYZ'
    age = '30'
    job = 'IT'


print("getattr(TempClass, 'age', 'Not found') = ", getattr(TempClass, 'age', 'Not found'))
print("getattr(TempClass, 'addr', 'Not found') = ", getattr(TempClass, 'addr', 'Not found'))


# Example 2


class TempClass2:
    name = 'XYZ'
    age = '30'
    job = 'IT'

    def __init__(self):
        self.name = 'DEF'
        self.age = '23'
        self.addr = 'India'


temp_obj = TempClass2()
print("getattr(temp_obj, 'age', 'Not found') = ", getattr(temp_obj, 'age', 'Not found'))
print("getattr(temp_obj, 'addr', 'Not found') = ", getattr(temp_obj, 'addr', 'Not found'))
print("getattr(temp_obj, 'job', 'Not found') = ", getattr(temp_obj, 'job', 'Not found'))
print()

# ------------------------------------------------------------------------------------

# globals()
""" The global methods returns the dictionary of the current global symbol table.
    A symbol table is a data structure maintained by a compiler which contains all
    necessary information about the program.
"""
print("globals()".center(30, '*'))
print(globals())
print("globals()['a_global'] = ", globals()['a_global'])
print()

# ------------------------------------------------------------------------------------

# hasattr(object, name)
# Using class TempClass2 to demonstrate this function
print("hasattr()".center(30, '*'))
print("hasattr(temp_obj, 'job') = ", hasattr(temp_obj, 'job'))
print("hasattr(temp_obj, 'sex') = ", hasattr(temp_obj, 'sex'))
print()

# ------------------------------------------------------------------------------------

# hash(object) --> Only immutable objects can be hashed such as bool, int, long, float, string, unicode, tuple

# hex(int) and hex.float(float)
print("hex() and float.hex()".center(30, '*'))
print("hex(34) = ", hex(34))
print("hex(-34) = ", hex(-34))
print("float.hex(34.56) = ", float.hex(34.56))
print("type(hex(34)) = ", type(hex(34)))
print()

# ------------------------------------------------------------------------------------

# input(prompt), int(number or string, base)

# ------------------------------------------------------------------------------------

# isinstance(object, classinfo)
# Using SomeClass2 for demo
print("isinstance()".center(30, "*"))
print("isinstance(temp_obj, TempClass2) = ", isinstance(temp_obj, TempClass2))
print()

# ------------------------------------------------------------------------------------

# issubclass(object, classinfo) --> Note that a class is called as subclass of itself
print("issubclass()".center(30, "*"))


class ParentClass:

    def __init__(self):
        print("It's a parent class")


class ChildClass(ParentClass):
    pass


print("issubclass(ParentClass, ParentClass) = ", issubclass(ParentClass, ParentClass))
print("issubclass(ParentClass, ChildClass) = ", issubclass(ParentClass, ChildClass))
print("issubclass(ChildClass, ParentClass) = ", issubclass(ChildClass, ParentClass))
print()

# ------------------------------------------------------------------------------------

# locals()
"""It returns the dictionary of current local symbol table"""
print("locals()".center(30, '*'))


def demo1():
    print("Local variable present in the demo1() = ", locals())


def demo2():
    var_temp = "Hello World"
    print("Local variable present in the demo2() = ", locals())


demo1()
demo2()
print()

# ------------------------------------------------------------------------------------

# map(function, iterable)
print("map()".center(30, "*"))
print("map(lambda x: x**2, (3,5,7,9)) = ", list(map(lambda x: x ** 2, (3, 5, 7, 9))))
print("map(math.sqrt, [4,9,16,25,36,49]) = ", list(map(math.sqrt, [4, 9, 16, 25, 36, 49])))
print()

# ------------------------------------------------------------------------------------

# max(iterable, *iterables, key, default) and max(arg1, arg2, *args, key)
print("max()".center(30, "*"))
print("max([32, 43, 12, 65]) = ", max([32, 43, 12, 65]))
print("max(32, 43, 12, 65) = ", max(32, 43, 12, 65))
print()

# ------------------------------------------------------------------------------------

# memoryview(obj)

# ------------------------------------------------------------------------------------

# min(iterable, *iterables, key, default) and max(arg1, arg2, *args, key)
print("min()".center(30, "*"))
print("min([32, 43, 12, 65]) = ", min([32, 43, 12, 65]))
print("min(32, 43, 12, 65) = ", min(32, 43, 12, 65))
print()

# ------------------------------------------------------------------------------------

# next(iterator, default), object()

# ------------------------------------------------------------------------------------

# oct(number)
print("oct()".center(30, "*"))
print("oct(40) = ", oct(40))
print("oct(-40) = ", oct(-40))
print()

# ------------------------------------------------------------------------------------

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# ------------------------------------------------------------------------------------

# ord(charater)
print("ord()".center(30, "*"))
print("ord('w') = ", ord('w'))
print("ord('3') = ", ord('3'))
print()

# ------------------------------------------------------------------------------------

# pow(x, y, z) --> x = a number, the base ; y = a number, the exponent ; z(optional) = a number, used for modulus
print("pow()".center(30, "*"))
print("pow(4, 5) = ", pow(4, 5))
print("pow(4, 5, 2) = ", pow(4, 5, 2))
print()

# ------------------------------------------------------------------------------------

# print(), property(), range() and repr()

# ------------------------------------------------------------------------------------

# reversed(seq)
print("reversed()".center(30, "*"))
print("list(reversed(['x', 'a', 'r', 'u'])) = ", list(reversed(['x', 'a', 'r', 'u'])))
print("list(reversed([3, 6, 1, 9])) = ", list(reversed([3, 6, 1, 9])))
print()

# ------------------------------------------------------------------------------------

# round(number, ndigits)
print('round()'.center(30, "*"))
print("round(34.23221, 3) = round(34.23221, 3)")
print("round(34.23221, 3) = round(34.27)")
print()

# ------------------------------------------------------------------------------------

# set()

# ------------------------------------------------------------------------------------

# setattr(object, name, value)
print("setattr()".center(30, "*"))


# Example 1
class Person:
    name = "Hello"


p = Person()
print("Before Modification - ", p.name)
setattr(p, 'name', 'World')
print("After Modification - ", p.name)


# Example 2
class Person1:
    name = "Hello"


p = Person()

setattr(p, 'name', 'World')
print("After Modification, Name is - ", p.name)

setattr(p, 'age', 32)
print("age attribute is not there but it is set using setattr() - ", p.age)
print()

# ------------------------------------------------------------------------------------

# slice(start, stop, step) -->  It returns a slice object that can use the to slice any sequence like list, tuple etc
print("slice".center(30, "*"))
print("slice(5) = ", slice(5))
print("slice(1, 5, 1) = ", slice(1, 5, 1))
print("[13, 34, 65, 1234, 4356, 545, 17, 854][slice(5)] = ", [13, 34, 65, 1234, 4356, 545, 17, 854][slice(5)])
print("[13, 34, 65, 1234, 4356, 545, 17, 854][slice(1, 5, 1)] = ", [13, 34, 65, 1234, 4356, 545, 17, 854][slice(1, 5, 1)])
print()

# ------------------------------------------------------------------------------------

# sorted(iterable, key=None, reverse=False)
print("sorted()".center(30, '*'))
print("sorted([93, 432, 1, 23, 97, 43]) = ", sorted([93, 432, 1, 23, 97, 43]))
print("sorted([93, 432, 1, 23, 97, 43], reverse=True) = ", sorted([93, 432, 1, 23, 97, 43], reverse=True))
print("sorted([[1, 3, 5], ('a', 'b', 'c', 'd'), {332, 'a', 12, 'd'}], key=len) = ", sorted([[1, 3, 5], ('a', 'b'), {332, 'a', 12, 'd'}], key=len))
print()

# ------------------------------------------------------------------------------------

# staticmethod() and str()

# ------------------------------------------------------------------------------------

# sum(iterable, start)
print("sum()".center(30, "*"))
print("sum((134, 45.8, 313, 1000.54)) = ", sum((134, 45.8, 313, 1000.54)))
print("sum([1, 2, -6], 10) = ", sum([1, 2, -6], 10))
print()

# ------------------------------------------------------------------------------------

# super(), tuple(), and type()

# ------------------------------------------------------------------------------------

# vars(object)
print("vars()".center(30, "*"))
print("vars(TempClass2) = ", vars(TempClass2))
print("vars(temp_obj) = ", vars(temp_obj))
print()

# ------------------------------------------------------------------------------------

# zip(*iterables) --> it takes 0 or more iterables, aggregates them in a tuple and return it.
print("zip()".center(30, "*"))
print("zip([1, 2, 3]('a', 'b', 'c')) = ", zip([1, 2, 3], ('a', 'b', 'c')))
print("zip([1, 2, 3]('a', 'b', 'c')) = ", list(zip([1, 2, 3], ('a', 'b', 'c'))))
print("zip([1, 2, 3]('a', 'b')) = ", list(zip([1, 2, 3], ('a', 'b'))))
z = zip([1, 2, 3], ['a', 'b', 'c'], ['$', '#', '*'])
z1, z2, z3 = zip(*z)  # Unzipping
print("z = zip([1, 2, 3], ['a', 'b', 'c'], ['$', '#', '*'])")
print("z1, z2, z3 = zip(*z)")
print("z1 = ", z1)
print("z2 = ", z2)
print("z3 = ", z3)
print()

# ------------------------------------------------------------------------------------

# __import__()

# ------------------------------------------------------------------------------------
