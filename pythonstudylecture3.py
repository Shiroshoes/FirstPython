# restudy of python programming
#Jeo-Criz Izzack E. Perdio
# Data Science

#input() = i a function that prompts the user to enter a data
# it returns the entered data as a string

print("input() function")
condition = input("How are you are you okay? ")

if condition == "yes":
    print("That's nice")
else:
    print("My bad")

print("\n")
name = input("What is your name? ")
age = input("How old are you? ")
print(f"Hi {name}!!")
print(f"nice you are {age} years old")

print("\n")

#Converting the string to int
print("Converting the string to int")
print("Happy Birthday!!")
#To convert the input that is always string you can use typecasting
#We have two method of changing the string the first one is shorter
Age = int(age) + 1
#the second one is longer
#old = int(age)
#Age = old + 1
print(f"You are now {Age} years old")

# We can also use the most shorter method of converting the data if we wont used them to string type data
AGE = int(input("Hi how old are you? "))
AGe = AGE + 1
print(f"Hi I am {AGE} turning {AGe} years old")

print("\n")

#RECtangle area calc
print("Solvingf the rectangle area")
lenght = input("Enter the Lenght: ")
width = input("Enter the width: ")

area = float(lenght) * float(width)
#To achieve the square here is the windows key: NumLk + Alt + 0178
print(f"the area is {area}cm²")

print("\n")

#Shopping
print("Welcome to JCI store")
item = input("What item are you buying: ")
pricing = float(input("How much wass it: "))
quanTity = int(input("How many are they: "))
total = pricing * quanTity

print(f"Reciept",
      f"Product: {item}",
      f"Price: {pricing}",
      f"Quantity: {quanTity}",
      f"---------------------",
      f"Total: {total}",
      f".",
      f"Thank you for Purchase")