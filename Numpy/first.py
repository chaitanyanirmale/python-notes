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