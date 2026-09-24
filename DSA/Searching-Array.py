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
#Two Sum - Time Complexity O(n^2)
def two_sum(arr, target):
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] + arr[j] == target:
        return i, j

arr = [2, 7, 11, 15] 
# print(two_sum(arr, 9))

#This has the 
#Solve by using dictionary
def twoSum( nums, target):
  seen = {}
  for i in range(len(nums)):
    complement = target - nums[i]
    if complement in seen:
      return [seen[complement], i]
    seen[nums[i]] = i



#LeetCode - 2nd Problem 
#Contains Duplicate - Time Complexity O(n)
class Solution:
  def contain_duplicate(self, nums):
    seen = set()
    for num in nums:
      if num in seen:
        return True
      seen.add(num)
    return False

solution = Solution()
result = solution.contain_duplicate([1, 2, 3, 2])
# print(result)


#Best time to Buy and Sell Stocks
def maxProfit(prices):
  min_price = prices[0]
  max_profit = 0
  for price in prices:
    if price < min_price:
      min_price = price
    profit = price - min_price
    if profit > max_profit:
      max_profit = profit

  return max_profit

prices = [7, 1, 5, 3, 4, 6]
# print(maxProfit(prices))


def removeDuplicates(arr):
  if len(arr) == 0:
    return 0
  i = 0
  for j in range(1, len(arr)):
    if arr[j] != arr[i]:
      i += 1
      arr[i] = arr[j]
  return i + 1

arr = [0, 0, 1, 1, 2, 3, 4, 4]
# print(removeDuplicates(arr))


#Merge Sorted Arrays
def merge(nums1, m, nums2, n):
  i = m - 1
  j = n - 1
  k = m + n - 1
  while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
      nums1[k] = nums1[i]
      i -= 1
    else: 
      nums1[k] = nums2[j]
      j -= 1
    k -= 1
  while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1


# Majority Element
def majorityElement(nums):
  count = {}
  for num in nums:
    count[num] = count.get(num, 0) + 1
    if count[num] > len(nums) // 2:
      return num

nums = [2,2,1,1,1,2,2]
# print(majorityElement(nums))


# Intersection of Two Arrays
def intersection(nums1, nums2):
  set1 = set(nums1)
  set2 = set(nums2)

  return list(set1 & set2)

nums1 = [4, 9, 5]
nums2 = [4, 9, 9, 8 , 4]
# print(intersection(nums1, nums2))


# Rotate Array
def rotate(nums, k):
  k = k % len(nums)
  nums[:] = nums[-k:] + nums[:-k]
  return nums

nums_2 = [1,2,3,4,5,6,7]
# print(rotate(nums_2, 3))


# Find missing number
def missingNumber(nums):
  n = len(nums)
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(nums)
  return expected_sum - actual_sum

numbers = [1, 2, 0, 4, 5]
# print(missingNumber(numbers))


# Single Number 
def singleNumber(nums):
  result = 0
  for num in nums:
    result = result ^ num

  return result

# print(singleNumber([1, 2, 4, 1, 2]))