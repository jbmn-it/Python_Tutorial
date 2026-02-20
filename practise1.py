####
import random
target = random.randint(1, 1000)
chances = 3

while chances > 0:
    userchoise = input("Guess the number (1-100) or 'Quit' to exit : ")
    if userchoise == "Quit":
        print("You chose to quit the game.")
        break

    userchoise = int(userchoise)
    if userchoise == target:
        print("Congratualation🎉You won the game!!")
        break

    elif userchoise < target:
        print("You number was too low!! Try higher number😊")

    else:
        print("Your number was too higher!! Try lower number😊")

    chances -= 1
    print(f"Your chances left:{chances}.")

if chances == 0:
    print(f"Game Over!! Correct number was:{target}.")


# import random
# import string
# pass_len = 20
# charValues = string.ascii_letters + string.punctuation + string.digits
# password = "".join([random.choice(charValues) for i in range(pass_len)])
# print(f"Your password is : {password}")
# ##
# import random
# import string
# pass_len = 5000
# charValues = string.ascii_letters + string.punctuation + string.digits
# password = "".join([random.choice(charValues) for i in range (pass_len)])
# print(f"Your password is : {password}")




# n = int(input("Enter a number :"))

# def check_odd_even(n):
#     if n % 2 == 0:
#         print(n," is even.")
#     else:
#         print(n, "is odd.")
        
# check_odd_even(n) 
# 
# #
# def check_password(password):
#     issues = []

#     if len(password) < 8:
#         issues.append("❌ Must be at least 8 characters long.")
#     if not any(char.isupper() for char in password):
#         issues.append("❌ Add at least one UPPERCASE letter.")
#     if not any(char.islower() for char in password):
#         issues.append("❌ Add at least one lowercase letter.")
#     if not any(char.isdigit() for char in password):
#         issues.append("❌ Add at least one number (0-9).")
#     if not any(char in "!@#$%^&*()_+-=[]{},.<>?/\\|" for char in password):
#         issues.append("❌ Add at least one special character (!, @, #, etc).")

#     if not issues:
#         print("✅ Strong password! Great job.")
#     else:
#         print("⚠️ Weak password. Suggestions:")
#         for problem in issues:
#             print(problem)

# password = input("Enter your password: ")
# check_password(password)

### Vowel Counter
# Count how many vowels are in a given string.

# text = input("Enter a string: ")

# vowel_count = 0
# vowels = "aeiouAEIOU"  

# for char in text:
#     if char in vowels:
#         vowel_count += 1

# print(f"Total number of vowels: {vowel_count}")



#### Palindrome Checker
# Check if a string reads the same forward and backward (like "madam").

# text = input("Enter a word: ")

# # স্ট্রিংটা ছোট হাতের করে নিই যেন তুলনা সহজ হয়
# text = text.lower()

# # স্ট্রিং উল্টে নিই
# reversed_text = text[::-1]

# if text == reversed_text:
#     print("It's a palindrome!")
# else:
#     print("Not a palindrome.")