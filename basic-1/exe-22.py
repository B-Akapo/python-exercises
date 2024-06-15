# Description: Write a Python program to count the number 4 in a given list.
# Date: 15th June 2024

def main():
    """
    The main function initializes the list and calls the count_list function
    to count the occurrences of the number 4 in the list.
    """
    my_list = [1, 4, 6, 4, 7, 4]
    result = count_list(my_list)
    print(result)


def count_list(numbers):
    """
    This function counts the occurrences of the number 4 in the provided list.

    Parameters:
    numbers (list): A list of integers to search through.

    Returns:
    int: The count of the number 4 in the list.
    """
    count_four = 0  # Initialize the count of 4's to 0
    for num in numbers:
        if num == 4:
            count_four += 1  # Increment the count when a 4 is found
    return count_four  # Return the total count of 4's


if __name__ == '__main__':
    """
    If this script is run directly, the main function is called.
    """
    main()
