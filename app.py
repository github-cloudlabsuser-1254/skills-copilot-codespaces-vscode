# Simple Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return None

def percentage(a, b):
    if b != 0:
        return (a / b) * 100
    else:
        return "Error! Division by zero."

def calculator():
    """
    A simple calculator function that allows the user to perform basic arithmetic operations.

    The user can select from the following operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Percentage calculation

    The function prompts the user to input their choice of operation and two numeric values.
    It then performs the selected operation and displays the result.

    Exceptions:
    - Handles invalid numeric input by displaying an error message.
    - Displays an error message for invalid operation choices.

    Returns:
    - None
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        if choice == '1':
            result = add(num1, num2)
            print(f"The result is: {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result is: {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result is: {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result is: {result}")
        elif choice == '5':
            result = percentage(num1, num2)
            print(f"The result is: {result}%")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
        elif choice == '5':
            print(f"The result is: {percentage(num1, num2)}%")
    else:
        print("Invalid input. Please try again.")

# Run the calculator
calculator()