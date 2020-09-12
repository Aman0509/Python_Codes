"""
- Exception - Error occurs at runtime are called as Exception.
- Whenever these types of runtime error occur, Python creates an exception object. If not handled properly, it prints a
  traceback to that error along with some details about why that error occurred.

- There is an Exception class from which all built-in, non-system-exiting exceptions are derived. All user-defined
  exceptions should also be derived from this class.

- In Python, exceptions can be handled using a try statement. A critical operation which can raise exception is placed
  inside the try clause and the code that handles exception is written in except clause.

- Remember, you can't put a statement between try and except blocks.

- except implementation:

  1 - Multiple excepts
      try:
          pass
      except TypeError:
          pass
      except ValueError:
          pass
      and so on...

  2 - Multiple Exceptions handled under one except
      try:
          pass
      except (TypeError, NameError, ZeroDivisionError):
          pass

  3 - A Generic except after all excepts. Remember, you can only define one generic except. More than one will throw
      error
      try:
          pass
      except ZeroDivisionError:
         pass
      except (ValueError, KeyError):
         pass
      except:
         # This will catch all other type of exception
         pass

- We can also forcefully raise exception using keyword raise.

- The try statement in python can have optional 'finally' clause. This clause is executed no matter what and is
  generally used to release external resources.

- In python, users can define such exceptions by creating a new class. This exception class has to be derived, either
  directly or indirectly from Exception Class. Most of the built-in exceptions are also derived form this class.
"""
import sys


# Example 1

random_list = ['x', 0, 5]
for i in random_list:
    try:
        print("Element is - ", i)
        r = 1/int(i)
        break

    except:
        print(f"This {sys.exc_info()[0]} occurred")
        print("Next Entry")

print(f"The reciprocal of {i} is ", r)
print()

# Example 2 - Raising an exception

try:
    a = int(input("Enter a positive number - "))
    if a < 0:
        raise ValueError("This is not a positive number")
except ValueError as v:
    print(v)
print()

# Example 3 - try...finally

try:
    f = open("file1.txt", 'r')
    print(f.readline(20))
finally:
    f.close()
print()


# Example 4 - try, except and else
"""
- The else clause in a try, except statement must follow all except clauses and is useful fo code that must be executed if
  the try clause does not raise an exception
- Exception in the else clause are not handled by the preceding except clauses. Make sure that else clause is run before
  the finally block
"""
try:
    a = int(input("Enter Num1 - "))
    b = int(input("Enter Num2 - "))
    c = a/b

except (ValueError, ZeroDivisionError):
    print("Some Error")

else:
    print(c)
