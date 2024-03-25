import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Creating Arrays With a Defined Data Type
arr1 = np.array([1, 2, 3, 4], dtype='S')
print(arr1.dtype)

# For i, u, f, S and U we can define size as well.
arr2 = np.array([1, 2, 3, 4], dtype='i4')  # an array with data type 4 bytes integer:
print(arr2.dtype)

# Change data type from float to integer by using 'i' as parameter value:
arr3 = np.array([1.1, 2.2, 3.3, 4.4])
newarr = arr3.astype('i')  # or we can use arr3.astype(int)
print(arr3)
print(newarr)
