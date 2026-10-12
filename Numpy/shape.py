import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

print(arr.shape)

# What is reshaping?
# Reshaping means changing the structure of an array without changing its elements

new_arr = arr.reshape(2, 3) 
print(new_arr)
print(new_arr.shape)

# Every NumPy array has a data type, which tells us what kind of values it stores.
print(arr.dtype)

nums = np.array([1, 2, 3, 4], dtype=float)
print(nums)
print(nums.dtype)


arr2 = np.array([10.8, 20.5, 30.9])
new_arr2 = arr2.astype(int)
print(new_arr2)


arr3 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

# Reshape it into 3 rows and 4 columns.
new_arr3 = arr3.reshape(3, 4)
print(new_arr3)

# Reshape it into 4 rows and 3 columns
new_arr3_ = arr3.reshape(4, 3)
print(new_arr3_)

# Reshape it into 2 rows using -1 for the other dimension.
print(arr3.reshape(2, -1))

# Print its data type using .dtype.
print(new_arr3_.dtype)

# Convert the array to a float type using .astype(float).
new_arr4 = arr3.astype(float)
print(new_arr4)