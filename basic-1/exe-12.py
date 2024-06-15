# Description: Write a Python program that prints the calendar for a given month and year.
# Date: 12th June 2024

import calendar

# take user input
theyear = int(input("Please enter the year: "))
themonth = int(input("Please enter the month: "))
theday = int(input("Please enter the day: "))


print(calendar.month(theyear, themonth))


