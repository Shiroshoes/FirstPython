# restudy of python programming
# Jeo-Criz Izzack E. Perdio
# Data Science

#nested loop = is a loop within another loop (outer, inner)
#       outer loop:
#           inner loop:


#you can use the while inside while loop, for inside for loop, for inside while loop, while inside for loop

for x in range(3): # using this nested loop it will coubnt the y 3 times
    for y in range(1, 10): #1-9
        print(y, end="") # end="" will count the iteration in one line the empty string can also be input like end="-" the result will be 1-2-3-4
    print() #by using this it will print a new line after it finish counting the first 1-9 then repeat it until it print all of the iteration

print("\n")


row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
symbol = input("enter the symbol to use:")

for i in range(row):
    for j in range(column):
        print(symbol, end="")
    print()