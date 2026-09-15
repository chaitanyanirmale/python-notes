students = [
  'Name: Chaitanya',
  'Course: MCA',
  'Language: Python'
]

with open('Student.txt', 'w') as file:
  for student in students:
    file.write(student + "\n")

with open('Student.txt', 'r') as file:
  content = file.read()
  print(content)

with open('Student.txt', 'a') as file:
  file.write('Goal: Software Developer')

with open('Student.txt', 'r') as file:
  for student in students:
    print(student.strip())


try:
  with open('missing.txt', 'r') as file:
    data = file.read()
    print(data)

except FileNotFoundError:
  print('File not found')

def add_student(name, course):
  with open('student.txt', 'a') as file:
    file.write(f'Name: {name} \nCourse: {course}\n\n')

def view_students():
  with open('student.txt', 'r') as file:
    data = file.read()
    print(data)

add_student('Ranjit', 'JavaScript')
add_student('Rahul', 'Node Js')

view_students()