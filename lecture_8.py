# class student:
#     name = "Karan"
# s1 = student()
# print(s1.name)
# s2 = student()
# print(s2.name)

# class Car:
#     color = "Blue"
#     brand = "Mercedes"
# car1 = Car()
# print(car1.color)
# print(car1.brand)        

# class Student:

#     def __init__(self,name,age,marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#         print("adding new student in Database...")

# s1 = Student("Joy Barmon",21,77)
# print(s1.name, s1.age, s1.marks)
# s2 = Student("Shohak Barmon", 21, 99)
# print(s2.name, s2.age, s2.marks)        

# Class & isinstance Attribute
# Class : their identity is the same
# instance : they  are change

# class Student:

#     college_name = "ABC College"  #class attribute
#     name = "anonymous"
#     def __init__(self,name,age,marks):
#         self.name = name  # obj attr > class attr
#         self.age = age
#         self.marks = marks
#         print("adding new student in Database...")

# s1 = Student("Joy Barmon",21,77)
# print(s1.name, s1.age, s1.marks)
# s2 = Student("Shohak Barmon", 21, 99)
# print(s2.name, s2.age, s2.marks) 
# print(Student.college_name)


# class Student:

#     college_name = "ABC College"  #class attribute
   
#     def __init__(self, name, age, marks):
#         self.name = name  # obj attr > class attr
#         self.age = age
#         self.marks = marks
       
#     def welcome(self):
#         print("welcome student,", self.name)

#     def get_marks(self):
#         return self.marks

#     def get_age(self):
#         return self.age  
# s1 = Student("Joy Barmon", 21, 77)
# s1.welcome()
# print("Marks:", s1.get_marks())
# print("Age:", s1.get_age())

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_average(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "Your average score is:", sum/3)

# s1 = Student("Joy Barmon,",[66,88,99])
# s1.get_average()
# s1.marks = [88,99,55]
# s1.get_average()            

#staticmethod(no need self)
# class Student:
#     @staticmethod
#     def Color():
#         print("Blue")

# s1 = Student.Color()       

# Abstruction

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.acc = True
#         self.clutch = True
#         print("Car Started...")

# car1 = Car()
# car1.start()        


# class Account:
    
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_num = acc
#     #Devit Methods
#     def devit(self, amount):
#         self.balance -= amount
#         print("TK.", amount, "was devited")
#         print("Total balance =", self.get_balance())
#     #Credit Methods
#     def credit(self, amount):
#         self.balance += amount
#         print("TK.", amount, "was credited")
#         print("Total balance =", self.get_balance())

#     def get_balance(self):
#         return self.balance    
        
# acc1 = Account(10000, 12345678)
# acc1.devit(1000)
# acc1.credit(500)
# acc1.credit(40000)
# acc1.devit(10000)      