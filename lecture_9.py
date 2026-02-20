# del keyword
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Joy Barmon")
# print(s1.name)
# del s1.name
# print(s1.name)

### Private(Like) attribute & methods
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
            
# acc1 = Account(123456, "jkl")
# print(acc1.acc_no)
# print(acc1.__acc_pass)
# # # 
# class person:
#     __name = "anynomouse"
#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()
# p1 = person()
# print(p1.welcome())


###inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortunar")
# car2 = ToyotaCar("melody")
# print(car2.stop()) 

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)             


###super method
# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = ToyotaCar("fortunar", "electrict")
# print(car1.type)


###class methods

# class Person:
#     name = "anonymous"

#     # def changeName(self, name):
#     #   self.__class__.name = "ROY"

#     @classmethod
#     def changeName(cls, name):
#         cls.name =name

# p1 = Person()
# p1.changeName("JOY")
# print(p1.name)
# print(Person.name)


# ### property methods
# class Student:
#     def __init__(self, phy, chem, math, bio):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.bio = bio

#     @property
#     def percentage(self):
#         return str ((self.phy+self.chem+self.math+self.bio)/4) + "%"
# stu1 = Student(99, 88, 87, 77)
# print(stu1.percentage)
# stu1.bio = 88
# print(stu1.percentage)

##polymorphism

##Complex Number

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def shownNumber(self):
#         print(self.real, "i +", self.img, "j")

#     def __add__ (self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex (newReal, newImg)

# num1 = Complex(1, 2)
# num1.shownNumber()

# num2 = Complex(3, 4)
# num2.shownNumber()

# num3 = num1 + num2
# num3.shownNumber()

# ##practise##
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area (self):
#         return (22/7) * self.radius ** 2

#     def perimeter (self):
#         return 2 * (22/7) * self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())
# ####
# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showDetails(self):
#         print("role =", self.role)
#         print("department =", self.department)
#         print("salary =", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "755522")
        
#     def showDetails(self):
#         # First show the details from the Employee class
#         super().showDetails()
#         # Now include Engineer-specific details
#         print("name =", self.name)
#         print("age =", self.age)

# # Create an instance of Engineer and display all details
# egg1 = Engineer("JOY BARMON", "21")
# egg1.showDetails()

# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
#     def __gt__(self, ord2):
#         return self.price > ord2.price 


# ord1 = Order("chips", 30)
# ord2 = Order("tea", 15)

# print(ord1 > ord2)