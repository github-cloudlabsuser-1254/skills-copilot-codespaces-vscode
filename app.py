def calculator():
    """
    A simple calculator function that allows users to perform basic arithmetic operations.

    The calculator provides the following operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Percentage calculation
    6. Exit the calculator

    The function runs in a loop, allowing users to perform multiple calculations until they choose to exit.

    How it works:
    - The user selects an operation by entering a number corresponding to the desired operation.
    - For operations 1 to 4, the user is prompted to input two numbers.
    - For the percentage operation (5), the user is prompted to input one number, and the result is calculated as the percentage of the input number.
    - The function handles invalid inputs gracefully by displaying error messages and prompting the user to try again.
    - Division by zero is explicitly checked and handled to prevent runtime errors.

    Note:
    - The function exits when the user selects option 6.
    - Input validation is implemented to ensure numeric values are entered where required.
    """
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Percentage")
        print("6. Exit")

        try:
            choice = int(input("Enter choice (1/2/3/4/5/6): "))

            if choice in [1, 2, 3, 4, 5]:
                try:
                    num1 = float(input("Enter first number: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    try:
                        num2 = float(input("Enter second number: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        continue
                if choice == 5:
                    print(f"The result is: {num1 / 100}")
                else:
                    num2 = float(input("Enter second number: "))

                    if choice == 1:
                        print(f"The result is: {num1 + num2}")
                    elif choice == 2:
                        print(f"The result is: {num1 - num2}")
                    elif choice == 3:
                        print(f"The result is: {num1 * num2}")
                    elif choice == 4:
                        if num2 != 0:
                            print(f"The result is: {num1 / num2}")
                        else:
                            print("Error: Division by zero is not allowed.")
            elif choice == 6:
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("Invalid input. Please select a valid operation.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()