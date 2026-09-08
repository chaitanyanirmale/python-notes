#Functions is block of statement that performs a specific task

# def sum(a, b):
#   s = a + b 
# print(sum(3, 7))

#functions => Built-In and Userdefined 

#default parameters
# def calc_prod(a=1, b=2):
#   print(a*b)
#   return a*b

# calc_prod()

#Q. WAF to print the length of a list

# nums = [2,4,6,8,10]
# cities = ['Pune', 'Mumbai', 'Delhi', 'Banglore']

# def len_nums(list):
#   print(len(list))

# len_nums(nums)
# len_nums(cities)

#Q. WAF to print the elements of a list in a single line 

# def list_items(list):
#   for items in list:
#     print(items, end=" ")

# list_items(cities)
# list_items(nums)

#Q. WAF to find the factorial of n.

# def cal_factorial(n):
#   fact = 1
#   for i in range(1, n+1):
#     fact *= i
#   print(fact)

# cal_factorial(6)

#Q. WAF to convert USD to INR

# def converter(usd_val):
#   inr_val = usd_val * 83
#   print(usd_val, "USD =", inr_val, "INR")

# converter(5)


#Q. WAF to check enven or odd

# def eve_odd(n):
#   if(n % 2 == 0):
#     print("Even")
#   else:
#     print("Odd")

# eve_odd(10)

#------------------------------------------------

#Recursion => When a function calls itself repeatedly

# def show(n):
#   if(n == 0):
#     return
#   print(n)
#   show(n-1)

# show(5)

# def fact(n):
#   if(n == 0 or n == 1):
#     return 1
#   else: 
#     return fact(n-1) * n

# print(fact(5))


#Q. Write a recursive function to calculate the sum of first n natural numbers

# def sum(n):
#   if(n == 0):
#     return 0
#   return sum(n-1) + n
# sumOfNumber = sum(10)
# print(sumOfNumber)

#Q. Write a recursive function to print all elements in a list

def print_list(list, idx=0):
  if(idx == len(list)):
    return
  print(list[idx])
  print_list(list, idx+1)

fruits = ["Mango", "Litchi","Apple", "Banana"]
print_list(fruits)