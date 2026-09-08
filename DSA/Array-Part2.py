#Reverse an array
arr = [1, 2, 3, 4, 5]
reversed_arr = []
for i in range(len(arr)-1, -1, -1):
  reversed_arr.append(arr[i])

print(reversed_arr)

arr.reverse()
print(arr)

#Two pointer technique
arr = [1, 2, 3, 4, 5]
left = 0 
right = len(arr) - 1
while left < right:
  arr[left], arr[right] = arr[right], arr[left]
  left += 1
  right -= 1

print(arr)

#Second Largest Element
arr = [10, 5, 20, 8, 15]
largest = float('-inf')
second_largest = float('-inf')

for num in arr:
  if num > largest:
    second_largest = largest
    largest = num
  elif num > second_largest and num != largest:
    second_largest = num

print(second_largest)

#Move zeros to the end
arr = [0, 1, 0, 3, 12]
position = 0
for i in range(len(arr)):
  if arr[i] != 0:
    arr[position], arr[i] = arr[i], arr[position]
    position += 1

print(arr)

#reverse array using two pointer
arr = [10, 20 , 30, 40, 50]
left = 0
right = len(arr) - 1
while left < right:
  arr[left], arr[right] = arr[right], arr[left]
  left += 1
  right -= 1

print(arr)

#find positive and negative number
arr = [5, -2, 8, -7, 0, 3, -1]

positive = 0
negative = 0

for i in arr:
  if i > 0:
    positive += 1
  elif i < 0:
    negative += 1

print('Positve number =', positive)
print('Negative number =', negative)

#find missing number
arr = [1, 2, 4, 5]
n = 5
actual_sum = 0
expected_sum = n * (n+1)//2
for i in range(len(arr)):
  actual_sum += arr[i] 

missing_number = expected_sum - actual_sum
print('Missing number =', missing_number)