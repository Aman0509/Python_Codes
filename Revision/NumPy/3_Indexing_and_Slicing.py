import numpy as np

'''
Indexing and Slicing operations are same as list in 1D array
'''

arr1 = np.linspace(10, 30, 15, dtype=np.int)
print("arr1 = ", arr1)
print("arr1[3:8] = ", arr1[3:8])
print("arr1[::-1] = ", arr1[::-1])
print()

'''
Views - Sub-arrays that are extracted from arrays using slice operations are alternative views of the same underlying 
array data. That is, they are arrays that refer to the same data in the memory as the original array, but with a 
different strides configuration. When elements in a view are assigned new values, the values of the original array are 
therefore also updated.
With multidimensional arrays, element selections like those introduced in the previous section can be applied on each 
Subarrays that are extracted from arrays using slice operations are alternative views of the same underlying array 
data. That is, they are arrays that refer to the same data in the memory as the original array, but with a different 
strides configuration. When elements in a view are assigned new values, the values of the original array are therefore
also updated.
axis (dimension). The result is a reduced array where each element matches the given selection rules.
'''

arr2 = np.fromfunction(lambda x, y: x+y, (5, 6), dtype=np.int)
print("arr2 = \n", arr2)
print("arr2[:, 1] = \n", arr2[:, 1])
print("arr2[1, :] = \n", arr2[1, :])
print("arr2[:3, :3] = \n", arr2[:3, :3])
print("arr2[3:, 3:] = \n", arr2[3:, 3:])
print("arr2[::2, ::2] = \n", arr2[::2, ::2])
print()

'''
Fancy Indexing
In the previous section, we looked at indexing NumPy arrays with integers and slices, to extract individual elements or 
ranges of elements. NumPy provides another convenient method to index arrays, called fancy indexing. With fancy
indexing, an array can be indexed with another NumPy array, a Python list, or a sequence of integers, whose values 
select elements in the indexed array.
'''

arr3 = np.linspace(2, 20, 12, dtype=np.int)
print("arr3 = ", arr3)
print("arr3[np.array([4, 5, 6])] = ", arr3[np.array([4, 5, 6])])  # Array represents index
print("arr3[[0, 10, 5]] = ", arr3[[0, 10, 5]])  # List represent index
print()

'''
Boolean Indexing
In this case, each element (with values True or False) indicates whether or not to select the element from the list 
with the corresponding index. That is, if element n in the indexing array of Boolean values is True, then element n is 
selected from the indexed array. If the value is False, then element n is not selected.
'''

print("arr3 > 6 = ", arr3 > 6)
print("arr3[arr3 > 6] = ", arr3[arr3 > 6])


'''
Ellipses(...) in Indexing - If you have 2D array, it will return the all row or column of a passes column and row of array.
'''

arr4 = np.array([['IBM', 'Samsung', 'Apple'], [1911, 1938, 1976], [380000, 489000, 137000]])
print("arr4 = \n", arr4)
print("arr4[2, ...] \n", arr4[2, ...])
print("arr4[..., 1] \n", arr4[..., 1])
print()

