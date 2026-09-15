# File Handling -> File handling means creating, reading, writing, updating, and managing files using Python.

# r -> Read
# w -> Write
# a -> Append
# x -> Create a new file
# rb -> Read Binary
# wb -> Write Binary

# 1. Opening a File -> Python uses the open() function.
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# with open()
# Instead of manually closing the file, Python provides:
with open("data.txt", "r") as file:
  content = file.read()
  print(content)

# Reading only a few characters
with open("data.txt", "r") as file:
  content = file.read(10)
print(content)

# readline() reads one line.
with open("data.txt", "r") as file:
  line = file.readline()
print(line)

with open("data.txt", "r") as file:
  print(file.readline())
  print(file.readline())

# readlines() returns all lines as a list.
with open("data.txt", "r") as file:
  lines = file.readlines()
print(lines)

# Reading a File Using a Loop
with open("data.txt", "r") as file:
  for line in file:
    print(line.strip())
# .strip() removes unnecessary whitespace/newline characters.

#--------------------------------------------------
# Writing to a File -> Use "w". 
with open("data.txt", "w") as file:
  file.write("Hello Python")

# "w" overwrites existing content.
with open("data.txt", "w") as file:
  file.write("New Content")

#--------------------------------------------------
# Append Mode "a", means add content to the end.
with open("data.txt", "a") as file:
  file.write("\nReact")
# Unlike "w", "a" doesn't delete the existing content.

# -------------------------------------------------
# Creating a New File with "x"
with open("newfile.txt", "x") as file:
  file.write("New file created")

# This creates a new file.
# But if the file already exists, Python raises: FileExistsError 

try:
  with open("newfile.txt", "x") as file:
    file.write("Hello")

except FileExistsError:
  print("File already exists")
#------------------------------------------
try:
  with open("abc.txt", "r") as file:
    print(file.read())

except FileNotFoundError:
  print("File not found")

#----------------------------------------
# Combining File Handling + Exception Handling
try:
  with open("employees.txt", "r") as file:
    data = file.read()
    print(data)

except FileNotFoundError:
  print("Employee file does not exist")

except PermissionError:
  print("You don't have permission to access this file")

#------------------------------------------------
# Working with File Paths
with open("D:/Projects/TestApp/data.txt", "r") as file:
  print(file.read())

#------------------------------------------------
# Checking if a File Exists -> Python's os module can help.
import os
if os.path.exists("data.txt"):
  print("File exists")
else:
  print("File does not exist")

#------------------------------------------------
# Getting File Information
import os
print(os.path.exists("data.txt"))
print(os.path.getsize("data.txt"))
# getsize() returns the file size in bytes.

#------------------------------------------------
employees = [
    "Amit - Developer - 40000",
    "Rahul - Tester - 35000",
    "Sneha - Manager - 60000"
]

with open("employees.txt", "w") as file:
  for employee in employees:
    file.write(employee + "\n")

with open("employees.txt", "r") as file:
  for employee in file:
    print(employee.strip())


with open("employees.txt", "r") as file:
  employees = [line.strip() for line in file]

print(employees)
#----------------------------------------------
def save_employee(name, role, salary):
  with open("employees.txt", "a") as file:
    file.write(f"{name} - {role} - {salary}\n")

save_employee("Amit", "Developer", 40000)
save_employee("Rahul", "Tester", 35000)