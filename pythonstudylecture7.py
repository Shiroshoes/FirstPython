# restudy of python programming
#Jeo-Criz Izzack E. Perdio
# Data Science

#Logical operators - was used to  evaluate multiple conditions like (or, and, not)
# or - is a condition that must be true
# and - a symbol that signifies that both conditions must be true
# not - inverts the condition like (not false, not true)

temp = 30
is_rain = False

print("or - Logical operator \n")
# the 'or' logical operator, signifies that if both of the statement is true or each one of them is true then--
# we can consider the statement to be true.
if temp > 35 or temp < 0 or is_rain:
    print(f"The outdoor event is cancelled as the temp is {temp}")
else:
    print("The outdoor event will continue")


print("\n")

print("and - Logical operator \n")
tempi = 20
is_sun = True
# In 'and' logical operator, has a rule that both condition must be true else it will not--
# accept the condition and print the next condition.
if tempi >= 28 and is_sun:
    print("It is hot")
elif tempi <= 0 and is_sun:
    print("it is cold")
elif 28 > tempi > 0 and is_sun:
    print("The weather is normal outside")
else:
    print("go check outside >:{")

#if tempi 28 and is_ sun: then for example here if the tempi is 25 and is_sun is True this condition will not push--
#through so the both condition must be in the define specific value which is 28 and True.

print("\n")

# The 'not' logical operator invert the condition if the condition is true it will become false--
# otherwise if it's false it will become true.
#in this sample if we change the value of is_sun to False it will print the latter or the not operator condition.
print("not - Logical operator \n")
if tempi >= 28 and is_sun:
    print("It is hot")
elif tempi <= 0 and is_sun:
    print("it is cold")
elif 28 > tempi > 0 and is_sun:
    print("The weather is normal outside")
elif tempi >= 28 and not is_sun:
    print("It is hot and cloudy")
elif tempi <= 0 and not is_sun:
    print("it is cold and cloudy")
elif 28 > tempi > 0 and not is_sun:
    print("The weather is normal outside but cloudy")
else:
    print("go check outside >:{")