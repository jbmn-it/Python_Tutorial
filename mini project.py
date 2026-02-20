##### 
import random
target = random.randint(1, 10)

chances = 3  # Number of tries

while chances > 0:
    userchoice = input("Guess the number (1–10) or type 'Quit' to exit: ")

    if userchoice == "Quit":
        print("You chose to quit the game.")
        break

    userchoice = int(userchoice)

    if userchoice == target:
        print("Success: Correct Guess!! 🎉")
        break
    elif userchoice < target:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

    chances -= 1
    print(f"Tries left: {chances}")

if chances == 0:
    print(f"Game Over! The correct number was {target}.")


### Random Password

# import random
# import string

# pass_len = 20
# charValues = string.ascii_letters + string.punctuation + string.digits

# #list comprehension [function for i in range(n)]

# password = "".join([random.choice(charValues) for i in range (pass_len)])


# # password = ""
# # for i in range (pass_len):
# #     password += random.choice(charValues)

# print("Your password is :", password)