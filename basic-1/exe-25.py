# Description: Python program to check if a specified value is in a list of values.
# Date: 15th June 2024

def main():
    # List of values to check against
    my_list = [1, 5, 8, 3]

    # Get input value from user
    x = get_integer()

    # Check if x is in my_list and print result
    if x in my_list:
        print(f"The value {x} is in the list.")
    else:
        print(f"The value {x} is not in the list.")


def get_integer():
    """
    Function to get an integer input from the user.

    Returns:
        int: The integer value entered by the user.
    """
    num = int(input("Please enter the value to check: "))
    return num


if __name__ == "__main__":
    main()