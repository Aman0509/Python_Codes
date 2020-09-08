"""
- First Class Function - First-class functions means that the language treats functions as values – that you can assign a
  function into a variable, pass it around etc.
- Properties of First Class Function:
     - A function is an instance of the Object type.
     - You can store the function in a variable.
     - You can pass the function as a parameter to another function.
     - You can return the function from a function.
     - You can store them in data structures such as hash tables, lists etc.

- Closures - A closure is a nested function which has access to a non local variable from an enclosing function that has
  finished its execution. Three characteristics of a Python closure or when can we have closures:
    - We must have a nested function
    - The nested function must refer to a value defined in a enclosing function
    - The enclosing function must return the nested function

- Closures can be use to avoid the use of global values and provide some form of data hiding.
- Closure can also provide an object oriented solution to the problem.
- When there are few methods to be implemented in a class, closures ca provide an alternate and more elegant solutions.

- Decorators use the closure and first class function's concept.
- Decorators are very powerful and useful tool in python since it allows programmers to modify the behaviour of function
  or class.
- Decorators allow us to wrap another function in order to extend the behaviour of wrapped function, without permanently
  modifying it.
- In decorators, functions are taken as the argument into another function and then called inside the wrapper function.
- A decorator takes in a function, adds some functionality and returns it.
- We can also use multiple decorators on one function.

@deco1
@deco2
def func():
    pass

func()

This will also be equivalent to when call without using * :

func = deco1(deco2(func))

"""
import functools


# First Class Function


# Storing function in other variable and then calling it
def func1():
    print("Hello")


a = func1
a()
print()


# Functions can be passed as argument to other functions

def func2(func):
    func()


func2(func1)
print()


# Function can return another function

def create_add(x):
    def add(y):
        return x + y

    return add


f = create_add(3)
print(f(4))
print()


# Closures - We will see 2 examples to understand it

# Example 1 - When nested function is called from enclosing function

def print_msg(msg):
    # msg is non local variable for function printer
    def printer():
        print(msg)

    printer()


print_msg("Hello")  # So printer() is able to access non-local variable of print_msg()
print()


# Example 2 - When enclosing function return the wrapper function

def print_msg(msg):
    # msg is non local variable for function printer
    def printer():
        print(msg)

    return printer


print_msg("Hello")()  # Now here even though 'msg' goes out of scope, it's value will be remembered by wrapper function
print()


# Decorators

#  Example 1 - Decorators without arguments

def decorator_func(function):
    def wrapper_func():
        print("Some heading".center(30, "*"))
        function()
        print("The End".center(30, "*"))

    return wrapper_func


@decorator_func
def display():
    print("Content Content Blah Blah")


# display = decorator_func(display) --> You can also call your decorated function without using @ convention
display()
print()


# Example 2 - Decorator with Arguments

def decorator_func(function, name, home):
    def wrapper_func():
        print("Some heading".center(30, "*"))
        function(name, home)
        print("The End".center(30, "*"))

    return wrapper_func


def display(name, home):
    print(f"There once was an penguin named {name} and it lives in a {home}")


display = decorator_func(display, 'Pingu', 'Igloo')
display()
print()


# Example 2 continued...

def decorator_func(function):
    def wrapper_func(*args, **kwargs):
        print("Some heading".center(30, "*"))
        function(*args, **kwargs)
        print("The End".center(30, "*"))

    return wrapper_func


@decorator_func
def display(name, home):
    print(f"There once was an penguin named {name} and it lives in a {home}")


display('Pingu', 'Igloo')
print()

# Decorators are also used with classes.

"""
When you decorate a function, it loses it's own identity in form of docstring, name etc as it wrapped by another
function. Hence, to solve this issue, you can use wraps from functools module.

"""


def logged(func):
    @functools.wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x + x


f(4)
print(f.__name__)
print(f.__doc__)
print()
