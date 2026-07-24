#Reading the file
f = open("demo.txt", "r")
data = f.read() #used to read the file
print(data)
print(type(data))
f.close()
data = f.readline() #reads one line at a time

f = open("demo.txt", "r+") #Overwrite the text
f.write("ABC")
f.close()
#----------------------------------------
#Writing into file
f = open("demo.txt", "w")
f.write("I am currently learning python")
f.close()
#----------------------------------------
#Append text to file
f = open("demo.txt", "a")
f.write("\nAfter I will learn ReactJs")
f.close()
#----------------------------------------
#with syntax
with open("demo.txt", "r") as f:
  data = f.read()
  print(data)
#----------------------------------------
#Deleting a file
# os.remove(filename)
import os
os.remove("demo.txt")
#----------------------------------------
#create a new file "Practice.txt" and add the below data
with open("practice.txt", "w") as f:
  f.write("Hi everyone \nwe are learning file I/O \n")
  f.write("Using java \nI like programming in java")

#WAF that replaces all occurrences of "Java" with "Python" in above file

with open("practice.txt", "r") as f:
  data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("Practice.txt", "w") as f:
  f.write(new_data)

#Search the word "learning" in the file

def check_for_word():
  word = "learning"
  with open("Practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
      print("Found")
    else:
      print("No found")

def check_for_line():
  word = "learning"
  data = True
  line_no = 1
  with open("Practice.txt", "r") as f:
    while data:
      data = f.readline()
      if(word in data):
        print(line_no)
        return
      line_no += 1
  return -1

print(check_for_line())

#----------------------------------------------
#Q. from a file containing numbers seprated by comma, print the count of even numbers

count = 0
with open("Practice.txt", "r") as f:
  data = f.read()
  print(data)
  num = ""
  for i in range(len(data)):
    if(data[i] == ","):
      print(int(num))
      num = ""
    else:
      num += data[i]
#------------------------
  nums = data.split(",")
  for i in nums:
    if(int(i) % 2 == 0):
      count += 1
  print(count)
