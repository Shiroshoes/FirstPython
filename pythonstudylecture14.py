# restudy of python programming
# Jeo-Criz Izzack E. Perdio
# Data Science

# for loops = execute a block of code a fixed number of times.
#             you can iterate over a range, string, sequence, etc.

#for counter in range(start, end): this method will count the number from 1 to 10
for x in range(1, 11):
    print(x)

print("\n")

#reversed function to reverse the count of range
for new in reversed(range(1, 11)):
    print(new)
print("Happy New Year")

print("\n")

#in here we use the range(start, end, step) as usual the step is like a modulo where in we skip according to the value it placed
for b in range(1, 11, 2):
    print(b)

print("\n")

#iterating string with a for loop
credit_card = "1234-5678-9012-3456"
for d in credit_card:
    print(d)

print("\n")

#by using the continue this will skip the 13 number and continue counting
for a in range(1, 21):
    if a == 13:
        continue
    else:
        print(a)

print("\n")

#break will break the iteration/loop this will count from 1-12
for c in range(1, 21):
    if c == 13:
        break
    else:
        print(c)