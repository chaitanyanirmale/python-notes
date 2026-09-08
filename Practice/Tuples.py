#Tuples are immutable

marks = (40, 50, 35, 28)
print(type(marks))

#Slicing
print(marks[0:2])
print(marks[3:len(marks)])
print(marks[2:])
print(marks[-3:-1])

#methods

print(marks.index(50)) #print index of element 
print(marks.count(40)) #counts the element occured 

#1) WAP to count the number of students with the "A" grade in the following tuple

tup = ("C", "D", "A", "A", "B", "B", "A")

print(tup.count("A"))

#2) Store the above values in a list and sort them from "A" to "D"

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)