# Description: Write a Python program to get a newly-generated string from a given string.
# Add "Is" to the front of the inputted string
# Return the string unchanged if the given string already begins with "Is".
# Date: 12th June 2024

def main():
    result = generate_new_string()
    print(result)


def generate_new_string():
    """
    Generate a new string from a given string by adding "Is" to the front of the inputted string.

    If the given string already begins with "Is", return the string unchanged.

    Returns:
        str: The generated string or a message indicating the validity of the input string.
    """
    string_value = input("Please type in a word: ").strip()
    new_string = "Is" + string_value
    if string_value.startswith("Is"):
        return f"{string_value} is valid"
    elif string_value.startswith("is"):
        return string_value.capitalize()
    else:
        return f"{string_value} is invalid. Here is a valid string => '{new_string}'"


if __name__ == "__main__":
    main()
