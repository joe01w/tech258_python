# Simple Calc functions

# import math_operators
from math_operators import add, minus, multiply, divide


def calculator():
    choice = input("Select: +, -, *, / :")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == "+":
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == "-":
        print(num1, "-", num2, "=", minus(num1, num2))
    elif choice == "*":
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == "/":
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Error")

calculator()
