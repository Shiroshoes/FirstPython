# restudy of python programming
#Jeo-Criz Izzack E. Perdio
# Data Science

# printing
print("Hello World")
print('1\n')

#When renaming the variable, the following provided is the rule
#Use descriptive, concise, and meaningful names.
#Use lowercase with underscores for variable names (snake_case).
#Avoid single-letter names (except for counters like i, j).
#Don't use Python reserved keywords (like list, str, class, etc.).

#strings - a sequence of characters enclosed in either single quotes ('...') or double quotes ("...").
naruto = "Chakra"
family_position = "Eldest"
fam = "Family"

# to make an output of your string you can use the print("String") or use print(Variablename)
print(family_position)

# (f-string or formatted string) - was use to begin a string with f or F before opening--
# the quotation mark or triple the qoutation mark inside this string between {} are characters--
# can refer to variables or literal values.

print("f-string or formulated string")
print(f"Good morning, {family_position}")
print(f"low on {naruto}")
print(f"The {family_position} is low on {naruto}")

print("\n")

#Integers method
age = 19
quantity = 5
population = 500

print("Integers")
print(f"Hi I am {age} years old and I am the {family_position} in my {fam}")
print(f"I am buying {quantity} apples")
print(f"The campus has {population} students")

print("\n")

#Float method
price = 2000.00
gdp = 1000.00
height = 5.5

print("FLoat Method")
print(f"The RX-78 is ${price}")
print(f"The country's GDP is {gdp} Billion Dollars")
print(f"The average height of a student is {height}")

print("\n")

#Boolean
real = True # if you change this to False then the Else will be printed
fallacy = False

print("BOOLEAN method")
print(f"Is that news real? {fallacy}")
if real:
    print("Is that news real?")
else:
    print("That news is fake")
