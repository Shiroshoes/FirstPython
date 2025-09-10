# restudy of python programming
#Jeo-Criz Izzack E. Perdio
# Data Science

# conditional expression - is a one-line shortcut for the if else statement (ternary operator)
# print or assign one of two values based on a condition X if condition else Y

num = 7
print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "odd"
print(result)

import math

a = 7
b = 8
c = 9
maxnum = a if a > b and c and b > a and c and c > a and b else max(a,b,c)
minnum = a if a < b and c and b < a and c and c < a and b else min(a,b,c)
print(maxnum)
print(minnum)


age = 19
stat = "Adult" if age >= 18 else "child"
print(stat)


temp = 35
weather = "hot" if temp >= 28 else "Warm"
print(weather)

userrole = "admin"
access = "Full access" if userrole == "admin" else "Limited Access"
print(access)