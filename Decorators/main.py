# What is a Decorator? -> A decorator is a function that adds extra behavior to another function without changing its original code.

# Functions as Objects
def greet():
  print("Hello!")

message = greet
message()

# Function Inside Another Function
def outer():
  def inner():
    print("Inside inner function")    
  inner()
outer()

# Passing a Function to Another Function
def greet():
  print("Hello!")

def execute_function(function):
  function()

execute_function(greet)

#---------------------------------------------------
# Creating Decorator
def decorator(function):
  def wrapper():
    print("Starting...")
    function()
    print("Finished...")

  return wrapper

@decorator
def greet():
  print("Hello!")

greet()
#---------------------------------------------------
# Decorator with Function Arguments
def decorator(function):
  def wrapper(*args, **kwargs):
    print("Before function")
    function(*args, **kwargs)
    print("After function")
  return wrapper

@decorator
def greet(name):
  print(f"Hello {name}")

greet("Rohit Sharma")

# *args   → positional arguments
# **kwargs → keyword arguments
#-------------------------------------------------
#Ex:
is_logged_in = False
def login_required(function):
  def wrapper():
    if is_logged_in:
      function()
    else:
      print("Please login first")
  return wrapper

@login_required
def dashboard():
  print("Welcome to Dashboard")

dashboard()
#--------------------------------------------------
