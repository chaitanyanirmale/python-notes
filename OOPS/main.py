# OOPS stands for Object Oriented Programming.
# It is a way of organizing code around objects

#In OOP:
# Data → Attributes
# Actions → Methods
# Class → Blueprint
# Object → Actual instance

# Class -> A class is a blueprint/template for creating objects.
# Ex: class Class_Name:

# Object -> An object is an actual instance of class.
# emp1 = Class_Name()
# emp2 = Class_Name()

# class Employee:
#   pass

# emp = Employee()
# emp.name = 'Rahul'
# emp.salary = 30000

# print(emp.name)
# print(emp.salary)

#---------------------------------
# __init__() -> It is a special method that runs when you create an object.

# class Employee:
#   def __init__(self):
#     print("Employee object created")

# emp1 = Employee()

# self -> allows each object to store its own value.

#-------------------------------------
# class Employee:
#   def __init__(self, name, salary):
#     self.name = name
#     self.salary = salary

#   def display(self):
#     print("Name:", self.name)
#     print("Salary:", self.salary)

#   def increase_salary(self, amount):
#     print('After increment salary:')
#     self.salary += amount

# emp1 = Employee('Rahul', 20000)
# emp2 = Employee('Ajinkya', 30000)

# emp1.display()
# emp1.increase_salary(5000)
# emp1.display()
# emp2.display()
# emp2.increase_salary(1000)
# emp2.display()
#------------------------------------------

# class BankAccount:
#   def __init__(self, owner, balance):
#     self.owner = owner
#     self.balance = balance

#   def deposit(self, amount):
#     self.balance += amount

#   def withdraw(self, amount):
#     if amount <= self.balance:
#       self.balance -= amount
#     else:
#       print("Insufficient balance")

#   def display_balance(self):
#     print("Balance:", self.balance)

# account = BankAccount("Rahul", 5000)
# account.display_balance()
# account.deposit(2000)
# account.display_balance()
# account.withdraw(1000)
# account.display_balance()

#-----------------------------------
class Student:
  def __init__(self, name, age, course):
    self.name = name
    self.age = age
    self.course = course

  def showDetails(self):
    print("Name: ",self.name)
    print("Age: ",self.age)
    print("Course: ",self.course)

student1 = Student('Rahul', 18, 'Python Full Stack')
student1.showDetails()
#------------------------------------------

