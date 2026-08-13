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


def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")
        if choice.lower() == 'q':
            break
            
        if choice in ('1', '2', '3', '4'):
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
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
