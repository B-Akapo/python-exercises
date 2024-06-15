# Description: Write a Python program that determines whether a given number (accepted from the user) is even or odd,
# and prints an appropriate message to the user.
# Date: 15th June 2024

def main():
    number = get_number()
    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


def get_number():
    while True:
        user_input = input("Please enter a number: ")
        try:
            x = int(user_input)
            return x
        except ValueError:
            print("That's not a valid number. Please try again.")


def is_even(num):
    return num % 2 == 0


if __name__ == "__main__":
    main()
