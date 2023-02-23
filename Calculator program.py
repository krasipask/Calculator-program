import sys

# function to add two numbers
def add(a, b):
    return a + b

# function to subtract two numbers
def subtract(a, b):
    return a - b

# function to multiply two numbers
def multiply(a, b):
    return a * b

# function to divide two numbers
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        sys.exit()

# function to format the result
def format_result(result):
    if result.is_integer():
        return int(result)
    else:
        return round(result, 2)

# main function
def calculator():
    while True:
        print("Select operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice (1/2/3/4): ")

        # validate the user's choice
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input")
            continue

        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        # validate the user's inputs
        if not (num1.isnumeric() and num2.isnumeric()):
            print("Error: invalid input")
            continue

        num1 = float(num1)
        num2 = float(num2)

        if choice == '1':
            result = add(num1, num2)
            op = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            op = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            op = "*"
        elif choice == '4':
            result = divide(num1, num2)
            op = "/"

        # format the result
        result = format_result(result)
        print(f"{num1} {op} {num2} = {result}")

        # ask the user if they want to do another calculation
        choice = input("Would you like to do a new calculation? (yes/no): ")
        if choice.lower() == "no":
            sys.exit()

# run the calculator
calculator()