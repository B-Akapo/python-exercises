# Description: Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
# Date: 16th June 2024

import math


def main():
    x_name = "first number"
    y_name = "second number"

    x, y = get_positive_integer(x_name, y_name)
    result = find_gcd(x, y)
    print(f"The GCD of {x} and {y} is: {result}")


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


def find_gcd(num1, num2):
    gcd_result = math.gcd(num1, num2)
    return gcd_result


if __name__ == "__main__":
    main()
