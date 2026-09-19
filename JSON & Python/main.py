# What is JSON?
# JSON = JavaScript Object Notation. It is a format used to store and exchange data.
{
  "name": "Chaitanya",
  "age": 22,
  "course": "MCA"
}
# JSON looks very similar to a Python dictionary, but they are not exactly the same thing.
# The main difference is that JSON is a text/data interchange format, while a Python dictionary is a Python object.

# Python has a built-in json module. We don't need to install anything with pip.
import json

# Python Dictionary → JSON. This process is called serialization
# dumpS → Python object → JSON string

student = {
  "name": "Chaitanya",
  "age": 22,
  "course": "Python"
}
json_data = json.dumps(student, indent=4)
print(json_data)
# print(type(student))
# print(type(json_data))

students = [
  "Chaitanya",
  "Ajinkya",
  "Rohit"
]
data = json.dumps(students)
print(data)

# The reverse process is called deserialization.
json_data = '{"name": "Chaitanya", "course": "Python"}'
student = json.loads(json_data)
print(student)


# dump() vs dumps()

# dumps() => Python object → JSON string
# dump() => Python object → JSON file
#--------------------------------------------------
# Saving JSON to a File
employees = [
    {
        "name": "Chaitanya",
        "dept": "Development"
    },
    {
        "name": "Ajinkya",
        "dept": "Sales"
    }
]

with open("employees.json", "w") as file:
  json.dump(employees, file, indent=4)

# Reading JSON from a File
with open('employees.json', 'r') as file:
  employee = json.load(file)

print(employee)
print(employee[0]["name"]) # Accessing the name from json file

# loads  → String → Python
# load   → File → Python

#-----------------------------------------------
# Loop through JSON data
for key, value in student.items():
  print(key, ":", value)
#------------------------------------------------

# Handling Invalid JSON  
# Invalid JSON can cause:JSONDecodeError

try:
  data = json.loads('{"name": "Chaitanya"')

except json.JSONDecodeError:
  print("Invalid JSON")