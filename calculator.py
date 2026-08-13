import math


def add(x, y):
    """Return the sum of *x* and *y*.
    
    Simple arithmetic addition.
    """
    return x + y

def subtract(x, y):
    """Return the difference of *x* minus *y*.
    """
    return x - y

def multiply(x, y):
    """Return the product of *x* and *y*.
    """
    return x * y

def divide(x, y):
    """Return *x* divided by *y*.
    
    If *y* is zero, returns an error string.
    """
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    """Return *x* raised to the power of *y*.
    """
    return x ** y


def modulo(x, y):
    """Return the modulo of *x* by *y*.
    If *y* is zero, returns an error string.
    """
    if y == 0:
        return "Error! Division by zero."
    return x % y


def square(x):
    """Return the square of *x* (i.e., *x* × *x*).
    """
    return x * x


def square_root(x):
    """Return the square root of *x*.

    If *x* is negative, returns an error string.
    """
    if x < 0:
        return "Error! Cannot compute square root of a negative number."
    return math.sqrt(x)


def factorial(n):
    """Return the factorial of non-negative integer *n*.

    If *n* is negative or not an integer, returns an error string.
    """
    if not isinstance(n, int) or n < 0:
        return "Error! Factorial is only defined for non-negative integers."
    return math.factorial(n)


def absolute_value(x):
    """Return the absolute value of *x*.
    """
    return abs(x)


def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulo")
    print("7. Square")
    print("8. Square Root")
    print("9. Factorial")
    print("10. Absolute Value")

    two_operand_choices = ('1', '2', '3', '4', '5', '6')
    one_operand_choices = ('7', '8', '9', '10')

    while True:
        choice = input("Enter choice (1-10) or 'q' to quit: ")
        if choice.lower() == 'q':
            break

        if choice in two_operand_choices:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '6':
                print(f"{num1} % {num2} = {modulo(num1, num2)}")

        elif choice in one_operand_choices:
            try:
                num = float(input("Enter number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '7':
                print(f"square({num}) = {square(num)}")
            elif choice == '8':
                print(f"sqrt({num}) = {square_root(num)}")
            elif choice == '9':
                print(f"factorial({int(num)}) = {factorial(int(num))}")
            elif choice == '10':
                print(f"abs({num}) = {absolute_value(num)}")
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
