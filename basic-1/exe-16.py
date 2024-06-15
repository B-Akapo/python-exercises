# Description: Write a Python program to calculate the difference between a given number and 17.
# If the number is greater than 17, return twice the absolute difference.
# Date: 12th June 2024

def main():
    """
    Main function to execute the program logic.
    """
    number = get_positive_integer()
    difference = calculate_difference(number)
    print(f"The calculated difference is: {difference}")


def get_positive_integer() -> int:
    """
    Prompt the user to enter a positive integer. Repeats until a valid positive integer is entered.

    Returns:
        int: The positive integer entered by the user.
    """
    while True:
        try:
            number = int(input("Please enter a positive integer: "))
            if number <= 0:
                print("Please enter a positive number.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def calculate_difference(number: int) -> int:
    """
    Calculate the difference between the given number and 17.
    If the number is greater than 17, return twice the absolute difference.
    Otherwise, return the absolute difference.

    Args:
        number (int): The number to compare with 17.

    Returns:
        int: The calculated difference based on the specified rules.
    """
    diff = 17 - number
    if number > 17:
        return 2 * abs(diff)
    else:
        return abs(diff)


# Execute the main function
if __name__ == "__main__":
    main()
