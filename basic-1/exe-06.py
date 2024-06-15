# Description: Write a Python program that accepts a sequence of comma-separated numbers from the user
# and generates a list and a tuple of those numbers.
# Date: 11th June 2024

# get user input
user_input = input("Please enter 5 numbers separated by a comma: ")

# split the user input into a list
numbers = user_input.split(",")

# create a new list without commas
new_list = []
for number in numbers:
    new_list.append(number.strip())  # strip() removes leading and trailing spaces

# convert list to a tuple
new_tuple = tuple(new_list)

print(new_list)
print(new_tuple)

