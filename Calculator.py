import os
import math

def calculate(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif op == '^':
        return num1 ** num2
    elif op == 'sqrt':
        return math.sqrt(num1)
    elif op == 'sin':
        return math.sin(math.radians(num1))
    elif op == 'cos':
        return math.cos(math.radians(num1))
    elif op == 'tan':
        return math.tan(math.radians(num1))
    else:
        return "Error: Invalid operation"

def save_to_history(history, result):
    with open('calc_history.txt', 'a') as file:
        file.write(f"{history} = {result}\n")

def display_history():
    try:
        with open('calc_history.txt', 'r') as file:
            history = file.read()
            if history:
                print("\nCalculation History:")
                print(history)
            else:
                print("\nNo calculation history.")
    except FileNotFoundError:
        print("\nNo calculation history.")

def clear_history():
    try:
        os.remove('calc_history.txt')
        print("\nCalculation history cleared.")
    except FileNotFoundError:
        print("\nNo calculation history to clear.")

def print_supported_operations():
    print("\nSupported Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Square Root (sqrt)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")

def main():
    print("Welcome to the Advanced Calculator")

    while True:
        print("\nOptions:")
        print("1. Perform Calculation")
        print("2. Use Previous Result from History")
        print("3. View Calculation History")
        print("4. Clear Calculation History")
        print("5. Display Supported Operations")
        print("6. Exit")

        choice = input("Enter your choice (1, 2, 3, 4, 5, or 6): ")

        if choice == '1':
            # Get user input for calculation
            expression = input("\nEnter the expression or 'back' to go back: ")

            if expression == 'back':
                continue

            try:
                result = eval(expression)
            except (SyntaxError, NameError, ZeroDivisionError) as e:
                print(f"Error: {e}")
                continue

            print(f"\nExpression: {expression}")
            print(f"Result: {result}")

            # Save to history
            save_to_history(expression, result)

        elif choice == '2':
            # Use Previous Result from History
            display_history()

            try:
                # Prompt the user to select a previous result from history
                selection = int(input("\nEnter the number of the result to use: "))
                with open('calc_history.txt', 'r') as file:
                    lines = file.readlines()
                    if 1 <= selection <= len(lines):
                        # Extract the selected calculation from history
                        selected_calculation = lines[selection - 1].strip().split('=')
                        history_expression = selected_calculation[0].strip()
                        previous_result = float(selected_calculation[1].strip())
                        print(f"Using previous result: {history_expression} = {previous_result}")
                    else:
                        print("Invalid selection. Please enter a valid number.")
                        continue
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            # Prompt for a new expression with the previous result
            expression = input("Enter the new expression or 'back' to go back: ")

            if expression == 'back':
                continue

            try:
                result = eval(expression)
            except (SyntaxError, NameError, ZeroDivisionError) as e:
                print(f"Error: {e}")
                continue

            print(f"\nExpression: {expression}")
            print(f"Result: {result}")

            # Save to history
            save_to_history(expression, result)

        elif choice == '3':
            # View Calculation History
            display_history()

        elif choice == '4':
            # Clear Calculation History
            clear_history()

        elif choice == '5':
            # Display Supported Operations
            print_supported_operations()

        elif choice == '6':
            # Exit
            print("Thank you for using the Advanced Calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")

if __name__ == "__main__":
    if not os.path.exists('calc_history.txt'):
        with open('calc_history.txt', 'w'):
            pass
    main()
