# What is numpy -> NumPy = Numerical Python
# It is a python library designed for working with numbers, arrays, mathematical operations, and large amounts of data.

# The important difference is that NumPy gives us a powerful array structure that is designed for numerical computation.

import numpy as np

numbers = np.array([10, 20, 30, 40])

# print(numbers)
# print(numbers + 5)

# A NumPy array is similar to a Python list, but it is designed for fast numerical operations.

# print(numbers * 2)
# print(numbers + 10)
# print(numbers - 5)
# print(numbers / 2)

# Accessing elements
# Just like Python lists, NumPy uses indexing.

# print(numbers[0])
# print(numbers[1])
# print(numbers[2])

# Slicing => You can select multiple elements:  [start : stop] The stop index is not included.
# print(numbers[1:4])


values = np.array([5, 10, 15, 20, 25, 30])

# print(values)  # Print the array.
# print(values[0]) # Print the first element.
# print(values[-1:])  # Print the last element.
# print(values[2:5])  # Print 15, 20, 25.
# print(values * 3)  # Multiply every element by 3.

# NumPy Dimensions and Shape
# print(values.ndim)

# 2D array
arr = np.array([
  [10, 20, 30],
  [40, 50, 60]
])
# print(arr.ndim)
# print(arr.shape)

# 3D array
arr2 = np.array([
  [
    [1, 2, 3],
    [4, 5, 6]
  ],
  [
    [7, 8, 9],
    [10, 11, 12]
  ]
])

# print(arr2.ndim)  # Number of dimensions
# print(arr2.shape) # Size of each dimension
# print(arr2.size)  # Total number of elements

# 2 blocks
#   ↓
# 2 rows in each block
#   ↓
# 3 columns in each row

arr3 = np.array([
  [10, 20, 30, 40], # First row  → index 0
  [50, 60, 70, 80], # Second row → index 1
  [90, 100, 110, 120] # Third row  → index 2
])

# print(arr3.ndim)
# print(arr3.shape)
# print(arr3.size)  
# print(arr3[1,2]) # [row, col] => The value 70 
# print(arr3[1]) # The second row


# NumPy Array Creation Functions
# np.zeros() => Creates an array filled with 0.
# arr4 = np.zeros(5)
# print(arr4)

# # np.ones() => Creates an array filled with 1
# arr5 = np.ones(5)
# print(arr5)
# # 2D array
# arr6 = np.ones((2, 3))
# print(arr6)

# # np.arange() => Creates numbers within a given range. syntax = np.arange(start, stop, step)
# arr7 = np.arange(1, 10)
# print(arr7)
# arr8 = np.arange(2, 11, 2) # added step
# print(arr8)

# # np.linspace() => This one is slightly different. It creates a specified number of evenly spaced values.
# arr9 = np.linspace(0, 10, 5)
# print(arr9)

# practice
# 1. Create an array of 6 zeros.
question1 = np.zeros(6)
print(question1)

# 2. Create a 3 × 4 array of ones.
question2 = np.ones((3,4))
print(question2)

# 3. Create numbers from 10 to 20.
question3 = np.arange(10, 21)
print(question3)

# 4. Create even numbers from 2 to 20.
question4 = np.arange(2, 21, 2)
print(question4)

# 5. Create 5 evenly spaced numbers between 0 and 100.
question5 = np.linspace(0, 100, 5)
print(question5)