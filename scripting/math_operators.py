# math operators for simple_calc.py

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
