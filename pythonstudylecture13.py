# restudy of python programming
# Jeo-Criz Izzack E. Perdio
# Data Science

# while loop = execute some code WHILE some condition remains true

start = True

while start:
    name = input("Enter your name: ")

    if name == "":
        print("No name has been entered")
    else:
        print(f"hello {name}")
    
    pick = input("Would you want to continue? (Yes/No): ").capitalize #I use the string method .capitalize to always capitalize the first letter of the word

    if pick == "No":
        start = True
        print("thank you for using the program")
    else:
        start = False
    
    #you can use this one line coding
    #pick = input("Would you want to continue? (Yes/No): ").capitalize(), start = True if pick == "No" else True

#or you can use this
#name = input("Enter your name: ")
#while name == "":
#    print("Ypu did not enter the name")
#    name = input("Enter your name: ")
#print(f"Hello {name}")


# infinite loop
#name = input("Enter your name: ")
#while name == "":
#    print("Ypu did not enter the name")
#print(f"Hello {name}")

print("\n")


#age it will return as True unless the user inputed a positive number
age = int(input("Enter your age: "))

while age < 0:
    print("Age cant be negative")
    age = int(input("Enter your age: "))

print(f"Your age is {age}")

print("\n")


food = input("Enter a food you like (x to exit): ").lower()
#we use the not logical operator to invert the value
while not food == "x":
    print(f"YOur food is {food}")
    food = input("Enter a food you like (x to exit): ").lower()
print("thank you")

print("\n")


num = int(input("Enter a number between 1-10: "))

while num < 1 or num > 10:
    print(f"Num is not valid")
    num = int(input("Enter a number between 1-10: "))

print(f"Your number is {num}")

