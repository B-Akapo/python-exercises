# Description:  Write a Python program that returns a string
# that is n (non-negative integer) copies of a given string.
# Date: 12th June 2024

def main():
    """
    Main function to execute the program.
    """
    n = get_positive_input()  # Get the number of copies
    string_value = get_string()  # Get the input string
    if string_value:
        copies = copy_string(string_value, n)  # Generate copies of the input string
        print(copies)  # Print the resulting string
    else:
        print("Invalid input. Please try again.")


def get_positive_input():
    """
    Prompt the user to input a positive integer.
    Repeat until a positive integer is entered.
    """
    while True:
        try:
            x = int(input("Please enter a  number: "))
            if x <= 0:
                print("Please enter a only positive number")
            else:
                return x
        except ValueError:
            print("Please enter a valid number")


def get_string():
    """
    Prompt the user to input a single word.
    Repeat until a valid single word is entered.
    """
    while True:
        string_value = input("Please enter a word: ").strip()
        if len(string_value.split()) == 1:  # Check if there's only one word
            return string_value
        else:
            print("Please enter only one word.")


def copy_string(string_value, n):
    """
    Generate a new string by concatenating 'n' copies of the input string.

    Args:
        string_value (str): The input string.
        n (int): The number of copies.

    Returns:
        str: The resulting string consisting of 'n' copies of the input string.
    """
    copies = string_value * n
    return copies


if __name__ == "__main__":
    main()
