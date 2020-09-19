"""
- Array in Numpy is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive
  integers. In Numpy, number of dimensions of the array is called rank of the array.A tuple of integers giving the size
  of the array along each dimension is known as shape of the array. An array class in Numpy is called as ndarray.
  Elements in Numpy arrays are accessed by using square brackets and can be initialized by using nested Python Lists.
"""

import numpy as np

# Creating 1D Array

arr1 = np.array([1, 2, 3, 5])
print("Your 1D Array is - ", arr1)
print("Type of 1D Array - ", type(arr1))
print()

# Creating 2D Array

arr2 = np.array([[5, 7, 1], [6, 2, 9]])
print("Your 2D Array is - ", arr2)
print("Type of 2D Array - ", type(arr2))
print()

# When length of column and row are not same, then it will create 1D Array. It's throwing error. Need to check

# arr3 = np.array([[5, 7, 1], [2, 9]], dtype=np.int)
# print("Your Array is - ", arr3)
# print("Type of Array - ", type(arr3))


# Attributes of ndarray class. We will take arr2 to demonstrate attributes.

print("arr2.shape = ", arr2.shape)
print("arr2.size = ", arr2.size)
print("arr2.ndim = ", arr2.ndim)
print("arr2.nbytes = ", arr2.nbytes)
print("arr2.dtype = ", arr2.dtype)
print("arr2.strides = ", arr2.strides)
print()


# The following example demonstrates how to use the dtype attribute to generate arrays of integer-, float-, and
# complex-valued elements:

arr3 = np.array([1, 2, 3], dtype=np.int)
arr4 = np.array([1, 2, 3], dtype=np.float)
arr5 = np.array([1, 2, 3], dtype=np.complex)
print("np.array([1, 2, 3], dtype=np.int) = ", arr3)
print("np.array([1, 2, 3], dtype=np.float) = ", arr4)
print("np.array([1, 2, 3], dtype=np.complex) = ", arr5)
print()


# Once a NumPy array is created, its dtype cannot be changed, other than by creating a new copy with type-casted array
# values. Typecasting an array is straightforward and can be done using either the np.array function or by using astype
# method of ndarray class

print("arr4 = ", arr4)
print("arr4.dtype = ", arr4.dtype)
print("Changing the dtype of arr4...")
print("arr4 = np.arr4(arr4, dtype=np.int)")
arr4 = np.array(arr4, dtype=np.int)
print("arr4 = ", arr4)
print("arr4.dtype = ", arr4.dtype)
print("\nChanging the dtype using astype() method...")
print("arr4.astype(dtype=np.float) = ", arr4.astype(dtype=np.float))
print()






