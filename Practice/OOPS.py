#Class and Objects
#Class is the blueprint for creating objects

class Student:     #creating a class
  name = "Karan"

s1 = Student()      #creating object instance
print(s1.name)
#-------------------------------------------------
#Constructor  --> __init__ function

class Employee:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks
    print("Adding new employee in database")

e1 = Employee("Karan", 98)
print(e1.name, e1.marks)

e2 = Employee("Ajinkya", 80)
print(e2.name, e2.marks)

#---------------------------------------------------
#Methods => Methods are functions that belong to objects

class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def hello(self):
    print("Wlecome Student", self.name)

  def get_marks(self):
    return self.marks

s1 = Student("Karan", 97)
s1.hello()
print(s1.get_marks())
#----------------------------------------------------
#Create student class that takes name and marks of 3 subjects as arguments in contructor. Then create a function to print the average

class Student: 
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def get_avg(self):
    sum = 0
    for val in self.marks:
      sum += val
    print('Hi', self.name, "your avg score is:", sum/3)

s1 = Student("Arjun", [90, 80, 70])
s1.get_avg()

s1.name = "Ajinkya"
s1.get_avg()

#---------------------------------------------------
#Static method => Methods that don't use the self parameter(work at class level)

class College:
  @staticmethod   #decorator
  def college():
    print("ABC college")

c1 = College()
c1.college()

#-----------------------------------------------
# Abstraction => Hiding the implementation details of a class and only showing the essential features to the user

class Car:
  def __init__(self):
    self.acc = False
    self.brk = False
    self.clutch = False
  
  def start(self):
    self.clutch = True
    self.acc = True
    print("car started")

car1 = Car()
car1.start()

#----------------------------------------------------
# Encapsulation => Wrapping data and function into a single unit(object)

#----------------------------------------------------

#Q. Create Account class with 2 attributes - balance and account no. 

class Account:
  def __init__(self, bal, acc):
    self.balance = bal
    self.account = acc

  def debit(self, amount):
    self.balance -= amount
    print("Rs", amount, "was debited")
    print("total balance = ", self.get_balance())

  def credit(self, amount):
    self.balance += amount
    print("Rs", amount, "was credited")
    print("total balance = ", self.get_balance())

  def get_balance(self):
    return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.debit(700)
acc1.credit(200)

#----------------------------------------------------
#del keyword => Used to delete object properties or itself 

class Student:
  def __init__(self, name):
    self.name = name

s1 = Student("Chaitanya")
print(s1.name)
del s1.name
print(s1.name)

#--------------------------------------------------
#Private(like) attributes and Methods => Used only within the class and are not accessible from outside the class

class Account:
  def __init__(self, acc_no, acc_pass):
    self.acc_no = acc_no
    self.__acc_pass = acc_pass #private

acc1 = Account("12345", "abcd")
print(acc1.acc_no)
print(acc1.__acc_pass)

#----------------------------------------------------
#Inheritance => When one class (child/derived) derives the properties and methods of another class(parent/base)

class Car:
  @staticmethod
  def start():
    print("Car Started..")

  @staticmethod
  def stop():
    print("Car Stopped.")

class ToyotaCar(Car):
  def __init__(self, name):
    self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print(car1.start())
#----------------------------------------------------
#Types of Inheritance
#1) Single
#2) Multi-level
#3) Multiple
#----------------------------------------------------

# Multi-level

class Car:
  @staticmethod
  def start():
    print("Car Started..")

  @staticmethod
  def stop():
    print("Car Stopped.")

class ToyotaCar(Car):
  def __init__(self, brand):
    self.brand = brand

class Fortuner(ToyotaCar):
  def __init__(self, type):
    self.type = type

car1 = Fortuner("diesel")
print(car1.type)
#-----------------------------------------------------

#Multiple

class A:
  varA = "welcome to class A"

class B:
  varB = "welcome to class B"

class C(A, B):
  varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

#-----------------------------------------------------
#super() => super method is used to access methods of the parent class

class Car:
  def __init__(self, type):
    self.type = type

  @staticmethod
  def start():
    print("Car Started..")

  @staticmethod
  def stop():
    print("Car Stopped.")

class ToyotaCar(Car):
  def __init__(self, name, type):
    super().__init__(type)
    self.name = name
    super().start()

car1 = ToyotaCar("Fortuner", "electric")
print(car1.type)
#---------------------------------------------------

#class method => A class method is bound to the class and recieves the class as an implicit first argument
# Note => static method can't access or modify class state and generally for utility.

class Person:
  name = "anonymous"
  # def changeName(self, name):
  #   #Person.name = name
  #   self.__class__.name = "Rohit"

  @classmethod
  def changeName(cls, name):
    cls.name = name

p1 = Person()
p1.changeName("Rohit")
print(p1.name)
#---------------------------------------------------

class Student:
  def __init__(self, phy, chem, math):
    self.phy = phy
    self.chem = chem
    self.math = math

  @property 
  def percentage(self):
    return str((self.phy + self.chem + self.math)/3) + "%"
  
student1 = Student(98, 78, 89)
print(student1.percentage)

student1.phy = 86
print(student1.percentage)
#----------------------------------------------------

# Polymorphism => when the same operator is allowed to have different meaning according to the context

class Complex:
  def __init__(self, real, img):
    self.real = real
    self.img  = img

  def showNumber(self):
    print(self.real,"i +", self.img,"j")

  def __add__(self, num2):
    newReal = self.real + num2.real
    newImg = self.img + num2.img
    return Complex(newReal, newImg)
  
  def __sub__(self, num2):
    newReal = self.real - num2.real
    newImg = self.img - num2.img
    return Complex(newReal, newImg)
  
num1 = Complex(1, 3)
num1.showNumber()
num2 = Complex(2, 4)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()

#----------------------------------------------------

#Q. Define a circle class to create a circle with radius r using the constructor. Define an Area() method of the class which calculates the area of the circle. Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return (22/7) * self.radius ** 2

  def perimeter(self):
    return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

#------------------------------------------------------
#Q. Define a Employee class with attributes role, department and salary. This class also has a showDetails() method. Create an Enginner class that inherits properties from Employee and has 

class Employee:
  def __init__(self, role, dept, salary):
    self.role = role
    self.dept = dept
    self.salary = salary

  def showDetails(self):
    print("role =", self.role)
    print("dept =", self.dept)
    print("salary =", self.salary)

class Engineer(Employee):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    super().__init__("Engineer", "IT", "75,000")


engg1 = Engineer("Elon Musk", 40)
engg1.showDetails()
