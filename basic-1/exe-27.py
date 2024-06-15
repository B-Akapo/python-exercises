# Description: Write a Python program that concatenates all elements in a list into a string and returns it.
# Date: 15th June 2024

from typing import List


def main():
    my_list = [1, 5, 12, 2]
    result = concatenate_string(my_list)
    print(result)


def concatenate_string(my_list: List[int]) -> str:
    """
    Concatenates all elements in a list into a single string.

    Args:
        my_list (List[int]): List of integers to concatenate.

    Returns:
        str: Concatenated string of all list elements.
    """
    # Convert all elements to strings and concatenate them
    return ''.join(map(str, my_list))


if __name__ == '__main__':
    main()
