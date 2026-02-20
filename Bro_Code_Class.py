# While loops
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name.")
    name = input("Enter your name: ")

print(f"Hello {name}") 
# 


# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative.")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old.") 

# food = input("Enter a food you like or (q to quit): ")

# while not food == "q":
#     print(f"You like {food}.")
#     food = input("Choose another food you like or (q to quit): ")

# print("Bye")    


#Python compound interest calculator
# principle = 0
# rate = 0
# time = 0

# while True:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle can not be less than or equal to zero")
#     else:
#         break

# while True:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interest rate can not be less than or equal to zero")
#     else:
#         break

# while True:
#     time = int(input("Enter the time: "))
#     if time <= 0:
#         print("Time can not be to zero")
#     else:
#         break

# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time} years/s: ${total:.2f}")

##For loops
# Count Down Clock
# import time
# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIMES UP!!")    
   