# Description: Write a  Python program that accepts the user's first and last name and
# prints them in reverse order with a space between them.
# Date: 11th June 2024

# get users name
fullname = input("Please enter your first and last name: ")

# split the names
names = fullname.split(" ")

# print userinput
print(fullname)

# reverse the name
print(f"{names[1]} {names[0]}")
