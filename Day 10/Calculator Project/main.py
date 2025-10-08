import os
import art
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_exit(value):
    """Exit the program if user types 'esc'."""
    if value.lower().strip() == "esc":
        clear()
        print("Calculator exited. Goodbye!")
        sys.exit()

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def get_number(prompt):
    while True:
        value = input(prompt)
        check_exit(value)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number, or type 'esc' to exit.")

def get_operator():
    while True:
        operator = input("Enter your operator (+, -, *, /): ").strip()
        check_exit(operator)
        if operator in ["+", "-", "*", "/"]:
            return operator
        print("Invalid operator. Please enter +, -, *, /, or type 'esc' to exit.")

def calc():
    clear()
    print(art.logo)
    n1 = get_number("Enter your first number: ")
    keep_going = True

    while keep_going:
        result = None
        operator = get_operator()
        n2 = get_number("Enter your next number: ")

        if operator == "+":
            result = add(n1, n2)
        elif operator == "-":
            result = subtract(n1, n2)
        elif operator == "*":
            result = multiply(n1, n2)
        elif operator == "/":
            result = divide(n1, n2)

        print(f"{n1:g} {operator} {n2:g} = {result:g}")

        while True:
            choice = input(f"Type 'y' to continue with {result:g}, 'n' for new calculation, or 'esc' to exit: ").lower().strip()
            check_exit(choice)
            if choice == "y":
                n1 = result
                break
            elif choice == "n":
                clear()
                print("\nRestarting calculator...\n")
                calc()
                return
            else:
                print("Please enter 'y', 'n', or 'esc'.")

calc()
