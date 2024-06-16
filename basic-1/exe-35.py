# Description: Write a Python program that returns True if the two given integer values are equal,
# or if their sum or difference is 5.
# Date: 16th June 2024

def main():
    """
    Main function to execute the program.
    Demonstrates the usage of get_sum() with example values (27, 53) and prints the result.
    """
    x = 27
    y = 53
    result = get_sum(x, y)
    print(f"The result is {result}")


def get_sum(x, y):
    """
    Function to check if two given integers x and y satisfy any of the following conditions:
    - They are equal
    - Their sum is 5
    - Their absolute difference is 5
    Returns True if any condition is satisfied, otherwise returns False.
    """
    total_sum = x + y
    diff = x - y

    # Condition 1: Check if x and y are equal
    if x == y:
        return True

    # Condition 2: Check if the sum of x and y is 5
    elif total_sum == 5:
        return True

    # Condition 3: Check if the absolute difference between x and y is 5
    elif abs(diff) == 5:
        return True

    # If none of the conditions are met, return False
    else:
        return False


if __name__ == '__main__':
    main()
