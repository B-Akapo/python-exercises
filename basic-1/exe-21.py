# Description: Write a Python program that determines whether a given number (accepted from the user) is even or odd,
# and prints an appropriate message to the user.
# Date: 15th June 2024

def main():
    """
    The main function that orchestrates the flow of the program.
    It gets a number from the user and determines if it is even or odd.
    """
    number = get_number()  # Get a valid number from the user
    if is_even(number):  # Check if the number is even
        print(f"{number} is even")
    else:  # If the number is not even, it is odd
        print(f"{number} is odd")


def get_number():
    """
    Prompts the user to enter a number. Keeps prompting until a valid integer is entered.
    Returns the valid integer entered by the user.
    """
    while True:
        user_input = input("Please enter a number: ")
        try:
            x = int(user_input)  # Try to convert the input to an integer
            return x  # Return the integer if successful
        except ValueError:
            print("That's not a valid number. Please try again.")  # Handle the case where the input is not a valid integer


def is_even(num):
    """
    Determines if a given number is even.
    Returns True if the number is even, otherwise returns False.
    """
    return num % 2 == 0  # Check if the number is evenly divisible by 2


# This ensures that the main function is called only when this script is executed directly,
# and not when it is imported as a module in another script.
if __name__ == "__main__":
    main()
