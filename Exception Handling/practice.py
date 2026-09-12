#Division Calculator
try:
  num1 = int(input("Enter First Number:" ))
  num2 = int(input("Enter Second Number:" ))
  result = num1 / num2
  print(result)

except ValueError: 
  print('Enter valid numbers')

except ZeroDivisionError:
  print('Number can not be zero')

#------------------------------------------
#Age Validation
age = int(input('Enter the Age: '))
if age < 0:
  raise ValueError('Age can not be negative')
if age < 18: 
  print('You are a minor')
if age >= 18:
  print('You are a adult')

#----------------------------------------
#Employee Salary
def calculate_salary(salary):
  if salary < 0:
    raise ValueError('Salary can not be negative')
  print(salary)

salary = int(input('Enter salary: '))
calculate_salary(salary)   

#------------------------------------------
# List Search
numbers = [10, 20, 30, 40, 50]
idx = int(input("Enter index: "))

if idx > len(numbers) or idx < 0:
  raise IndexError('Invalid Index value')

print(numbers[idx]) 
#-----------------------------------------
employee = {
  "name": "Chaitanya",
  "role": "Developer",
  "salary": 40000
}

key = input('Enter key: ')

if key not in employee:
  raise KeyError("Key doesn't exist")

print(employee[key])

#--------------------------------------
#Login system
username = 'admin'
password = '1234'

user_name = input('Enter username: ')
user_password = input('Enter password: ')

try: 
  if username == user_name and password == user_password:
    print('Login Successfully!')
  else:
    raise ValueError('Invalid username or password')
except ValueError as e:
  print('Login Failed: ', e)