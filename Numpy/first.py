import numpy as np

arr = np.array([
  [10, 20, 30, 40],
  [50, 60, 70, 80],
  [90, 100, 110, 120]
])

# Access one element => arr[row, column]
print(arr[1, 2])

# Get an entire row
print(arr[1])

# Get an entire column
print(arr[:, 0]) # Here : means all rows.

# Slice rows and columns => arr[row_start:row_end, column_start:column_end], The ending index is not included.
print(arr[0:2, 1:3])


# practice
print(arr[1,1]) # 60

print(arr[2])

print(arr[:, 2])

# arr[row_start:row_end, column_start:column_end]
print(arr[0:2, 1:3])
print(arr[1::, 1::])

# -----------------------------------------------
# NumPy Mathematical Operations
numbers = np.array([10, 20, 30, 40, 50])

print(numbers + 5) # Addition => Add a number to every element
print(numbers - 5) # Subtraction
print(numbers * 5) # Multiplication
print(numbers / 10) # Division

# -----------------------------------------------
# Aggregation Functions
# 1) np.sum()
print(np.sum(numbers)) # Find the total

# 2) np.mean()
print(np.mean(numbers)) # Find the average

# 3) np.min()
print(np.min(numbers)) # Find the smallest value

# 4) np.max()
print(np.max(numbers)) # Find the largest value

# 5) np.median()
print(np.median(numbers)) # Find the middle value

# 6) np.std()
print(np.std(numbers)) # Find the standard deviation 