# basic calculator functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Can't divide by zero")
    return a / b


# REPL loop — runs when you execute this file directly
if __name__ == "__main__":
    print("Simple Calculator")
    print("Type 'quit' to exit\n")

    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op == "quit":
            break
        if op not in ["+", "-", "*", "/"]:
            print("Invalid operation, try again\n")
            continue

        a = float(input("First number: "))
        b = float(input("Second number: "))

        if op == "+":
            print(f"Answer: {add(a, b)}\n")
        elif op == "-":
            print(f"Answer: {subtract(a, b)}\n")
        elif op == "*":
            print(f"Answer: {multiply(a, b)}\n")
        elif op == "/":
            try:
                print(f"Answer: {divide(a, b)}\n")
            except ValueError as e:
                print(f"Error: {e}\n")