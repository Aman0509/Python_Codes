"""

- Most of the programming languages use the main method or function as the starting point of execution in any program.
  But what about Python? Generally, the execution of a python program(script) starts from the very first line that is at
  the indentation level 0 of that program. However, when a python program is executed, before its execution a __name__
  variable is created. This variable can be used as an alternate for the main method in python.

- __name__ variable is not available in Python 2.x version and was introduced in Python 3.0

- __name__ is a built-in variable in python that stores the name of the current module. If the current module is
  executing, then the __name__ variable contains the value __main__ otherwise it simply contains the name of the module.

- So, when a program or script is executing then its name variable will always have the value __main__ and if any python
 file is imported in any other program file then the __name__ variable stores the name of the module. Thus, it can be
 used to check whether the current script is running on its own or being imported somewhere else by combining it with
 an if conditional statement.

 - Here __main__ is just a string that is used to check if the current module is running on its own or not. In the
  __name__ variable, the double underscores on both sides of name is for indicating the python interpreter to recognize
  it as a special/reserved keyword.

"""
import Namespace_Example_2


def something():
    print("Inside 'something function' of script named as __name__Var_Examples.py")


if __name__ == "__main__":
    print("__name__Var_Examples.py is called from itself")
    print("Value of name variable is - ", __name__)
    Namespace_Example_2.outer_foo()

else:
    print("__name__Var_Examples.py is called by some another script")
    print("Value of name variable is - ", __name__)
