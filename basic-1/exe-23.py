# Description: Write a Python program to get n (non-negative integer) copies of the first 2 characters of a string.
# Return n copies of the whole string if the length is less than 2.
# Date: 15th June 2024

def main():
    """
    Main function that orchestrates the program flow.
    It gets a non-negative integer from the user and prints the result of creating copies based on the input.
    """
    n = get_positive()  # Get non-negative integer from user
    result = create_copies(n)  # Create copies based on the input number
    print(f"Copies: {result}")


def get_positive():
    """
    Function to prompt the user for a non-negative integer input.
    It continues prompting until a valid input is provided.
    """
    while True:
        try:
            userinput = int(input("Please enter a non-negative integer: "))
            if userinput > 0:
                return userinput
            else:
                print("This is not a non-negative integer")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def create_copies(n):
    """
    Function to create copies of the first 2 characters of a string or the whole string if its length is less than 2.

    Parameters:
    - n: The number of copies to create.

    Returns:
    - String: The resulting string with n copies.
    """
    string_value = input("Please enter a word: ")
    if len(string_value) >= 2:
        first_two_chars = string_value[:2]
        char_copies = first_two_chars * n  # Return n copies of the first two characters
        return char_copies
    else:
        return string_value * n  # Return n copies of the whole string if length is less than 2


if __name__ == "__main__":
    main()
