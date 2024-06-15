# Description: Write a Python program to print all even numbers from a given list of numbers in the same order.
# Stop printing any after 237 in the sequence.
# Date: 15th June 2024

def main():
    # List of numbers to check
    numbers = [
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 743, 527
    ]
    # Call function to print even numbers until 237
    print_even_until_237(numbers)


def print_even_until_237(num_list):
    """
    Prints all even numbers from a given list in the same order until the number 237 is encountered.

    Args:
        num_list (list): List of integers to check.
    """
    # Iterate through each number in the list
    for num in num_list:
        # If the number 237 is encountered, stop processing
        if (num == 237):
            break
        # If the number is even, print it
        if (num % 2 == 0):
            print(num)


if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
