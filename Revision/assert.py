"""
- Assert is a debugging tool. If it finds the condition to be true, there is nothing it needs to do. So, it moves over
  to the next line of code. If not, it stops all operation and throws an AssertionError. It also shows the point of
  error.

- Assertion in python is the pythonic way of applying conditions for validations where usually if...else conditions are
  used.

- Assert statement can be defined in 2 ways:
  - assert <condition>
  - assert <condition>, <error message>

-
"""
import math


# Example 1

def func1(num):
    assert num > 0, 'Number cannot be negative!!'
    return math.sqrt(num)


print(func1(4))


# Example 2

def div(p, q):
    try:
        assert q != 0, 'Denominator cannot be negative'
        return p/q
    except AssertionError:
        return "Zero Division is not allowed!"


print(div(5, 2))
print(div(5, 0))
