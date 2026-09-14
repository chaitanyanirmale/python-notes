# Lambda Function -> A lambda is a small, one-line function.
# syntax -> lambda arguments: expression
square = lambda num: num * num
print(square(5))

add = lambda a, b: a + b
print(add(10, 20))
#------------------------------------------------
# map() -> map() applies a function to every item in a collection.
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda num: num * 2, numbers))
print(result)

names = ["amit", "rahul", "sneha"]
result = list(map(str.upper, names))
print(result)
#-------------------------------------------------
# filter() -> filter() is used when you want to select specific items based on a condition.

numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda num: num % 2 == 0, numbers))
print(result)

employees = {
  "Amit": 25000,
  "Rahul": 45000,
  "Sneha": 55000
}
result = dict(
  filter(lambda item: item[1] > 30000, employees.items())
)
print(result)
#-------------------------------------------------
# sorted() -> sorted() sorts data.
numbers = [5, 2, 8, 1, 3]
result = sorted(numbers)
print(result)

result = sorted(numbers, reverse=True)
print(result)

names = ["Rahul", "Amit", "Sneha", "Priya"]
print(sorted(names))

employees = [
  {"name": "Amit", "salary": 30000},
  {"name": "Rahul", "salary": 50000},
  {"name": "Sneha", "salary": 40000}
]
result = sorted(
  employees,
  key=lambda employee: employee["salary"]
)
result = sorted(
  employees,
  key=lambda employee: employee["salary"],
  reverse=True
)
print(result)
# ------------------------------------------------

cube = lambda num: num * num * num
print(cube(5))
#-------------------------------------------------
add_numbers = lambda a, b, c: a + b + c
print(add_numbers(10, 20, 30))
#-------------------------------------------------
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda num: num * 10, numbers))
print(result)
# ------------------------------------------------
numbers = [5, 12, 8, 20, 3, 15]
result = list(filter(lambda num: num > 10, numbers))
print(result)
# ------------------------------------------------
numbers = [50, 10, 40, 20, 30]
result = sorted(numbers)
result = sorted(numbers, reverse=True)
print(result, result)
# -------------------------------------------------
employees = [
    {"name": "Amit", "salary": 30000},
    {"name": "Rahul", "salary": 50000},
    {"name": "Sneha", "salary": 40000},
    {"name": "Priya", "salary": 60000}
]
result = sorted(
  employees,
  key = lambda employee: employee['salary'],
  reverse=True
)
print(result)
#----------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(
    map(
        lambda num: num * 10,
        filter(lambda num: num % 2 == 0, numbers)
    )
)
print(result)
