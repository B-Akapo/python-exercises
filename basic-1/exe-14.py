# Description: Write a Python program to calculate the number of days between two dates.
# Date: 12th June 2024

from datetime import date

# define the tuples
first_tuple = (2014, 7, 2)
second_tuple = (2014, 7, 11)

# Convert tuples to date objects directly
first_date = date(*first_tuple)
second_date = date(*second_tuple)

# Calculate the difference between the two dates
difference = abs(second_date - first_date)

# Print the result
print(f"The difference between the dates is: {difference.days} days")




