# restudy of python programming
# Jeo-Criz Izzack E. Perdio
# Data Science

# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. duplicates OK
#   Set   = {} unordered and immutable. but add/rempve OK. No duplicates
#   Tuple = () ordered and unchangeable. Duplicate OK. Faster

print("List")
fruits = ["apple", "Orange", "banana", "coconut"] # if we add a value of "coconut" it will print in 2 coconut

#print(dir(fruits)) by using this we can see other plausible function to use in list
#print(help(fruits)) by using help function we can view not only the function available in our list but also its explanation

print("\n")

print(len(fruits)) # this is to know the length of our list

print("\n")

print("apple" in fruits) # this is a boolean method which question the list if the apple is inside the list which is there so the result will be true otherwise if other value wasnt inside the list it will print the value in false

print("\n")

fruits[0] = "pineapple" # this will add a new value inside the list base at the location of index

fruits.append("papaya") # unlike the upper code, this code is the formal way of adding a new value however in this the added value will be place in last and the first will remain the same

fruits.remove("apple") # this will remove the value specified inside the parenthesis

fruits.insert(0, "grapes") # just like the pineapple this will method will add a new value at the specified index

fruits.sort() # this will sort the value in alphabetical order

fruits.reverse() # like index operator in reversing the iterate this .reverse will also reverse the list 

#also noted by combining the .sort and .reverse this will not only sort the data alphabetically but also reverse them

fruits.clear() # this will erase all of the value inside the list

print(fruits.index("apple")) # this method is the kabaligtaran of the [0] which in here if we select a value such as the "apple" it will print in 0 also if the value is not found in the list it will result in error

print(fruits.count("banana")) # this will print on how many banana like value is inside the list 1 if the value selected is not found like "meat" it will result in 0 instead of error

# by using the index operator like array we can call the list like [0] for apple
# [0: 2] = apple, orange, banana or you can use the skip [0: 3: 1] this will skip by 1
print(fruits[::-1]) # in here as you can see I use a reverse iterator so I can reverese the item in list

print("\n")

# by using the for loop like its use for i these can also iterate the value inside the list
for fruit in fruits:
    print(fruit)


print("\n")


print("Set")
fruty = {"apple", "orange", "banana", "coconut"} # if we add another "coconut" this will only print one coconut
#print(dir(fruty)) like the dir in list this will also show the plausible function
# help als has the same function

print(len(fruty)) #this will print the length of the Set

print("grape" in fruty) # like the in the list the set also has the same method they print a boolean depending on the specified value like if it is inside it will print true while if the value is not it will print in false

# we cant use the index operator []

fruty.add("pineapple") # this will add the value inside the Set

fruty.remove("apple") # this will remove the  apple value inside the Set

fruty.pop() # this will pop the first value inside the Set however since this is Set it will be in random

fruty.clear() # this will clear the value of Set

print(fruty) # unlike the list the set will print the fruty value in unordered random of the value inside the Set


print("\n")


print("Tuple")
fruited = ("apple", "orange", "banana", "coconut") # a duplicate value can also print

#print(dir(fruited)) like the dir in other method
# help like the other

print(len(fruited)) # this will print the lenght of our Tuple

print("\n")

print("apple" in fruited) # just like the other this will print in True since the value exist inside the tuple however if not exist it will print in false

print(fruited.index("apple")) # this will print the location of the value inside the tople which the apple is 0 if we try other value like "orange" then the result is 1

fruited.count("coconut") #this will print if the specified value in how many it exist inside the Tople which in here is 1 coconut inside the tople if we add another cocnonut then this will be in 2

# this will iterate the tople like the list
for fruts in fruited:
    print(fruts)
