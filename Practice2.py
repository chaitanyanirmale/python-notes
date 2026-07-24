#Q. Write a function to check if a number is prime.
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a Prime Number.")
else:
    print(number, "is Not a Prime Number.")
#----------------------------------------------------
#Q. Write a function to calculate the GCD(Greatest Common Divisor) of two numbers.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)

print("GCD is:", result)
#----------------------------------------------------
#Q. Create a function that returns the largest element in a list
def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = find_largest(numbers)

print("Largest element:", result)
#----------------------------------------------------
#Q. Write a recursive function to compute factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter a number: "))

result = factorial(number)

print("Factorial of", number, "is", result)
#---------------------------------------------------
#Q. Write a function that counts uppercase and lowercase letters in a string.
def count_letters(text):
    uppercase = 0
    lowercase = 0

    for char in text:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1

    return uppercase, lowercase


text = input("Enter a string: ")

upper, lower = count_letters(text)

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
#---------------------------------------------------
#Q. Count the occurrence of each word in a sentence.
sentence = input("Enter a sentence: ")

words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequencies:")

for word, count in word_count.items():
    print(word, ":", count)
#---------------------------------------------------
#Q. Find the longest word in a sentence.
def longest_word(sentence):
    words = sentence.split()

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


sentence = input("Enter a sentence: ")

result = longest_word(sentence)

print("Longest word:", result)
#----------------------------------------------------
#Q. Compress a string (e.g., "aaabbc" → "a3b2c1").
def compress_string(text):
    compressed = ""
    count = 1

    for i in range(len(text)):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
        else:
            compressed += text[i] + str(count)
            count = 1

    return compressed

text = input("Enter a string: ")

result = compress_string(text)

print("Compressed string:", result)
#---------------------------------------------------
#Q. Remove all spaces from a string.
text = input("Enter a string: ")

result = text.replace(" ", "")

print("String after removing spaces:", result)
#---------------------------------------------------
#Q. Capitalize the first letter of every word.
sentence = input("Enter a sentence: ")

result = sentence.title() #The title() method converts the first letter of every word to uppercase.

print("Capitalized sentence:", result)
#---------------------------------------------------
#Q. Find the missing number in a sequence from 1 to n.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

n = len(numbers) + 1

total_sum = n * (n + 1) // 2

actual_sum = sum(numbers)

missing_number = total_sum - actual_sum

print("Missing number:", missing_number)
#--------------------------------------------------
#Q. Flatten a nested list.
nested_list = [[1, 2], [3, 4], [5, 6]]

def flatten_list(nested_list):
    flat_list = []

    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)

    return flat_list


result = flatten_list(nested_list)

print("Flattened List:", result)
#----------------------------------------------------
#Q. Group words by their first letter.
words = input("Enter words separated by spaces: ").split()

grouped = {}

for word in words:
    first_letter = word[0]

    if first_letter in grouped:
        grouped[first_letter].append(word)
    else:
        grouped[first_letter] = [word]

print("Grouped Words:")

for letter, word_list in grouped.items():
    print(letter, ":", word_list)
#----------------------------------------------------
#Q. Find the key with the highest value in a dictionary.
data = {
    "A": 45,
    "B": 78,
    "C": 65,
    "D": 92
}

highest_key = None
highest_value = float('-inf')

for key, value in data.items():
    if value > highest_value:
        highest_value = value
        highest_key = key

print("Key with the highest value:", highest_key)
print("Highest value:", highest_value)
#----------------------------------------------------
#Q. Create a dictionary from two lists.
keys = input("Enter keys separated by spaces: ").split()
values = list(map(int, input("Enter values separated by spaces: ").split()))

result = {}

for i in range(len(keys)):
    result[keys[i]] = values[i]

print("Dictionary:", result)