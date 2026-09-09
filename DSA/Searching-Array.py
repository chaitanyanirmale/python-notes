#Linear Search
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

# arr = [10, 5, 25, 8, 40, 15]

# print(linear_search(arr, 40))
# print(linear_search(arr, 100))


def largest_element(arr):
  largest = float('-inf')
  largest_index = -1

  for i in range(len(arr)):
    if arr[i] > largest:
      largest = arr[i]
      largest_index = i

  return largest_index   

# print(largest_element(arr))

#Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

# arr = [10, 20, 30, 40, 50, 60, 70]
# arr = [5, 10, 15, 20, 25, 30, 35]

# print(binary_search(arr, 60))
# print(binary_search(arr, 25))
# print(binary_search(arr, 70))


#LeetCode - 1st Problem 
#Two Sum 
def two_sum(arr, target):
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] + arr[j] == target:
        return i, j

arr = [2, 7, 11, 15] 
print(two_sum(arr, 9))

#This has the time complexity O(n^2)
#Solve by using dictionary
def twoSum(self, nums, target):
  seen = {}
  for i in range(len(nums)):
    complement = target - nums[i]
    if complement in seen:
      return [seen[complement], i]
    seen[nums[i]] = i


