# Description: Write a Python program to test whether a number is within 100 of 1000 or 2000.
# Date: 12th June 2024

def main():
    number = get_positive_integer()
    result = check_value(number)
    print(result)


def get_positive_integer():
    while True:
        try:
            number = int(input("Pleas enter a number: "))
            if number <= 0:
                print("Please enter a positive number!! ")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def check_value(number):
    if 900 <= number <= 1100 or 1900 <= number <= 2100:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
