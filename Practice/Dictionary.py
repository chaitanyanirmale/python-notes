# Dictionaries are used to store data values in key:value pairs 
# They are unordered, mutable, and don't allow duplicate values

dict = {
  "name" : "Arjun",
  "cgpa" : 9.4,
  "city" : "Pune"
}

print(dict)

student = {
  "name" : "Krishna",
  "subjects" : ["Python", "Java", "ReactJs"],
  "marks" : (74, 80, 94),
  "class" : "1st Year", 
  "grade" : "A"
} 

print(student)
print(student["name"])
print(student["subjects"])
print(student["class"])

student["name"] = "Aniket"
print(student["name"])

fruits = {}
print(fruits)  #empty dict
fruits["name"] = "Mango"  #added a new key with value
print(fruits)


student1 = {
  "name" : "Ajinkya",
  "subjects" : {
    "phy" : 90,
    "chem" : 78,
    "bio" : 88,
    "math" : 94
  } 
}

print(student1["subjects"]["phy"])  #nested dictionaries

#methods 

print(student.keys()) #returns all keys 
print(list(student.keys())) #converting in list

print(student.values()) #returns all values
print(list(student.values())) 

print(student.items()) #returns all (key, val) pairs as tuples
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])

print(student.get("name")) #returns the key according to value
print(student.get("name2")) #returns none, not error

student.update({"city": "Pune"}) #inserts the specified items to the dictionary
print(student)


#practice
#1) Store the word meanings in a python dictionary
dict2 = {
  "cat" : "a small animal",
  "table" : ["a piece of furniture", "list of facts and figures"]
}

#2) Wap to enter marks of 3 subjects from the user and store them in dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value

marks = {}

x= int(input("Enter phy:"))
marks.update({"phy: " : x})

x= int(input("Enter math:"))
marks.update({"math: " : x})

x= int(input("Enter chem:"))
marks.update({"chem: " : x})

print(marks)