# Description: Write a  Python program that accepts a filename from the user and prints the extension of the file.
# Date: 11th June 2024

# get user input
filename = input("Please enter filename: ")

# split the filename using the period
split_filename = filename.split(".")

# get file extension
file_ext = split_filename[1]

print(f"This is a {file_ext} file")
