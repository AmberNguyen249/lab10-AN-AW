# https://github.com/AmberNguyen249/lab10-AN-AW.git
# Partner 1: Amber Nguyen
# Partner 2: Aster Wang

import unittest
import math



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(x)

def logarithm(base, value):
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    if value <= 0:
        raise ValueError("Logarithm argument must be positive.")
    return math.log(value, base)



class TestCalculator(unittest.TestCase):

    # Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(10, 10), 0)

    # Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(0, 5), 0)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_logarithm(self):
        self.assertTrue(math.isclose(logarithm(10, 1000), 3))
        with self.assertRaises(ValueError):
            logarithm(1, 100)  # base = 1 not allowed
        with self.assertRaises(ValueError):
            logarithm(-2, 100)
        with self.assertRaises(ValueError):
            logarithm(2, -100)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)
        self.assertTrue(math.isclose(hypotenuse(-5, 12), 13))

    def test_square_root(self):
        self.assertEqual(square_root(0), 0)
        self.assertTrue(math.isclose(square_root(9), 3))
        with self.assertRaises(ValueError):
            square_root(-4)

    def test_log_invalid_base(self):
        self.assertTrue(math.isclose(logarithm(10, 1000), 3))
        with self.assertRaises(ValueError):
            logarithm(1, 100)
        with self.assertRaises(ValueError):
            logarithm(-2, 100)
        with self.assertRaises(ValueError):
            logarithm(2, -100)

    def test_divide_by_zero(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(0, 5), 0)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_log_invalid_argument(self):
        self.assertTrue(math.isclose(logarithm(10, 1000), 3))
        with self.assertRaises(ValueError):
            logarithm(1, 100)  # base = 1 not allowed
        with self.assertRaises(ValueError):
            logarithm(-2, 100)
        with self.assertRaises(ValueError):
            logarithm(2, -100)
        

if __name__ == "__main__":
    unittest.main()
