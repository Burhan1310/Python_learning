import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[2])

print(arr[1], arr[3])

# Access 2-D Arrays
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('The 2nd element on 1st row: ', arr1[0, 1])
print('5th element on 2nd row: ', arr1[1, 4])

# Access 3-D Arrays
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr2[0, 1, 2])

# Negative Indexing
print(arr2[-1, 0, -1])
