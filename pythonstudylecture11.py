# restudy of python programming
# Jeo-Criz Izzack E. Perdio
# Data Science

email = input("Enter your email address: ")

index = email.index("@")

username = email[:index] # from the start of the string to the index of "@"
#domain = email[index:]  from the index of "@" to the end of the string like this @gmail.com
domain = email[index + 1:] # from the index of "@" + 1 to the end of the string

# or you can use this shortcut
# username = email[:email.index("@")]
# domain = email[email.index("@") + 1:]

# or you can use this method
#username, domain = email.split("@") # this will split the string into two parts at the "@" character

print(f"Your username is {username} and your domain is {domain}")


