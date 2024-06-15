# Description: Python program to create a histogram from a given list of integers.
# Date: 15th June 2024

def create_histogram(data):
    """
    Creates a histogram string representation from a list of integers.

    Args:
    - data (list of int): List of integers representing the heights of histogram bars.

    Returns:
    - str: String representation of the histogram.
    """
    histogram = ""
    for height in data:
        histogram += "*" * height + "\n"  # Create a line of asterisks corresponding to the height and add newline
    return histogram


def main():
    histogram_list = [2, 3, 6, 5]  # List of integers representing the heights of histogram bars
    result = create_histogram(histogram_list)  # Call create_histogram function with histogram_list
    print(result)  # Print the resulting histogram string


if __name__ == "__main__":
    main()
