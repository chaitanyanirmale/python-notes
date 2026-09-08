#Set is the collection of unordered items, each element in the set must be unique and immutable

nums = {1, 2, 3, 4, 5}
print(nums)

collection = {1,2,2,3,4,4} 
print(collection) #ignores the duplicate values
print(len(collection))

student = set() #empty set
print(type(student))

#cannot store list in a set

#methods

student.add("Rohit Sharma") #Adds element to the set
student.add("Virat Kohli")
student.add("Jasprit Bumrah")
print(student)

student.remove("Virat Kohli") #removes an element
print(student)

student.clear() #empties the set
print(len(student))


marks = {40, 70, 39, 44, 20}
print(marks.pop()) #removes a random value
print(marks.pop()) 


set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
print(set1.intersection(set2))


#Practice 
#1) You are given a list of subjects for student. Assume one classroom is required for 1 subject. How many classrooms are needed by all students
subjects = {"Java", "Python", "C++", "Java", "JavaScript", "C","C++", "Python", "Java", "Python"}

print("Classrooms needed by all students",len(subjects))