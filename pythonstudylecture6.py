# restudy of python programming
#Jeo-Criz Izzack E. Perdio
# Data Science

#If else statement
# if = is a  code only IF some condition is true
# elif = if the condition is two or more
# Else = do something else

age = int(input("Enter your age: "))

#If you ever forget or confuse the greater than is this (>) and less than is this (<)
if 18 <= age  <= 100:
    #Always indent the instance if you want them to be inside the "if"
    print("You have now the credibility to signed up")
elif age < 0:
    print("you are not born yet")
elif age >= 100:
    print("too old to sign up")
else:
    print("Sorry you're not old enough, you must be 18+ to sign up")


print("\n")

print("New")

response = input("Would you like to eat food? (Y/N): ")

if response == "Y":
    print("Here's a food")
else:
    print("Thank you for answering")

print("\n")

print("New")
name = input("Enter your name: ")

if name == "":
    print("No name have been entered")
else:
    print(f"Hello {name}")

print("\n")

print("New")

sale = bool(input("Enter True if for sale, Enter false if otherwise: "))

if sale:
    print("The item is for sale")
else:
    print("The item is not for sale")