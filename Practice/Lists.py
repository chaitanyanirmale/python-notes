#lists are mutable -- IMP

marks = [78.8,45.9,89.4,85.6,90.2]
print(marks) #print whole list
print(marks[1], marks[3]) #print particular marks 


student = ["Karan", 22, "Mumbai"]
print(student)
student[0] = "Arjun"
print(student)

#slicing 
numbers = [81, 73, 65, 97, 59]
print(numbers[0:2])
print(numbers[3:len(numbers)])
print(numbers[2:])
print(numbers[-3:-1])


#functions// methods

age = [81, 56, 26, 45]

age.append(34) #adds one element at the end 
print(age)
age.sort() #sorts in ascending
print(age)
age.sort(reverse=True) #sorts in descending
print(age)
age.reverse() #reverses the list 
print(age)

age.insert(3, 78) #inserts element at index 
print(age)

age.remove(26) #removes first occurences of element
print(age)


#1) WAP to ask the user to enter names oof their 3 favourite movies & store them in a list

movies = []
movies.append(input("Enter First Movie: "))
movies.append(input("Enter Second Movie: "))
movies.append(input("Enter Third Movie: "))

# print(movies)

#2) WAP to check if a list contains a palindrome of elements (Hint: use copy() method)

list = [1,2,3,2,1]
copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
  print("Palindrome")
else: 
  print("NOT Palindrome")