# Description: Write a Python program that computes the lowest common divisor (LCM) of two positive integers.
# Date: 16th June 2024

import math


def main():
    x_name = "first number"
    y_name = "second number"

    x, y = get_positive_integer(x_name, y_name)
    result = find_lcm(x, y)
    print(f"The LCM of {x} and {y} is: {result}")


def get_positive_integer(x_name, y_name):
    while True:
        try:
            x_str = input(f"Please enter a positive integer for {x_name}: ")
            y_str = input(f"Please enter a positive integer for {y_name}: ")

            # Check if inputs contain only digits
            if not x_str.isdigit() or not y_str.isdigit():
                print("Please enter integers only.")
                continue

            # Convert inputs to integers
            x = int(x_str)
            y = int(y_str)

            # Check if inputs are positive
            if x <= 0 or y <= 0:
                print("Please enter positive values only.")
                continue

            # If all checks pass, return x and y
            return x, y

        except ValueError:
            print("Please enter integers only.")


def find_lcm(num1, num2):
    lcm_result = math.lcm(num1, num2)
    return lcm_result


if __name__ == "__main__":
    main()
