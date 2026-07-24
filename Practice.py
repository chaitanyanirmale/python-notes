#Q. Reverse a string.
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

# string[start : end : step]
#------------------------------------------------

#Q. Count the number of vowels in a string.
text = input("Enter a string: ")

count = 0
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

#------------------------------------------------
#Q. Check if a string is a palindrome.
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
#------------------------------------------------
#Q. Find the second largest number in a list.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("Second largest number does not exist.")
else:
    print("Second largest number:", second_largest)

#---------------------------------------------------
#Q. Remove duplicate elements from a list.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List after removing duplicates:", unique_numbers)

#--------------------------------------------------
#Q. Count the frequency of each character in a string.
text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequencies:")
for char, count in frequency.items():
    print(char, ":", count)

#-------------------------------------------------
#Q. Merge two dictionaries.
dict1 = {
    "name": "Chaitanya",
    "age": 23
}

dict2 = {
    "city": "Pune",
    "course": "MCA"
}

merged_dict = {**dict1, **dict2}

print("Merged Dictionary:", merged_dict)

#--------------------------------------------------
#Q. Find the common elements between two lists.
list1 = list(map(int, input("Enter elements of List 1: ").split()))
list2 = list(map(int, input("Enter elements of List 2: ").split()))

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("Common elements:", common)

#--------------------------------------------------
#Q. Sort a list without using the built-in sort() method.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j] #Swaps the two elements using Python's tuple unpacking.

print("Sorted List:", numbers)

#---------------------------------------------------
#Q. Check whether two strings are anagrams
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if sorted(string1) == sorted(string2):
    print("The strings are Anagrams.")
else:
    print("The strings are Not Anagrams.")
#--------------------------------------------------
#Q. Generate the first n Fibonacci numbers.
n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
#--------------------------------------------------
#Q. Find all prime numbers between 1 and n.
n = int(input("Enter a number: "))

print("Prime numbers between 1 and", n, "are:")

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
#---------------------------------------------------
#Q. Rotate a list by k positions.

numbers = list(map(int, input("Enter elements separated by spaces: ").split()))
k = int(input("Enter the number of positions to rotate: "))

n = len(numbers)

k = k % n

rotated_list = numbers[-k:] + numbers[:-k]

print("Rotated List:", rotated_list)