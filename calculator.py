#https://github.com/AmberNguyen249/lab10-AN-AW.git
#Partner 1:Amber Nguyen
#Partner 2:Aster Wang
"""calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)
    except ValueError as e:
        print(f"Error in square_root: {e}")
        raise

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        print(f"Unexpected error in hypotenuse: {e}")
        raise

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return b / a
    except ZeroDivisionError as e:
        print(f"Error in divide: {e}")
        raise

def logarithm(a, b):
    try:
        if a <= 0 or a == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1.")
        if b <= 0:
            raise ValueError("Logarithm argument must be positive.")
        return math.log(b, a)
    except ValueError as e:
        print(f"Error in logarithm: {e}")
        raise

def exp(a, b):
    return a ** b


