import numpy as np

'''
Array splitting can be vertical, horizontal, or depth-wise. We can use functions hsplit(), vsplit() and dsplit() 
respectively for the same . We can split arrays into arrays of the same shape by indicating the position after which 
the split should occur.
'''

# Splitting 1D Array

arr1 = np.arange(4, 16)
print("arr1 = \n", arr1)
print("Splitting the 1D array to produce 4 equal-sized sub-arrays")
print(np.split(arr1, 4))
print(np.split(arr1, (1, 8)))  # Splitting at index 1 and then at index 8

# Splitting 2D Array

arr2 = np.arange(20, 32).reshape(3, 4)
print("arr2 = \n", arr2)
print("Splitting the 2D array to produce 4 equal-sized sub-arrays")
print(np.split(arr2, 3))  # Splitting row wise
print("---------------------------------------------------------------------------------------------------------------")



'''
Horizontal splitting: The ‘hsplit()’ function splits an array along axis parameter = 1. ‘numpy.hsplit’ is equivalent to
‘split’ with axis parameter = 1, the array is always splitted along the second axis regardless of the array dimension. 
This function split an array into multiple sub-arrays horizontally (column-wise).
'''

print('Splitting array horizontally using hsplit() method')
print("1D Array - \n", np.hsplit(arr1, 4))
print("2D Array - \n", np.hsplit(arr2, 4))  # Splitting column-wise

# Implementing hsplit() with split()
print("Imitating the behaviour of hsplit() with split()")
print("2D Array - \n", np.split(arr2, 4, axis=1))
print("---------------------------------------------------------------------------------------------------------------")

'''
Vertical splitting: The ‘vsplit()’ function splits an array along axis parameter = 0.‘numpy.vsplit’ is equivalent to 
‘split’ with axis parameter = 0. This function split an array into multiple sub-arrays vertically (row-wise).
vsplit only works on arrays of 2 or more dimensions.
'''

print('Splitting array horizontally using vsplit() method')
print("2D Array - \n", np.vsplit(arr2, 3))  # Splitting row-wise
print("Imitating the behaviour of vsplit() with split()")
print("2D Array - \n", np.split(arr2, 3, axis=0))
print("---------------------------------------------------------------------------------------------------------------")


'''
Depth-wise splitting: It Split the array into multiple sub-arrays along the 3rd axis (depth).
'''

arr3 = np.arange(27).reshape(3, 3, 3)
print("arr3 = \n", arr3)
print('Splitting array depth-wise using dsplit() method')
print(np.dsplit(arr3, 3))
print("Imitating the behaviour of dsplit() with split()")
print(np.split(arr3, 3, axis=2))

