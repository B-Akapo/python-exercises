# Description: Write a Python program to sum two given integers.
# If the sum is between 15 and 20 (inclusive), return 20.
# Date: 16th June 2024

def main():
    """
    Main function to execute the program.
    Calls get_sum() with example values (10, 12) and prints the result.
    """
    result = get_sum(10, 12)
    print(result)


def get_sum(x, y):
    """
    Function to calculate the sum of two integers x and y.
    If the sum is between 15 and 20 (inclusive), return 20.
    Otherwise, return the actual sum of x and y.
    """
    add_numbers = x + y

    # Check if the sum is between 15 and 20 (inclusive)
    if 15 <= add_numbers <= 20:
        return 20
    else:
        return add_numbers


if __name__ == '__main__':
    main()