import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

# 1) Comparison Operators
# Greater than (>)
# print(arr > 30) # NumPy checks every element and returns True or False
# print(arr[arr > 30]) # This gives values (Boolean indexing)
# # Greater than or equal to (>=)

# # Less than (<)
# # Less than or equal to (<=)
# print(arr[arr < 40])

# # Equal to (==)
# print(arr[arr == 30])
# # Not Equal to (!=)
# print(arr[arr != 20])

# # Combining conditions
# print(arr[(arr > 20) & (arr < 50)]) # use & for AND
# print(arr[(arr < 20) | (arr > 50)]) # use | for OR


nums = np.array([12, 25, 8, 45, 32, 60, 18, 50])

# Find all values greater than 30.
print(nums[nums > 30])

# Find all values less than 20.
print(nums[nums < 20])

# Find all values equal to 50.
print(nums[nums == 50])

# Find all values between 20 and 50, including 20 but excluding 50.
print(nums[(nums >= 20) & (nums < 50)])

# Find all values less than 15 or greater than 45.
print(nums[(nums < 15) | (nums > 45)]) 