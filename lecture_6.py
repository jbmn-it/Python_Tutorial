#functions main intentention is to decrease redundency
# funtions_difinition
# def calc_sum(a,b): #parameters
#     return a - b
# sum = calc_sum(2,5) #functions call;arguments
# print(sum)
     
# def print_hello():
#     print("hello")
# print_hello() 
# print_hello() 
# print_hello() 

#funtion_difinition
# def calc_sum(a,b):
#     sum = a + b
#     print(sum)
#     return sum
# calc_sum(5,6)
# calc_sum(55,7)
# calc_sum(77,6)
   
#average of 3 numbers
# def average_cal (a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
# average_cal(2,4,5)

# average_cal(3,5,6) 

# Question: WAF to print the lenth of a list(list in the perameter)
# cities = ["dinajpur","rangpur","rajshahi","shyklet","dhaka"]
# heroes = ["thor","spiderman","batman","superman","ironman"]
# Mahavarat = ["arjuna,krishna,"]
# # def print_len(list):
# #     print(len(list))
# print(len(cities))
# print(len(heroes))    

# Question: WAF to print the elements of a list in a single line.(list in the parameter)
# cities = ["dinajpur", "rangpur", "rajshahi", "shyklet", "dhaka"]
# heroes = ["thor", "spiderman", "batman", "superman", "ironman"]
# Mahavarat = ["arjuna,krishna,"]
# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end="     ")

# print_list(heroes)           

# WAF to find the factorial of n(n is a perameter)
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
# cal_fact(5)

#WAF to convert usd to inr
# def converter(usd_val):
#     taka_val = usd_val * 121.49
#     print(usd_val, "USD =", taka_val, "TK")
# converter(5000)    

# n = int(input("Enter a number: "))  # Store the input in variable n

# def check_odd_even(n):
#     if n % 2 == 0:
#         print(n, "is even")
#     else:
#         print(n, "is odd")

# check_odd_even(n)  # Call the function with the input
# Recursive function
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("STOP")
# show(5)    

# recursive factorial
# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n
# print(fact(4))
# Write a recursive function to calculate the sum of the first natural numbers
# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n
# sum = calc_sum(5)
# # print(sum)
# Write a recursive function to print all elements in a list
# def print_list(list, idx = 0):
#     if(idx ==len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)
# fruits =["mango","banana","apple"]   
# print_list(fruits) 