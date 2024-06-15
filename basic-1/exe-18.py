# Description: Write a Python program to calculate the sum of three given numbers.
# If the values are equal, return three times their sum.
# Date: 12th June 2024

def main():
    # Get three positive numbers from the user and calculate the result
    numbers_list = convert_to_positive()
    result = calculate_sum(numbers_list)
    print(f"Result = {result}")


def convert_to_positive():
    # Prompt the user to enter three positive numbers and store them in a list
    number_list = []
    for i in range(3):
        num = int(input("Please enter a number: "))
        number_list.append(abs(num))  # Convert negative numbers to positive using abs() function
    return number_list


def calculate_sum(numbers_list):
    # Calculate the sum of the numbers in the list
    sums = sum(numbers_list)

    # Check if all numbers in the list are equal
    if all(x == numbers_list[0] for x in numbers_list):
        # If all numbers are equal, return three times their sum
        return 3 * sums
    else:
        # If numbers are not equal, return their sum
        return sums


if __name__ == '__main__':
    # Execute the main function
    main()
