# What is NumPy?

# NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
# NumPy stands for Numerical Python.

#*******************************************************\
    
# importing numpy
import numpy as np


# Create a NumPy ndarray Object
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr)) #It returns the type "numpy.ndarray"


# The ndim attribute that returns an integer that tells us how many dimensions the array have.
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim) # It prints 0
print(b.ndim) # It prints 1
print(c.ndim) # It prints 2
print(d.ndim) # It prints 3


# *******************************************************************

# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

# ***********************************************************************


# A property called dtype that returns the data type of the array
arr = np.array([1, 2, 3, 4])
print(arr.dtype) # It prints int64


#  The copy property 
# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr) # It prints [42 2 3 4 5] 
print(x) # IT prints [1 2 3 4 5]


# The view property
# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr) # It prints [42 2 3 4 5]
print(x) # It prints [42 2 3 4 5]


# NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) # It prints (2,4).


