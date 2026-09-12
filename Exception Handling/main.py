# What is an exception?

# An exception is an error that happens while a program is running 
# If an exception isn't handled, the program stops at that point.

# Basic Structure
try:
  # code that might cause an error
  number = int(input("Enter a number: "))
  print(number)

except ValueError:
  # what to do if an error happens
  print("Please enter a valid number.")

# Common python exceptions

# 1) ValueError  -> Invalid Value
# 2) TypeError   -> Wrong data type
# 3) ZeroDivisionError -> Division by zero
# 4) IndexError  -> Invalid list index
# 5) KeyError    -> Missing dictionary key
# 6) FileNotFoundError -> File doesn't exist
# 7) NameError   -> Variable doesn't exist


#Multiple except
try:
  number = int(input("Enter number: "))
  result = 100 / number
  print(result)

except ValueError:
  print("Please enter a number.")

except ZeroDivisionError:
  print("Number cannot be zero.")

else:
  print("You entered:", number)  # else runs only when there is no exception

finally:
  print("Program finished.")  # finally runs whether an error occurs or not.


# raise -> Sometimes you want to create an exception yourself. That's what raise does.

age = 15
if age < 18:
  raise ValueError("Age must be 18 or above")

salary = -5000
if salary < 0:
  raise ValueError("Salary cannot be negative")

#--------------------------------------
numbers = [10, 20, 30]
try:
  print(numbers[5])

except IndexError:
  print("Index does not exist.")

#---------------------------------------
employee = {
  "name": "Rahul",
  "salary": 30000
}
try:
  print(employee["department"])

except KeyError:
  print("Department key doesn't exist.")

#--------------------------------------
try:
  file = open("employees.txt", "r")
  data = file.read()
  file.close()

except FileNotFoundError:
  print("File doesn't exist.")


