# restudy of python programming
# Jeo-Criz Izzack E. Perdio
# Data Science

#Python compound interest calculator

principle = 0
rate = 0
time = 0

#while principle <= 0:
while True:
    principle = float(input("Enter the principle amount: "))

    if principle < 0:
        print("Principle cant be less than zero")
    else:
        break
# if the while is True you are required to put a break at the to break the loop

while True:
    rate = float(input("Enter the rate rate: "))

    if rate < 0:
        print("rate cant be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))

    if time < 0:
        print("time cant be less than zero")
    else:
        break

print(principle)
print(rate)
print(time)

A = principle * pow((1 + rate/100), time)

print(f"Balance after {time} year/s: ${A:.2f}")