# Description: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Date: 11th June 2024

# get user input
n = input("please enter the value of n: ")

n1 = n + n
n2 = n + n + n

result = int(n) + int(n1) + int(n2)

print(result)
