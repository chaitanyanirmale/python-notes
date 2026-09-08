#Loops are used to repeat instructions

#1) While loops

# i = 1
# while i <= 10:
#   print(i*27)
#   i += 1

# a = 1
# while a <= 5:
#   print(a)
#   a += 1
# print("Loop end")

# b = 5 
# while b >= 1:
#   print(b)
#   b -= 1

# nums = 1
# while nums <= 100:
#   print(nums)
#   nums += 1

# #Q. Print the elements of the following list using a loop

# nums = [1,4,9,16,25,36,49,64,81,100] #list
# i = 0 
# while i < len(nums):
#   print(nums[i])
#   i += 1

# nums = (1,4,9,16,25,36,49,64,81,100) #tuple
# x = 36
# i = 0
# while i < len(nums):
#   if(nums[i] == x):
#     print("Element found at index: ", i)
#   i += 1


# #Break keyword

# i = 1
# while i <= 5:
#   print(i)
#   if(i == 3):
#     break
#   i += 1

# #Continue keyword

# i = 1
# while i <= 5:
#   if(i == 3):
#     i += 1
#     continue
#   print(i)
#   i += 1

#2) For loops -> used for sequential traversal.

# nums = [1,3, 5, 7, 9]
# for num in nums:
#   print(num)

# str = "India"
# for char in str:
#   print(char)



#Range -> This function returns a sequence of numbers, starting from 0 by default, and increments by 1(by default) and stops before a specified number.

# for i in range(1,6): #range(start and stop) 
#   print(i)

# for i in range(2, 20, 2): #range(start, stop, increment)
#   print(i)


#Q. Print 1 to 100 using for and range 
# for i in range(1, 101):
#   print(i)
 
# Print 0 to 100
# for i in range(100, 0, -1):
#   print(i)

#Multiplication table
# n = int(input("Enter the number: "))

# for i in range(1, 11):
#   print(n * i)

#Pass Statement -> Pass is a null statement that does noting, it is used as a placeholder for future code

# for i in range(5):
#   pass

# print("Work will be done in future")

#Q. WAP to find sum of first n natural numbers (using while)

# n = 5
# sum = 0
# i = 1
# while i<= n:
#   sum += i
#   i += 1

# for i in range(1, n+1):
#   sum += i

# print("Total Sum: ", sum)

#Q. WAP to find the factorial of first n natural numbers 

n = 5
fact = 1
i = 1
# while i <= n:
#   fact *= i
#   i += 1

# for i in range(1, n+1):
#   fact *= i

# print("Factorial is", fact)

#Q) Calculating sum of digits in a number
num = 12345
sum_digits = 0

while num > 0:
  digit = num % 10
  sum_digits += digit
  num = num // 10

print(sum_digits)