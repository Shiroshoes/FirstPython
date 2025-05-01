# restudy of python programming
#Jeo-Criz Izzack E. Perdio
# Data Science


#Calculator program python

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