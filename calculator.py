def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y

def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulo")
    print("7. View History")
    
    history = []
    
    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7) or 'q' to quit: ")
        if choice.lower() == 'q':
            break
            
        if choice == '7':
            if not history:
                print("No history yet.")
            else:
                print("\n--- Calculation History ---")
                for entry in history:
                    print(entry)
                print("---------------------------\n")
            continue

        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            result = ""
            if choice == '1':
                result = f"{num1} + {num2} = {add(num1, num2)}"
            elif choice == '2':
                result = f"{num1} - {num2} = {subtract(num1, num2)}"
            elif choice == '3':
                result = f"{num1} * {num2} = {multiply(num1, num2)}"
            elif choice == '4':
                result = f"{num1} / {num2} = {divide(num1, num2)}"
            elif choice == '5':
                result = f"{num1} ^ {num2} = {power(num1, num2)}"
            elif choice == '6':
                result = f"{num1} % {num2} = {modulo(num1, num2)}"
            
            print(result)
            history.append(result)
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
