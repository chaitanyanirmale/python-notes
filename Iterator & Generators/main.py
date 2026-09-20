# What is an Iterator?
# An iterator is an object that allows you to go through a collection one item at a time.

numbers = [10, 20, 30, 40]
numbers_iterator = iter(numbers)

print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))

# iter() -> iter() converts an iterable into an iterator

#--------------------------------------------------
# What is a Generator?
# A generator is a special type of iterator.

# The easiest way to create one is using: yield

def numbers():
  yield 32
  yield 33
  yield 34

result = numbers()

print(next(result))
print(next(result))
print(next(result))

#--------------------------------------------------
# return vs yield

# In return: The function produces the entire list at once.
# But the generator produces values one at a time
#--------------------------------------------------
def even_numbers(numbers):
  for i in numbers:
    if i % 2 == 0:
      yield i

numbers = [1,2,3,4,5,6,7,8,9,10]

for num in even_numbers(numbers):
  print(num)

#-------------------------------------------------
def square_num(numbers):
  for num in numbers:
    square = num * num
    yield square

numbers = [1, 2, 3, 4,  5]
for num in square_num(numbers):
  print(num)

#--------------------------------------------------
def multiple(numbers):
  for num in numbers:
    number = num * 10
    yield number

numbers = [1, 2, 3, 4,  5]
for num in multiple(numbers):
  print(num)
