import numpy as np
import matplotlib.pyplot as plt

'''
Arrays Created from Lists and Other Array-Like Objects
Using the np.array function , NumPy arrays can be constructed from explicit Python lists, iterable expressions,
and other array-like objects (such as other ndarray instances).
'''


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("arr1 = ", arr1)
print("arr2 = ", arr2)
print()

# ----------------------------------------------------------------------------------------------------------------------

'''
The functions np.zeros and np.ones create and return arrays filled with zeros and ones, respectively. They take, as 
first argument, an integer or a tuple that describes the number of elements along each dimension of the array.
'''

# Creating a zero array
arr3 = np.zeros((3, 3), dtype=np.int)
print("arr3 - ", arr3)
print()

# Creating a array with all element with one
arr4 = np.ones((3, 3), dtype=np.int)
print("arr4 - ", arr4)
print()

# ----------------------------------------------------------------------------------------------------------------------

'''
An array filled with an arbitrary constant value can be generated by first creating an array filled with ones and then 
multiplying the array with the desired fill value. However, NumPy also provides the function np.full that does exactly
this in one step.
'''

# Creating an array with desired fill value by using full() method

arr5 = np.full((3, 3), 5.4)
print("arr5 = ", arr5)
print()

# ----------------------------------------------------------------------------------------------------------------------

'''
An already created array(empty) can also be filled with constant values using the np.fill function , which takes an 
array and a value as arguments, and set all elements in the array to the given value. The following two methods to 
create an array therefore give the same results
'''

# Using fill() method

arr6 = np.empty((2, 3))  # Creating an uninitialized Array. It's element values changes from time to time.
print("Empty Array - ", arr6)
arr6.fill(4.5)
print("Array filled using fill function - ", arr6)
print()

# ----------------------------------------------------------------------------------------------------------------------

'''
In numerical computing it is very common to require arrays with evenly spaced values between a starting value and ending
value. NumPy provides two similar functions to create such arrays: np.arange and np.linspace. Both functions take three 
arguments, where the first two arguments are the start and end values. The third argument of np.arange is the increment,
while for np.linspace it is the total number of points in the array.
'''

# arange()

arr7 = np.arange(0, 10, 1)
print("arr7 = ", arr7)

# linspace()

arr8 = np.linspace(0, 10, 11)
print("arr8 = ", arr8)

# ----------------------------------------------------------------------------------------------------------------------

'''
The function np.logspace is similar to np.linspace , but the increments between the elements in the array are
logarithmically distributed, and the first two arguments, for the start and end values, are the powers of the optional 
base keyword argument (which defaults to 10).

'''

# logspace()

arr9 = np.logspace(0, 2, 5)
print("arr9 - ", arr9)
print()

# ----------------------------------------------------------------------------------------------------------------------

'''
The numpy.meshgrid function is used to create a rectangular grid out of two given one-dimensional arrays representing 
the Cartesian indexing or Matrix indexing. Meshgrid function is somewhat inspired from MATLAB.
'''

# meshgrid()

arr10 = np.linspace(-3, 3, 7)
arr11 = np.linspace(-2, 2, 5)
print("Creating a Meshgrid")
xx, yy = np.meshgrid(arr10, arr11)
print("All the x - axis value - ", xx)
print("All the y - axis value - ", yy)
plt.plot(xx, yy, marker='.', color='k', linestyle='none')
plt.show()
print()

# ----------------------------------------------------------------------------------------------------------------------

'''
It is often necessary to create new arrays that share properties, such as shape and data type, with another array. 
NumPy provides a family of functions for this purpose: np.ones_like, np.zeros_like, np.full_like, and np.empty_like.
'''

# ones_like(), zeroes_like() and empty_like()

arr12 = np.linspace(4, 14, 11)
print("arr12 = ", arr12)
print("np.ones_like(arr12) = ", np.ones_like(arr12))
print("np.zeros_like(arr12) = ", np.zeros_like(arr12))
print("np.empty_like(arr12) = ", np.empty_like(arr12))

# ----------------------------------------------------------------------------------------------------------------------

'''
- Matrices, or two-dimensional arrays, are an important case for numerical computing. NumPy provides functions for 
  generating commonly used matrices. In particular, the function np.identity generates a square matrix with ones on the 
  diagonal and zeros elsewhere

- The similar function numpy.eye generates matrices with ones on a diagonal (optionally offset).

- To construct a matrix with an arbitrary one-dimensional array on the diagonal, we can use the np.diag function (which
  also takes the optional keyword argument k to specify an offset from the diagonal)
'''

# identity()

arr13 = np.identity(3)
print("np.identity = ", arr13)

# eye()

arr14 = np.eye(5, k=2)
print("np.eye(5, k = 2)", arr14)

# diag()

arr15 = np.diag([1, 4, 2])
print("np.diag([1, 4, 2]) = ", arr15)
arr15 = np.diag(np.arange(1, 10, 2))
print("np.diag(np.arange(1, 10, 2)) = ", arr15)
print()

# ---------------------------------------------------------------------------------------------------------------------

'''
numpy.fromfunction() function construct an array by executing a function over each coordinate and the resulting array, 
therefore, has a value fn(x, y, z) at coordinate (x, y, z).

Syntax - numpy.fromfunction(function, shape, dtype)
'''

# fromfunction()

arr16 = np.fromfunction(lambda x, y: x+y, (3, 3), dtype=np.int)
print("arr16 using fromfunction() = \n", arr16)
print()

# ---------------------------------------------------------------------------------------------------------------------

'''
Structured Array:
Numpy’s Structured Array is similar to Struct in C. It is used for grouping data of different types and sizes. Structure
array uses data containers called fields. Each data field can contain data of any type and size. Array elements can be 
accessed with the help of dot notation.
'''

name = ['abc1', 'abc2', 'abc3', 'abc4']
age = [20, 12, 45, 34]
w = [50.5, 33.0, 80.9, 77.3]
stu_name = np.zeros(4, dtype=[('name', 'U25'), ('age', np.int), ('weight', np.float)])
print("stu_name = \n", stu_name)
stu_name['name'] = name
stu_name['age'] = age
stu_name['weight'] = w
print("stu_name = \n", stu_name)

# Trying another way
arr17 = np.array([['abc1', 20, 50.5], ['abc2', 12, 33.0]])
print("arr17 = \n", arr17)
print()
