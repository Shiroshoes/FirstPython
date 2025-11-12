# restudy of python programming
# Jeo-Criz Izzack E. Perdio
# Data Science

# dICTIONARY IS LIKE THE OBJECT OF JAVASCRIPT THE PRINCIPLE

#  PYTHON LESSON: DICTIONARY
# -----------------------------------
# A dictionary is a collection of key-value pairs.
# You use it to store data that’s connected — like a real dictionary (word → meaning).

# Example
person = {
    "name": "Jeo",
    "age": 20,
    "city": "Manila"
}

# Keys are: "name", "age", "city"
# Values are: "Jeo", 20, "Manila"


# -----------------------------------
# SYNTAX
# dictionary_name = { key1: value1, key2: value2, ... }

# Keys must be unique and immutable (string, number, tuple)
# Values can be any data type


# -----------------------------------
# CREATING DICTIONARIES

# 1. Using curly braces
student = {"name": "John", "age": 21, "course": "Data Science"}

# 2. Using dict() function
student2 = dict(name="Jane", age=22, course="AI")


# -----------------------------------
# 🔍 ACCESSING VALUES

print(student["name"])     # Output: John
print(student.get("age"))  # Output: 21

# .get() is safer — it won’t cause an error if key doesn’t exist
print(student.get("grade"))  # Output: None


# -----------------------------------
# ✏️ CHANGING OR ADDING VALUES

# Change existing value
student["age"] = 22

# Add new key-value pair
student["grade"] = "A"


# -----------------------------------
# REMOVING ITEMS

# pop() - removes key and returns its value
student.pop("course")

# del - deletes a key
del student["age"]

# clear() - removes everything
# student.clear()


# -----------------------------------
# DICTIONARY OPERATIONS

# len() - number of key-value pairs
print(len(student))

# in - check if a key exists
print("name" in student)  # True


# -----------------------------------
# LOOPING THROUGH A DICTIONARY

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(key, ":", value)


# -----------------------------------
# NESTED DICTIONARIES
students = {
    "student1": {"name": "John", "age": 21},
    "student2": {"name": "Mary", "age": 22}
}

print(students["student1"]["name"])  # Output: John


# -----------------------------------
# DICTIONARY METHODS SUMMARY
# clear() - Removes all elements
# copy() - Returns a shallow copy
# fromkeys() - Creates a dictionary from keys
# get(key) - Returns value of key
# items() - Returns key-value pairs
# keys() - Returns all keys
# pop(key) - Removes key and returns its value
# popitem() - Removes last inserted pair
# setdefault(key, value) - Adds key if not present
# update() - Adds items from another dictionary
# values() - Returns all values


# -----------------------------------
# EXAMPLE PROGRAM
inventory = {
    "apple": 50,
    "banana": 25,
    "orange": 30
}

# Add a new item
inventory["mango"] = 40

# Update a value
inventory["apple"] = 60

# Remove an item
inventory.pop("banana")

# Print all items
for fruit, qty in inventory.items():
    print(f"{fruit}: {qty}")

# Output:
# apple: 60
# orange: 30
# mango: 40