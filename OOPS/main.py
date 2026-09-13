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

class Employee:
  pass

emp = Employee()
emp.name = 'Rahul'
emp.salary = 30000

print(emp.name)
print(emp.salary)

#---------------------------------
# __init__() -> It is a special method that runs when you create an object.

class Employee:
  def __init__(self):
    print("Employee object created")

emp1 = Employee()

# self -> allows each object to store its own value.

#-------------------------------------
class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def display(self):
    print("Name:", self.name)
    print("Salary:", self.salary)

  def increase_salary(self, amount):
    print('After increment salary:')
    self.salary += amount

emp1 = Employee('Rahul', 20000)
emp2 = Employee('Ajinkya', 30000)

emp1.display()
emp1.increase_salary(5000)
emp1.display()
emp2.display()
emp2.increase_salary(1000)
emp2.display()
#------------------------------------------

class BankAccount:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
      print("Insufficient balance")

  def display_balance(self):
    print("Balance:", self.balance)

account = BankAccount("Rahul", 5000)
account.display_balance()
account.deposit(2000)
account.display_balance()
account.withdraw(1000)
account.display_balance()

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
class Cars:
  def __init__(self, brand, model, price):
    self.brand = brand
    self.model = model
    self.price = price

  def display_details(self):
    print("Brand Name:", self.brand)
    print("Model Name:", self.model)
    print("Price:", self.price)

car1 = Cars('Toyota', 'Fortuner', 5000000)
car2 = Cars('BMW', 'M5', 15000000)
car1.display_details()
car2.display_details()
#--------------------------------------------
class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def display_product(self):
    print("Product Name: ", self.name)
    print("Product Price: ", self.price)
    print("Product Quantity: ", self.quantity)

  def increase_quantity(self, amount):
    self.quantity += amount

  def calculate_total(self):
    total = self.price * self.quantity
    print('Your Total: ', total)

product1 = Product('Vivo', 18000, 2)
product1.display_product()
product1.increase_quantity(2)
product1.display_product()
product1.calculate_total()
