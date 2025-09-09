
# restudy of python programming
# Jeo-Criz Izzack E. Perdio
# Data Science


# string methods

name = input("Enter your name: ")

# length = len(name) - this will return the length of the string
# Result = name.find("o") - this will return the index of the first letter "o"
# Result = name.rfind("o") - if the letter selecvted is not found it will return -1
# Result = name.capitalize() - this will capitalize the first letter of the string
# Result = name.upper() - this will convert all the letters to uppercase
# Result = name.lower() - this will convert all the letters to lowercase
# Result = name.isdigit() - this will return true if all the characters in the string are digits
Result = name.isalpha() # - this will return true if all the characters in the string are letters the space is not included


print(Result)


phone_number = "0917-1234-567"

result = phone_number.count("-")  # this will count how many times the character "-" appears in the string
new = phone_number.replace("-", " ")  # this will replace the character "-" with space " "


print(new)

#excercise
# ask the user to enter a username
# username must be at least 12 characters long
# username must only contain letters
# username must not contain spaces
# username must not contain digits

username = input("Enter your username: ")

if len(username) > 12 and username.isalpha() and " " not in username and not username.isdigit():
    print(f"{username} is a Valid username")
else:
    print("Invalid username")
