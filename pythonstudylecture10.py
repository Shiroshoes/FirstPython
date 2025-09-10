# restudy of python programming
# Jeo-Criz Izzack E. Perdio
# Data Science


# indexing = accessing elements of a sequence using [] (indexing operator)
# [start:end:step] = slicing operator

credit_number = "1234-5678-9101-1121"
# the elements in a string are indexed starting from 0

print("Idexing the start and the end of a string")
print(credit_number[0])  # first element
print(credit_number[-1])  # last element as long as you use negative indexing

print("\n")

print("Slicing the string [start: end]")
print(credit_number[0:4])  # slicing first 4 elements, you can also use credit_number[:4] since the start is 0
print(credit_number[5:9])  # slicing middle 4 elements
print(credit_number[5:])  # slicing from the 5th index to the end

print("\n")

print("the step is like a module that will skip the elements according to the index provided")
print(credit_number[::2])  # slicing the whole string but skipping every 2nd element
print(credit_number[::3])  # slicing the whole string but skipping every 3rd element
print(credit_number[1::3])  # slicing the whole string but starting from index 1 and skipping every 3rd element

print(credit_number[::-1])  # slicing the whole string but reversing it as a whole

last_digit = credit_number[-4:]  # getting the last digit of the string
print(f"XXXX-XXXX-XXXX-{last_digit}")  # masking the credit card number except the last 4 digits
