"""
Iterators and Iterables

- Iterable is an object capable of returning its members one by one. Said in other words, an iterable is anything that
  you can loop over with a 'for' loop in python.
- Python's for loop doesn't use indices for looping.
- An iterator is an object representing a stream of data. You can create an iterator object by applying the iter() built
  in function to an iterable.
- So you can tell if something is iterable then it needs to have special method called __iter__(). You can the same
  using dir() function.
- And to identify that something is iterator then it needs to have __iter__() as well as __next__() methods.
- Iterator Protocol
    The iterator objects are required to support the following two methods, which together form the iterator protocol:
    - iterator.__iter__(): Return the iterator object itself. This is required to allow both containers (also called
     collections) and iterators to be used with the ‘for’ and ‘in’ statements. Remember, if an object has special
     method __iter__ in it, then, it is iterable. Check with dir().
    - iterator.__next__(): Return the next item from the container. If there are no more items, raise the StopIteration
    exception.

- Iterators are lazy because that don't work until we ask them for their next item.
- for loop in python works by calling iter() and next() function in background.
- Python has many built-in classes/functions that are iterables:
    - enumerate
    - reversed
    - zip
    - map
    - filter
    - file objects etc

"""

# Example 1

try:
    l = [1, 2, 4, 5]
    print("l = ", l)
    print("dir(l) {look for iter special method} = ", dir((l)))
    temp = iter(l)
    print("iter(l) {look for iter and next special method} = ", temp)
    print("dir(iter(l)) = ", dir(temp))
    print("1 - next(iter(l)) = ", next(temp))
    print("2 - next(iter(l)) = ", next(temp))
    print("3 - next(iter(l)) = ", next(temp))
    print("4 - next(iter(l)) = ", next(temp))
    print("5 - next(iter(l)) = ", next(temp))

except StopIteration as er:
    print(f"\nYou've ran out of elements")

print()


# Example 2 - Creating a custom iterator class

class CustomIterator:

    def __init__(self, a_min, a_max, step=1):
        self.a_min = a_min - step
        self.a_max = a_max
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.a_min >= self.a_max:
            raise StopIteration
        else:
            self.a_min += self.step
            return self.a_min


obj = CustomIterator(100, 110, 5)
print(obj)
print(list(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

for i in obj:
    print(i)




