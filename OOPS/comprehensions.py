# List & Dictionary Comprehensions

# They are especially useful in Django because you'll frequently work with lists, dictionaries, query results, and data transformations.

# numbers = [1, 2, 3, 4, 5]
# squares = []
# for num in numbers:
#     squares.append(num * num)
# print(squares)

# # This is the normal approach
# # By using list comprehension
# # Basic Syntax
# # [expression for item in iterable]

numbers = [1, 2, 3, 4, 5]
squares = [num * num for num in numbers]
print(squares)


numbers = [1, 2, 3, 4, 5]
result = [num * 2 for num in numbers]
print(result)

names = ["chaitanya", "rahul", "amit"]
upper_names = [name.upper() for name in names]
print(upper_names)

names = ["Amit", "Rahul", "Chaitanya"]
lengths = [len(name) for name in names]
print(lengths)

#--------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

# Using comprehension
# Syntax
# [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

numbers = [1, 2, 3, 4, 5, 6]
odd = [num for num in numbers if num % 2 != 0]
print(odd)

numbers = [5, 12, 8, 20, 3, 15]
result = [num for num in numbers if num > 10]
print(result)

# Using if-else -> Here if-else comes before the for
numbers = [1, 2, 3, 4, 5]
["Even" if num % 2 == 0 else "Odd" for num in numbers]

#--------------------------------------------------
# Dictionary comprehensions
# Syntax -> {key: value for item in iterable}

numbers = [1, 2, 3, 4, 5]
squares = {}
for num in numbers:
    squares[num] = num * num

print(squares)

numbers = [1, 2, 3, 4, 5]
squares = {num: num * num for num in numbers}
print(squares)

#-------------------------------------------------
employees = {
    "Amit": 30000,
    "Rahul": 45000,
    "Sneha": 50000,
    "Priya": 28000
}

high_salary = {
    name: salary
    for name, salary in employees.items()
    if salary > 30000
}
print(high_salary)
#--------------------------------------------------
prices = {
    "Laptop": 50000,
    "Mouse": 1000,
    "Keyboard": 2000
}

discounted = {
    product: price * 0.9
    for product, price in prices.items()
}
print(discounted)
#--------------------------------------------------

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
result = [num for row in matrix for num in row]
print(result)