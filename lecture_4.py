# Dictionary in pythone
# Dictionaries are used to store data values key:values pair
# they are unordered,mutable(changeable) & don't allows duplicates keys

info = {
     "key" : "value",
     "name": "apna_college",
    "learning" : "coding",
      "age" : 36,
      "is_adult" : True,
      12 : 434,
      "subject" : ["pythone","c","java"], #list
      "topics" : ("dict","sets") #tuple
      }
null_dictionary = {}
null_dictionary["name"] = "Joy Shree Ram"
print(null_dictionary)


info["name"] = "Joy_Barmon"
info["surname"] = "Barmon"
print(info)

#nasted_dictionary

# student = {
#        "name" :"Joy_Barmon",
#        "subjects" : {
#            "physics" : 78,
#            "chemistry" : 88,
#            "math" : 76
# }

# }
# print(student["subjects"]["chemistry"])

#Dictionary_methods
#myDic.keys --- returns all keys

#print(students.keys())
# print(len(student.keys()))
# print(len(list(student.keys())))

#myDic.values --- returns all values
# print(student.values())
# print(list(student.values()))

#myDic.item --- returns all(values and keys)pairs as tuples

# print(len(student.keys()))
# pairs = (list(student.items()))
# print(pairs[1])

#myDic.get --- returns the keys according to values
# print(student["name4"])
# print(student.get(name4))

#myDic.update --- inserts the specefied values

# student= {"name":"Shohak","city":"Dhaka"}
# (student.update({"iiii" : "tyiyiu"}))   
# print(student)

#set in pythone
#set is the collection of unordered items
#Eatch element in the set must be unique & unmutable

#nums = {1,2,3,4,5,6}
#sets ={1,2,2,2}
#repeated elements stored only once,so it resolved to {1,2}
# collection = {1,2,3,4,5,"Joy_Barmon","Hare_Krishna",9,7,4}
# print(collection)
# print(type(collection))
# print(len(collection))

# empty set
# null_set = set()
# print(type(null_set))

#sets methodes
#set.add #add an elements
# set1 = {1,2,3,4,5,6,7,8,9}
# set1.add(10)
# set1.remove(1)
# set1.clear()
# print(len(set1))

# information = {"Joy_Barmon",10,"Pythone","AI_ENGINEER","HARE_KRISHNA",22,45,44,56,78,88}
# print(information.pop())
#set.union
# set1 = {1,2,3,4}
# set2 = {8,9,7,3}
# print(set1.union(set2))
#set.intersection
# set1 = {1,3,4,5,6}
# set2 = {2,3,4,5,1,9}
# print(set1.intersection(set2))

# Lets Practise
#Q1 Store word meanings in a pythone Dictionary
# table : "a piece of furniture","list and facts and figures"
# cat : "a small animal"

# dictionary = {
#     "cat" : "a small cat",
#     "table" : ["a piece of furnitur","list and facts and figures"]

# }
# print(dictionary)
# Q2. You are given a list subjects for students.
# Assume one classroom required for 1 subject.How many subjects needed for classroom.
#     "pythone","java","c++","pythone","java script","c","c++"

# answer:
# subjects = {"pythone","java","c++","pythone","java script","c","c++"}
# print(len(subjects))

#Q3. WAP to enter marks of 3 subjects from the users and store them in a dictionary.
# Start with an empty dictionary & add one by one.Use subjects name as key & marks as value.
#answer:
# marks = {}

# x = int(input("enter physics:"))
# marks.update({"physics": x})


# y = int(input("enter chemistry:"))
# marks.update({"chemisty": y})


# z = int(input("enter math:"))
# marks.update({"math": z})

# print(marks)

a = 11
b = 11

# Don't change below this line
c = 0
if a >= b and not b < 10:
    c = 2

c += 1
print(f"c = {c}")

