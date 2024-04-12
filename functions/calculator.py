# Simple Calculator

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error, you cannot divide by zero."
    else:
        return x / y

def calculator():
    choice = input("Select: +, -, *, / :")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '+':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '-':
        print(num1, "-", num2, "=", minus(num1, num2))
    elif choice == '*':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '/':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Error")

calculator()