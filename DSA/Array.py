#An array is a collection of elements stored in an ordered manner.
arr = [10, 20, 30, 40, 50]

#Accessing an Array Element
print(arr[0])
print(arr[2])
print(arr[4])

#Traversing an Array
for num in arr:
  print(num)

#Index-based traversal
for i in range(len(arr)):
  print(arr[i])

#Updating an Element
arr[2] = 100
print(arr)

#Adding Elements
arr.append(40)
print(arr)

#Inserting an Element
arr.insert(2, 25)
print(arr)

#Deleting an Element
arr.pop(1)
print(arr)

#Searching in an Array
arr = [10, 25, 7, 40, 15]
target = 40

for num in arr:
  if num == target:
    print("Found")
    break

#Function
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

arr = [10, 25, 7, 40, 15]
result = linear_search(arr, 40)
print(result)

#Sum of Array
arr = [5, 10, 15, 20]
total = 0
for i in range(len(arr)):
  total += arr[i]

print(result)

#Count even numbers
arr = [2, 7, 4, 9, 6, 11]
count = 0

for i in arr:
  if i % 2 == 0:
    count += 1

print(count)

#Find Minimum 
arr = [8, 3, 10, 2, 6]
minimum = arr[0]
for i in arr:
  if i < minimum:
    minimum = i

print(minimum)

#Count Occurrences
arr = [2, 5, 2, 8, 2, 9, 5]
target = 2
count = 0
for i in arr:
  if i == target:
    count += 1

print(count)

#Find the index of the first occurrence
arr = [4, 7, 2, 7, 9, 7, 1]
target = 7

def first_occurrence(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1
