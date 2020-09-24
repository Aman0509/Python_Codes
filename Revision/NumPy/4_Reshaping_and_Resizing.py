import numpy as np

"""
For reshaping the arrays:
- numpy.reshape(array, shape, order = ‘C’) : shapes an array without changing data of array.
- numpy.ndarray.reshape()
"""

# reshape()
arr1 = np.array([[1, 2], [3, 4]])
print("arr1 = ", arr1)
print("np.reshape(arr1,(1, 4))\n", np.reshape(arr1, (1, 4)))
print("arr1.reshape(4) \n", arr1.reshape(4))
print("np.arange(12).reshape(2, -1)\n", np.arange(12).reshape(2, -1))
print()


"""
The np.ravel (and its corresponding ndarray method) is a special case of reshape, which collapses all dimensions of an 
array and returns a flattened one-dimensional array with a length that corresponds to the total number of elements in 
the original array. The ndarray method flatten performs the same function but returns a copy instead of a view.
"""

# ravel()
arr2 = np.fromfunction(lambda x, y: 2*x + y, (4, 3), dtype=np.int)
print("arr2 = \n", arr2)
print("arr2.ravel() = \n", arr2.ravel())

# flatten()
print("arr2.flatten() = \n", arr2.flatten())
print()


"""
it is also possible to introduce new axes into an array, either by using np.reshape or, when adding new empty axes, 
using indexing notation and the np.newaxis keyword at the place of a new axis.
"""

# newaxis
arr3 = np.arange(0, 8)
arr4 = np.arange(9, 18)
print("arr3 \n", arr3)
print("arr4 \n", arr4)
print("arr3[:, np.newaxis] \n", arr3[:, np.newaxis], arr3.shape)
print("arr4[np.newaxis, :] \n", arr4[np.newaxis, :], arr4.shape)
print()


"""
The function np.expand_dims can also be used to add new dimensions to an array, and in the preceding example, the 
expression data[:, np.newaxis] is equivalent to np.expand_dims(data, axis=1), and data[np.newaxis, :] is equivalent to
np.expand_dims(data, axis=0). Here the axis argument specifies the location relative to the existing axes where the new 
axis is to be inserted.
"""

# expand_dims()
print("np.expand_dims(arr3, axis=1) \n", np.expand_dims(arr3, axis=1))
print("np.expand_dims(arr4, axis=0) \n", np.expand_dims(arr4, axis=0))
print()


"""
numpy.squeeze() function is used when we want to remove single-dimensional entries from the shape of an array.
"""

# squeeze()
arr5 = np.arange(1, 10).reshape(1, 3, 3)
print("arr5 = \n", arr5)
print("np.squeeze(arr5, axis = 0) = \n", np.squeeze(arr5, axis=0))
print()


"""
With the help of numpy.transpose(), We can perform the simple function of transpose within one line by using 
numpy.transpose() method of Numpy. It can transpose the 2-D arrays on the other hand it has no effect on 1-D arrays.
"""

# transpose()
arr6 = np.array([[4, 5, 6], [9, 8, 6]])
print("arr6 = \n", arr6)
print("np.transpose(arr6) = \n", np.transpose(arr6))
print()


"""
In addition to reshaping and selecting subarrays, it is often necessary to merge arrays into bigger arrays, for example,
when joining separately computed or measured data series into a higher-dimensional array, such as a matrix. For this
task, NumPy provides the functions np.vstack, for vertical stacking of, for example, rows into a matrix, and np.hstack 
for horizontal stacking of, for example, columns into a matrix. The function np.concatenate provides similar 
functionality, but it takes a keyword argument axis that specifies the axis along which the arrays are to be 
concatenated.
"""

# vstack() and hstack()

arr7 = np.arange(33, 41)
print("arr7 = \n", arr7)
print("np.vstack(arr7, arr7, arr7) = \n", np.vstack((arr7, arr7, arr7)))
print("np.hstack(arr7, arr7, arr7) = \n", np.hstack((arr7, arr7, arr7)))

# To make np.hstack treat the input arrays as columns and stack them accordingly, we need to make the input arrays
# two-dimensional arrays of shape (1, 5) rather than one-dimensional arrays of shape (5,). We can insert a new axis by
# indexing with np.newaxis

arr7_1 = arr7[:, np.newaxis]
print("np.hstack(arr7, arr7, arr7) = \n", np.hstack((arr7_1, arr7_1, arr7_1)))

# concatenate()
print("np.concatenate((arr7, arr7, arr7), axis = 0) = \n", np.concatenate((arr7, arr7, arr7), axis=0))







