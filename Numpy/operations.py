import numpy as np

arr = np.array([40, 10, 50, 20, 30])

# Sorting arrays — np.sort()
# print(np.sort(arr))
# print(np.sort(arr)[::-1]) # reverse the sorted array

# # Finding unique values — np.unique()
# arr2 = np.array([10, 20, 10, 30, 20, 40])
# print(np.unique(arr2))

# Combining arrays — np.concatenate()
arr3 = np.array([10, 20, 30])
arr4 = np.array([40, 50, 60])

result = np.concatenate((arr3, arr4))
# print(result)


arr5 = np.array([30, 10, 40, 20, 10, 50, 30])
# Sort the array in ascending order.
print(np.sort(arr5))

# Sort it in descending order.
print(np.sort(arr5)[::-1])

# Find its unique values.
print(np.unique(arr5))

# Create two arrays, [1, 2, 3] and [4, 5, 6], and concatenate them.

arr6 = np.array([1, 2, 3])
arr7 = np.array([4, 5, 6])

result_arr = np.concatenate((arr6, arr7))
print(result_arr)