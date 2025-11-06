
#10#1

print("hello world")

print("\n")

#2
a, b = input("Enter a number (a + b): ").split()

a = int(a)
b = int(b)

print("Sum = {res}".format(res=(a+b)))

print("\n")


#3
odd_even = int(input("Enter a number: "))

if (odd_even % 2 == 0):
    print(f"{odd_even} is odd")
else:
    print(f"{odd_even} is even")


print("\n")


#4
q, w, e = input("Enter three numbers: ").split()

q = int(q)
w = int(w)
e = int(e)

larg = max(q, w, e)

print(f"The largest is {larg}.")

print("\n")


#5
c = int(input("Enter temperature in celsius: "))

f = ((c*(9/5)) + 32)

print(f"Temperature in Fahrenheit: {f:.1f}")


print("\n")


#6
multip = input("Enter a number: ")

for i in range(1, 11):
    print(f"{multip} x {i} = {multip*i}")


print("\n")


#7
import math

fact = int(input("Enter a number: "))

result = 1
for i in range(1, fact + 1):
    result *= i
print(f"Factorial = {result}")
    

print("\n")


#8
vow = input("Enter a word: ").lower()
vowel = "aeiou"
count = 0

for char in vow:
    if char in vowel:
        count += 1
print(f"Vowel Count: {count}")


print("\n")


#9
n = list(map(int, input("Enter numbers separated by spaces: ").split()))
small = min(n)

print(f"Smallest number: {small}")


print("\n")


#10
pal = input("Enter a palindrome: ").lower()

p = pal[::-1]

if pal == p:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")