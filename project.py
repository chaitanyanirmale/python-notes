#Guess the number

import random

target = random.randint(1, 100)

while True:
  userChoice = input("Guess the target or Quit(Q) : ")
  if(userChoice == "Q"):
    break
  userChoice = int(userChoice)
  if(userChoice == target):
    print("Success : Correct Guess!")
    break
  elif(userChoice < target):
    print("Your number was too small. Take a bigger guess")
  else:
    print("Your number was too big. Take a small guess")

print("------GAME OVER-----")

#------------------------------------------------------

#Random Password Generator

import random
import string

charValues = string.ascii_letters + string.digits + string.punctuation
pass_len = 12
password = ''
for i in range(pass_len):
  password += random.choice(charValues)

print("Your Password: ", password)

# List comprehension 

res = " ".join([random.choice(charValues) for i in range(pass_len)])

print(res)