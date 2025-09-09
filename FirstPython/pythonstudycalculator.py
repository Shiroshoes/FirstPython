# restudy of python programming
#Jeo-Criz Izzack E. Perdio
# Data Science


#Calculator program python
print("Calculator program python")
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st Number: "))
num2 = float(input("Enter the 2nd Number: "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print("Error please input an operator")

# you can also use this, the most clean way
#if operator == '+':
#    result = num1 + num2
#    print(result)
#elif operator == '-':
#    result = num1 - num2
#    print(result)
#elif operator == '*':
#    result = num1 * num2
#    print(result)
#elif operator == '/':
#    result = num1 / num2
#    print(result)
#else:
#    print("Error please input an operator")


#Python weight converter
print("\n")

print("Python weight converter")

weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds (K or L): ")

if unit == 'K':
    weight = weight * 2.20462
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == 'L':
    weight = weight / 2.20462
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print("Error no unit is inputed")


#Temperature conversion program
print("\n")

print("Temperature conversion program")

un = input("Is this the temperature in Celsius or Farenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if un == 'C':
    temp = round((temp * 9)/5 + 32, 1)
    print(f"The temp in Farenheit is: {temp} F")
elif un == 'F':
    temp = round((temp - 32) * 5/9, 1)
    print(f"The temp in Celcius is: {temp} C")
else:
    print("Error unit not found")