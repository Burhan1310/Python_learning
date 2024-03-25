import numpy as np

arr = np.array([1, 2, 3, 4, 5])  # 1-D Arrays
print(arr)
print(np.__version__)
print(type(arr))

arr1 = np.array((5, 4, 3, 2, 1))
print(arr1)

# 0-D Array
arr2 = np.array(54)
print(arr2)

# 2-D Arrays
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3)

# 3-D Arrays
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr4)

# check the dimension
print(arr4.ndim)
print(arr3.ndim)
print(arr2.ndim)
print(arr.ndim)

# An array can have any number of dimensions.
arr5 = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr5)
print('The number of  dimension : ', arr5.ndim)
