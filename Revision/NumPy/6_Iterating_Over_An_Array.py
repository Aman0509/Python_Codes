import numpy as np

'''
In general, numpy arrays can be iterate like list
'''

# Iterating over 1D Array

arr1 = np.arange(1, 10)**2
print("arr1 \n", arr1)
for i in arr1:
    print(i)
print()

# Iterating over 2D Array

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("arr2 \n", arr2)
print()
c = 0
for j in arr2:
    print("Row "+str(c)+":", j)
    c += 1
print()

'''
NumPy package contains an iterator object numpy.nditer. It is an efficient multidimensional iterator object using which
it is possible to iterate over an array. Each element of an array is visited using Python’s standard Iterator interface.
'''

# Iteration order will follow 'K' order

arr3 = np.arange(9).reshape(3, 3)
print("arr3 \n", arr3)
# Remember, by default, iteration order will be row wise
print("Iterating using nditer() - \n")
for i in np.nditer(arr3):
    print(i)
print()

# Iteration order will follow 'F' order

arr4 = np.arange(9).reshape(3, 3)
# In order to iterate column wise, create a transpose matrix
arr4 = arr4.T
print("arr4 \n", arr4)
print("Iterating using nditer() - \n")
for i in np.nditer(arr4):
    print(i)
print()


'''
There are times when it is important to visit the elements of an array in a specific order, irrespective of the layout 
of the elements in memory. The nditer object provides an order parameter to control this aspect of iteration. The 
default, having the behavior described above, is order=’K’ to keep the existing order. This can be overridden with 
order=’C’ for C order and order=’F’ for Fortran order.
'''

print("Iterating arr3 with order C")
for i in np.nditer(arr3, order='C'):
    print(i)
print()

print("Iterating arr3 with order F")
for i in np.nditer(arr3, order='F'):
    print(i)
print()


'''
Modifying Array Values:
The nditer object has another optional parameter called op_flags. Its default value is read-only, but can be set to 
read-write or write-only mode. This will enable modifying array elements using this iterator.
'''

arr5 = np.arange(1, 9).reshape(2, 4)
print("arr5 = \n", arr5)
for i in np.nditer(arr5, op_flags=['readwrite']):
    i[...] = i**2
print("Modified Array arr5 using op_flags parameter is\n", arr5)
print()

'''
External Loop:
The nditer class constructor has a flags parameter, which can take the following values
'''

print("printing with order = C")
for x in np.nditer(arr5, flags=['external_loop'], order='C'):
    print(x)
print()

print("printing with order = F")
for x in np.nditer(arr5, flags=['external_loop'], order='F'):
    print(x)
print()


'''
Broadcasting Iteration:
If two arrays are broadcastable, a combined nditer object is able to iterate upon them concurrently. Assuming that an
array a has dimension 3X4, and there is another array b of dimension 1X4, the iterator of following type is used (array
b is broadcast to size of a).
'''

arr6 = np.arange(12, 24).reshape(3, 4)
arr7 = np.arange(4)
print("arr6 = \n", arr6)
print("arr7 = \n", arr7)
for i, j in np.nditer([arr6, arr7]):
    print(f"{i} -- {j}")

