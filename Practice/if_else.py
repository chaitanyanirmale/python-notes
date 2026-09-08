marks = int(input("Marks: "))

if(marks >= 90): 
  print("A+")
elif(marks >= 80 and marks < 90): 
  print("A")
elif(marks >= 70 and marks < 80):
  print("B")
elif(marks >= 60 and marks <70):
  print("C")
else: 
  print("D")

#1) WAP to check if a number entered by the user is even or odd

number = int(input("Enter the Number: "))
if(number % 2 == 0):
  print("Even")
else: 
  print("Odd")

#2) WAP to find the greatest of three numbers entered by the user

a = int(input("Enter the first Number: "))
b = int(input("Enter the second Number: "))
c = int(input("Enter the third Number: ")) 

if(a >= b and a >= c):
  print("First no. is greatest")
elif(b >= c):
  print("Second no. is greatest")
else: 
  print("Third is largest")

#3) WAP to check if a number is multiple of 7 or not

number = int(input("Enter number: "))

if(number % 7 == 0):
  print("Multiple of 7")
else:
  print("Not a multiple of 7")