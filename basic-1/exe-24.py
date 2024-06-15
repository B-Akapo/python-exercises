# Description: Write a Python program to test whether a passed letter is a vowel or not.
# Date: 15th June 2024

def main():
    """Main function of the program to interact with the user and display results."""
    answer_entered, result = check_value_entered()
    if result is not None:
        if result:
            print(f"{answer_entered} is a vowel")
        else:
            print(f"'{answer_entered}' is not a vowel")
    else:
        print("Invalid input: Please enter only a single alphabetic character.")


def check_value_entered():
    """Function to validate user input and check if it is a vowel."""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    answer_entered = input("Please enter a single alphabetic character: ")
    if len(answer_entered) == 1 and answer_entered.isalpha():
        if answer_entered in vowels:
            return answer_entered, True  # Return the character and True if it's a vowel
        else:
            return answer_entered, False  # Return the character and False if it's alphabetic but not a vowel
    else:
        return answer_entered, None  # Return the character and None if it doesn't meet the criteria


if __name__ == "__main__":
    main()
