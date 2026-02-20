# ##2.1
# n = 42
# print(n) #legal 

# 42 = n
# print(42) #SyntaxError 

##2.2 
# x = y = 1
# print(y) 
#x,y has used as a valiables 
#2.3
# a = 10;
# print(a)
#codder do't use semicolone at the end of statements. 

#2.4
# x = 1.
# print(x)

#2.5

# x = 1
# y = 2
# # print(xy) #Sytex Error 
# print(x*y) #This is correct way 

#2.6
# import math
# r = 5
# volume = (4/3)* math.pi * r**3
# print(volume)

# 2.7 
start_hour = 6
start_minute = 52

easy = 8 * 60 + 15
tempo = 7 * 60 + 12
total_seconds = easy + (3* tempo) + easy
minutes = total_seconds // 60
seconds = total_seconds % 60
end_minute = start_minute + minutes
end_hour = start_hour + end_minute // 60
end_minute = end_minute % 60

print("You get home at:", end_hour, ":" ,end_minute, ":", seconds, "AM") 