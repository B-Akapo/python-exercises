# Description: Write a  Python program that will accept the base and height of a triangle and compute its area.
# Date: 15th June 2024

def main():
    """
    Main function to execute the program.
    - Obtains base and height from user input.
    - Calculates area of the triangle using calculate_area function.
    - Displays the computed area along with the base and height.
    """
    base, height = get_the_positive_value()  # Call function to get base and height
    area = calculate_area(base, height)      # Call function to calculate area
    print(f"The area of the triangle with base {base} and height {height} is {area}.")


def get_the_positive_value():
    """
    Function to prompt the user to enter positive integers for the base and height of the triangle.
    Keeps prompting until valid inputs are provided.
    Returns:
    - x: Base of the triangle (positive integer).
    - y: Height of the triangle (positive integer).
    """
    while True:
        try:
            x = int(input("Please enter the value of the base of the triangle: "))   # Prompt for base input
            y = int(input("Please enter the value of the height of the triangle: "))  # Prompt for height input
            if x <= 0 or y <= 0:  # Check if inputs are not positive
                print("Please enter a positive number.")  # Prompt user to enter positive numbers
            else:
                return x, y  # Return valid base and height
        except ValueError:
            print("Not a valid number. Please enter an integer.")  # Handle non-integer input


def calculate_area(x, y):
    """
    Function to calculate the area of a triangle given its base and height.
    Formula used: area = 0.5 * base * height
    Parameters:
    - x: Base of the triangle.
    - y: Height of the triangle.
    Returns:
    - area: Computed area of the triangle.
    """
    area = 0.5 * x * y  # Calculate area using the formula
    return area  # Return the calculated area


if __name__ == "__main__":
    main()  # Call the main function to start the program
