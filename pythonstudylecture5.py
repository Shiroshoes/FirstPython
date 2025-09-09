# restudy of python programming
#Jeo-Criz Izzack E. Perdio
# Data Science

#Arithmetic Function
print("Arithmetic Function")

print("\n")

#addition operator
print("Addition")
friend = 0
friends = friend + 1
print(friends)

# Augmented assign operator
print("Augmented")
friend += 1
print(friend)

print("\n")

#Subtraction assign operator
print("Subtraction")
friend1 = friend - 2
print(friend1)

# Augmented assign operator
print("Augmented")
friend -= 2
print(friend)

print("\n")

#Multiplication assign operator
friendie = 5

print("Multiplication")
friend2 = friendie * 4
print(friend2)

# AUgmented assign operator
print("Augmented")
friendie *= 4
print(friendie)

print("\n")

#Division assign operator
friende = 10

print("Division")
friend3 = friende / 2
print(friend3)

print("Augmented")
friende /= 2
print(friende)

print("\n")

#Exponent assign operator
friendi = 3

print("Exponent")
friend4 = friendi ** 2
print(friend4)

print("Augmented")
friendi **= 2
print(friendi)

print("\n")

#Modulo assign operator
remain = friendi % 2
print(remain)

print("Augmented")
friendi %= 2
print(friendi)

print("\n")

#XYC arithmetic
x = 3.14
y = 4
z = 5

#rounding the number/value
print("Round Number")
result = round(x)
print(result)

print("\n")

#Absolute value
print("Absolute value")
res = abs(y)
print(res)

print("\n")

#Power function
print("power function")
output = pow(z, 3)
print(output)

print("\n")

#Maximum Value
print("Maximum")
ma = max(x, y, z)
print(ma)

print("\n")

#Minimum Value
print("Minimum")
mi = min(x, y, z)
print(mi)

print("\n")

#importing a math module to add new feature
import math

x = 9
y = 9.4

print("pi")
print(math.pi)

print("\t")

print("Exponential constant 'e' ")
print(math.e)

print("\t")

print("Square root")
resul = math.sqrt(x)
print(resul)

print("\t")

#rounding the number/value up
print("ceiling function")
resu = math.ceil(y)
print(resu)

print("\t")

#rounding the value down
print("Floor function")
res = math.floor(y)
print(res)

print("\n")

#radius A = 2πr
print("A = 2πr")
radius = float(input("Enter the radius circle: "))
circumference = 2 * math.pi * radius

print(f"the circumference is: {circumference}cm")
#print(f"the circumference is: {round(circumference)}cm")
#print(f"the circumference is: {round(circumference, 2)}cm")

print("\n")

#A = πr²
print("A = πr²")
rad = float(input("Enter the radius circle: "))

ar = math.pi * pow(rad, 2)
print(f"the area of the circle:{round(ar, 2)}cm")

print("\n")

# c = √a²+b²
print("c = √a²+b²")

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side c = {c}")