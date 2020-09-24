import numpy as np

'''
- The term broadcasting refers to how numpy treats arrays with different Dimension during arithmetic operations which 
lead to certain constraints, the smaller array is broadcast across the larger array so that they have compatible shapes.
- Broadcasting provides a means of vectorizing array operations so that looping occurs in C instead of Python as we know 
  that Numpy implemented in C. It does this without making needless copies of data and which leads to efficient 
  algorithm implementations. There are cases where broadcasting is a bad idea because it leads to inefficient use of 
  memory that slow down the computation.
'''

arr1 = np.array([1, 2, 3])
print("arr1 = \n", arr1)
print("arr1 * 2 = \n", arr1 * 2)

arr2 = np.array([[4, 5, 6], [6, 7, 8]])
print("arr2 = \n", arr2)
print("arr1 + arr2 = \n", arr1 + arr2)

arr3 = np.arange(83, 85).reshape((2, 1))
print("arr3 = \n", arr3)
print("arr2 + arr3 = \n", arr2 + arr3)





