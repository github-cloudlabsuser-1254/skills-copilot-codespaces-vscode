// Simple Calculator Program

// Function to perform addition
function add(a, b) {
    return a + b;
}

// Function to perform subtraction
function subtract(a, b) {
    return a - b;
}

// Function to perform multiplication
function multiply(a, b) {
    return a * b;
}

// Function to perform division
function divide(a, b) {
    if (b === 0) {
        return "Error! Division by zero.";
    }
    return a / b;
}

// Main calculator function
function calculator() {
    console.log("Welcome to the Calculator!");
    console.log("Select an operation:");
    console.log("1. Add");
    console.log("2. Subtract");
    console.log("3. Multiply");
    console.log("4. Divide");

    const choice = parseInt(prompt("Enter your choice (1/2/3/4): "));

    if ([1, 2, 3, 4].includes(choice)) {
        const num1 = parseFloat(prompt("Enter the first number: "));
        const num2 = parseFloat(prompt("Enter the second number: "));

        let result;
        switch (choice) {
            case 1:
                result = add(num1, num2);
                console.log(`The result is: ${result}`);
                break;
            case 2:
                result = subtract(num1, num2);
                console.log(`The result is: ${result}`);
                break;
            case 3:
                result = multiply(num1, num2);
                console.log(`The result is: ${result}`);
                break;
            case 4:
                result = divide(num1, num2);
                console.log(`The result is: ${result}`);
                break;
        }
    } else {
        console.log("Invalid choice. Please restart the program and try again.");
    }
}

// Run the calculator
calculator();