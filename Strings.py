#Strings are immutable -- IMP

str1 = "Hello "
str2 = "My name is Chaitanya"

str3 = str1 + str2
# print(str3) # concatination

# print(len(str1)) #len() function


#indexing

name = "Chaitanya"
# print(name[2])

#slicing - Accessing parts of a string
#str[start_idx : end_idx]

str4 = "The view is beautiful"
# print(str4[0:2])
# print(str4[3:len(str4)])
# print(str4[6:])
# print(str4[-5:-1])


#functions

str5 = "I am a coder"
# print(str5.endswith('er')) #returns true if string ends with substr
# print(str5.capitalize()) #capitalizes 1st char 
# print(str5.replace("coder", "programmer")) #replaces all occurrences of old with new
# print(str5.find("o")) #returns 1st index of 1st occurrer
# print(str5.count("a")) #counts the occurrence of substr

# #Practice - questions
# #1) WAP to input userName and print its length
# userName = input("Enter your Name: ")
# print(len(userName))

# #2) WAP to find the occurrence of $ in a string
# str6 = "Hi, $ I am the $ symbol $99.99"
# print(str6.count("$"))

username = "racecar"

reverse_text = username[::-1]

if username == reverse_text:
  print("Palindrome")
else:
  print("Not Palindrome")