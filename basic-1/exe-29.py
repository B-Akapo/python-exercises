# Description: Write a Python program that prints out all colors from one list that are not present in the second.
# Date: 15th June 2024

def main():
    # Define the color lists
    color_list_1 = {"White", "Black", "Red"}
    color_list_2 = {"Red", "Green"}

    # Call the function to get the unique colors from the first list
    result = get_unique_colors(color_list_1, color_list_2)

    # Print the result
    print(result)


def get_unique_colors(list1, list2):
    """
    Returns a list of colors that are in list1 but not in list2.

    Args:
        list1 (set): First set of colors.
        list2 (set): Second set of colors.

    Returns:
        list: List of colors that are in list1 but not in list2.
    """
    # Use set difference to find colors in list1 that are not in list2
    unique_colors = list1 - list2

    # Convert the set to a list to print
    return list(unique_colors)


if __name__ == "__main__":
    main()
