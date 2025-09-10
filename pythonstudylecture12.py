# restudy of python programming
# Jeo-Criz Izzack E. Perdio
# Data Science

# format specifiers = {:flags} format a value base on what the flag are inserted

# :.(number)f = round to that many decimal places (a fixed point)
# :(number) = allocate that many spaces for the value (minimum width)
# :03 = allocate and zero pad to that many spaces (minimum width)
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use a plus sign to indicate positive values
# := = place the sign to the left most position
# : = insert a space before the positive numbers and a minus sign before negative numbers
# :, = use a comma as a thousands separator


price1 = 49.14159
price2 = -9.99
price3 = 999.99

print("This will display decimal places in two places")
print(f"Price1: ${price1:.2f}") # this will round the number to two decimal places 10.00
print(f"Price2: ${price2:.2f}") # Result = Price2: $-9.99
print(f"Price3: ${price3:.2f}")

#you can change the number of decimal places like this {price1:.3f} # this will round the number to three decimal places 10.000

print("\nThis will allocate spaces for the value")
print(f"Price1: ${price1:10}") # the result will have a 10 space gap to the printed provided like Price1: $          49.14159
print(f"Price2: ${price2:10}")
print(f"Price3: ${price3:10.3f}")

#you can also add a decimal value like {price1:10.2f}

print("\nzero padded")
print(f"Price1: ${price1:010}") # Result = Price1: $0049.14159
print(f"Price2: ${price2:010}") # Result = Price2: $-000009.99
print(f"Price3: ${price3:010}") # Result = Price3: $0000099.99


print("\nleft justified")
print(f"Price1: ${price1:<10}") # Result = Price1: $49.14159
print(f"Price2: ${price2:<10}") # Result = Price2: $-9.99
print(f"Price3: ${price3:<10}") # Result = Price3: $99.99


print("\nright justified")
print(f"Price1: ${price1:>10}") # Result = Price1: $  49.14159
print(f"Price2: ${price2:>10}") # Result = Price2: $     -9.99
print(f"Price3: ${price3:>10}") # Result = Price3: $     99.99


print("\n positive value")
print(f"Price1: ${price1:+}") # Result = Price1: $+49.14159
print(f"Price2: ${price2:+}") # Result = Price2: $-9.99
print(f"Price3: ${price3:+}") # Result = Price3: $+99.99


print("\n space")
print(f"Price1: ${price1: }") # Result = Price1: $ 49.14159
print(f"Price2: ${price2: }") # Result = Price2: $-9.99 # sign was not included to the space
print(f"Price3: ${price3: }") # Result = Price3: $ 99.99


#thousand comma
price4 = 90010.9134
print("\nComma")
print(f"Price4: ${price4:,}") # Result = Price4: $90,010.9134
# you can use the {price4:+,.2f} the result is $+90,010.91