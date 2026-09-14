# Inheritance — one class can reuse another class's functionality
# Encapsulation — controlling access to data
# Polymorphism — same method/interface behaving differently
# Abstraction — hiding unnecessary implementation details

class Employee:
  def work(self):
    print("Employee is working")

class Developer(Employee):
  def work(self):
    print("Developer is writing code")

class Manager(Employee):
  def work(self):
    print("Manager is managing the team")

developer = Developer()
manager = Manager()
# developer.work()
# manager.work()

# Method Overriding -> A child class can replace/redefine a method inherited from the parent.

#----------------------------------------------
# super() -> Sometimes we want to use the parent's functionality while adding our own. That's where super() is useful.
class Employee:
  def __init__(self, name):
    self.name = name

class Developer(Employee):
  def __init__(self, name, language):
    super().__init__(name)
    self.language = language

developer = Developer("Rahul", "Python")
# print(developer.name)
# print(developer.language)
#---------------------------------------------------
# Multiple Levels of Inheritance
class Employee:
  def work(self):
    print("Employee working")

class Developer(Employee):
  def code(self):
    print("Developer coding")

class PythonDeveloper(Developer):
  def python_code(self):
    print("Writing Python code")

developer = PythonDeveloper()  #The PythonDeveloper can access methods from both parent levels.
# developer.work()
# developer.code()
# developer.python_code()

#---------------------------------------------------
# Encapsulation -> Encapsulation means keeping data and the methods that operate on that data together, while controlling how the data is accessed or changed.

# Private Attribu -> Python uses naming conventions such as _name and __name.
class BankAccount:
    def __init__(self, balance):
      self.__balance = balance

    def deposit(self, amount):
      if amount > 0:
        self.__balance += amount

    def get_balance(self):
      return self.__balance

account = BankAccount(5000)
account.deposit(2000)
# print(account.get_balance())
#--------------------------------------------------
# Polymorphism -> This word sounds complicated, but the idea is simple. Polymorphism means the same interface/method can behave differently depending on the object.

class Developer:
  def work(self):
    print("Developer is writing code")

class Manager:
  def work(self):
    print("Manager is managing the team")

class Designer:
  def work(self):
    print("Designing UI")

employees = [
  Developer(),
  Manager(),
  Designer()
]

# for employee in employees:
#   employee.work()

#------------------------------------------

# Abstraction -> Expose what something does while hiding unnecessary implementation details.

# Abstract Classes -> Python provides the abc module for creating abstract base classes.

from abc import ABC, abstractmethod

class Employee(ABC):
  @abstractmethod
  def work(self):
    pass

#------------------------------------------------

class Animal:
  def eat(self):
    print('Animal is eating')

class Dog(Animal):
  def sound(self):
    print("Dog's sound")

class Cat(Animal):
  def sound(self):
    print("Cat's sound")

#------------------------------------------------
