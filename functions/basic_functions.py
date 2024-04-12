# Functions

# DRY - Don't Repeat Yourself

# basic function

def print_something(name):
    print("Hello, my name is " + name)

print_something("Joe")

# function with arguments

def addition(int1, int2):
    return int1 + int2

print(addition(2, 2))
print(addition(10, 15))

# default arguments

def addition(int1=2, int2=2):
    return int1 + int2

print(addition())
print(addition(10, 15))

# multiple arguments
def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)

multi_args(1, 2, 4, 6, 7)
multi_args(1, 2)

# type hints
def division(denom:int, num: int) -> float:
    return denom / num

print(division(5, 3))
