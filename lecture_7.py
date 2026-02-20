# Let's prectice:
# Creat a new file "prectice.txt" using python.Add the flowing data in it:
# Hi evereone
# we are learning File I/O
# using Java
# I like programming in Java
# # solution:
# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in Java.")

# # WAF (Write A Function) that replaces all occurrences of "Java" with "Python" in the file.

# def replace_occurrences():
#     with open("practice.txt", "r") as f:
#         data = f.read()

#     new_data = data.replace("Java", "Python")

#     with open("practice.txt", "w") as f:
#         f.write(new_data)

#     print(new_data)  # Optional: print the updated content


# # Call the function
# replace_occurrences()
      
    


# Search if the word "learning" exists in the File or not

def check_for_word():
    word = "my"
    data = True
    with open("practice.txt","r") as f:
        while data:
            data = f.read()
            if(word in data):
                print("Found")
                return
            else:
                print("Not Found")
check_for_word()                

  