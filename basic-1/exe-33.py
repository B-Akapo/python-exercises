# Description: Write a Python program to sum three given integers.
# However, if two values are equal, the sum will be zero.
# Date: 16th June 2024

def main():
    """
    Main function to execute the program.
    It calls get_sum() and prints the result.
    """
    result = get_sum()  # Call the get_sum function and store the result
    print(result)  # Print the result


def get_sum():
    """
    Function to calculate the sum of three integers with a specific condition.
    If any two of the integers are equal, the function returns 0.
    """
    x, y, z = 2, 2, 2  # Assigning values to x, y, z (can be replaced with user input)

    # Check if all three integers are equal
    if x == y == z:
        return 0  # If all are equal, return 0 as per the condition
    else:
        return x + y + z  # If not all are equal, return the sum of x, y, z


if __name__ == '__main__':
    main()  # Call the main function if this script is run directly
