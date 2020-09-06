"""
Yield

- When we write a function, which should perform some operation and provide some result back, we generally use the
return statement for returning the result.
- The yield keyword in python is also used to return a value from a function(just like return) but this keyword also
  maintains the state of the local variables of the function and when the function is called again, the execution is
  started from the yield statement executed last time.
- First things first, when we use a yield statement in a function then the function is called as Generator.
- A generator generates or yields values and cannot be called like a simple function rather it is called like an
  iterable i.e. by using a loop, for example a for loop.
- When we use yield keyword to return data from a function it starts storing the states of the local variable as a
  result the overhead of memory allocation for the variable in consecutive calls is saved.
- Also, in consecutive calls the flow starts from the last yield statement executed which saves time.
- We can easily create iterable functions using yield keyword.

Generator

- A Generator is nothing but a function which returns value using the yield keyword and not using the return statement.
  It is also defined as a function which returns a generator iterator. It looks like a normal function except that it
  contains yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a
  time with the next() function.

- If we have to write a custom iterator you will have to implement the __iter__() and __next__() method, define the
  mechanism of returning the next value by maintaining the state and raise the StopIteration exception when no more
  values are left for iterating.

- Well, generator makes it super easy to create an iterator in which state is maintained, all you have to do is use the
  yield keyword to return data.

- Any function that contains the yield keyword becomes a generator and will return an iterator object which can be
  iterated over using a for loop.

"""


# Example 1
def counter_iterator(args):
    x = 0
    while x < args:
        yield x
        x += 1


print("Calling a generator = ", counter_iterator(6))

for i in counter_iterator(6):
    print(i, end=" ")
print()
print()


# Example 2
def new_generator():
    """
    In this example, we have used multiple yield statement to save the state of the execution of the function
    (or generator) new_generation() such that the next time function is called the execution begins from where it left.
    """

    n = 1
    print("First Execution...")
    yield n

    n += 1
    print("Second Execution...")
    yield n

    n += 1
    print("Third Execution...")
    yield n


x = new_generator()
print(next(x))
print(next(x))
print(next(x))


# Generator Expression are very similar to list comprehensions. Just like a list comprehension, the general exp are
# concise

print()
numbers = [1, 3, 5, 8]
square = (i**2 for i in numbers)
print(type(square))
print(list(square))
