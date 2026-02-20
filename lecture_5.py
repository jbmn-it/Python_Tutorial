# Loops in Python
# loops are used to repeat instructions.

# while loops

count = 1
while count <=10000000 :
    print("I LOVE YOU", count)
    count += 1

# print numbers from 1 to 5
# i = 1 
# while i <= 5 :
#     print(i)
#     i += 1
# print("Loop ended") 
# # Do reverse
# i = 5
# while i >= 1 :
#     print(i)
#     i -= 1
# print("Loop ended")

# i = 5 
# while i <=6:
#     print(i)
#     i -= 1
# print("loops ended")    
      
# practise
# Q:1 print numbers from 1 to 100
# i = 1
# while i <= 1000000000000 :
#     print(i)
#     i += 1
# Q:2 print numbers 100 to 1
# i = 100
# while i >= 1 :
#     print(i)
#     i -= 1
# Q:3 print the multiplication number of a number n
# n = int(input("enter number:"))
# i = 1
# while i <= 10 :
#     print(n*i)
#     i += 1
# print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0 
# while idx < len(nums):
#     print(nums[idx])
#     idx +=1

# movies = ["titanic","lucy","forest jump","pursuit of happiness","home","pemalu"]
# idx = 0
# while idx < len(movies):
#     print(movies[idx])
#     idx +=1 
# l = [1,2,3,4,5,6,7,8,9,67,45,55,33,99]
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

# search for nuber x in thistuple using tuple
# (1,2,3,4,5,6,4,45,345,633,643,2455,556,,356,44)
# nums = (1,2,3,4,5,6,4,45,345,633,643,2455,556,2455,356,44)
# x = 2455
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("found at idx", i)
#     else:
#         print("finding...")
#     i += 1    

# Break & continue
# Break: used to terminate the loops when encountered.
# nums = (1,2,3,4,5,6,4,45,345,633,643,2455,556,2455,356,44)
# x = 2455
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("found at idx", i)
#         break
#     else:
#         print("finding...")
#     i += 1 
# print("end of the loop")

# nums1 = (66,54,6,35,74,25,57)
# x = 25
# i = 0
# while i < len(nums1):
#     if(nums1[i] == x):
#         print("found at idx", i)
#         break
#     else:
#         print("finding...")
#     i += 1    
# print("end of the loop")
# Continue
# i = 1
# while i <= 10:
#     if(i%2 !=0):
#         i += 1
#         continue
#     print(i)
#     i += 1
#  loop are used for sequential traversal.For traversing list,string,tuple etc.

# nums = [1,2,3,4,5,6,7,5,4,4,3,7,6]
# for val in nums:
#     print(val)
# veggies = ["potato","bringal","ladyfinger","papeya"]
# for val in veggies:
#     print(val)
    
# str1 = ("joybarmon")
# for chr in str1:
#     if(chr == 'r'):
#         print("founded")
#         break
#     print(chr)

# print("ended")

# Let's preactise
# using for
# print the elements of the following list using a loop:
# [1,2,3,4,5,6,7,8,9,44,66,77,88,]
# nums = [1,2,3,4,5,6,7,8,9,44,66,77,88]
# for el in nums:
#     print(el)
# Search for a number x in this tuple using loop:
# [1,2,3,4,5,6,7,8,9,44,66,77,88]
# nums = (1,2,3,4,5,6,7,8,600,9,44,66,6,77,600,88)
# x = 600
# idx = 0
# for el in nums:
#     if(el == x):
#         print("number founded at idx",idx)
#         break
#     idx += 1
# range()
# Range function retuns a sequence of numbers
# starting from 0 by default,and increments by 1 (by defualt),stop defaualt a
#stop before a spicified number.
# range(start?stop,stop?)
# for el in range(2,103,2):
#     print(el)

# Let's Practice
#using for & range()
#Q1 Print numbers from 1 to 100.
#Q2 Print numbers from 100 to 1.
#Q3 Print the multiplication table of a number n.
# Ans:1
# for i in range(1,101):
#     print(i)
# Ans:2
# for i in range (100,0,-1):
#     print(i)
# Ans:3
# n = int(input("enter number:"))
# for i in range(1,11):
#     print(n*i)
# pass Statement
# pass is a null statement that does nothing.it is used a placeholder for future code. 
# for i in range(5):
#     pass
# if i>5:
#     pass
# print("print some useful work")
# write a python to find the sum of first n numbers(using while)

# n = int(input("Enter the value of n: "))
# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1

# print("The sum is:", sum)
# write a python to find the factorial of first n numbers(using for)

# n = int(input("Enter the value of n: "))
# fact = 1

# for i in range(1,n+1):
#     fact *= i
# print("factorial", fact)   