# Description: Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Date: 11th June 2024

import math

# set your PI value
pi_value = math.pi

#  get the value of the radius from the user
radius = float(input(" Enter the value of the radius: "))

# calculate the area of the circle
area_of_circle = pi_value * pow(radius, 2)

# print output
print(f"The area of the circle is {area_of_circle}")

