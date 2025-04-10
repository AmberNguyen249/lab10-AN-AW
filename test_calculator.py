# https://github.com/AmberNguyen249/lab10-AN-AW.git
# Partner 1:Amber Nguyen
# Partner 2:Aster Wang
import unittest
from calculator import *


def multiply(param, param1):
    pass


def divide(param, param1):
    pass


class TestCalculator(unittest.TestCase):
    ######### Partner 2

    def test_add(a, b):
        return a + b

    def test_subtract(a, b):
        return a - b
    # ##########################

# << << << < HEAD


######## Partner 1

class TestMathFunctions(unittest.TestCase):

    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-2, 5), -10)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(2, 10), 5)  # 10 / 2
        self.assertEqual(divide(5, 0), 0)  # 0 / 5
        with self.assertRaises(ZeroDivisionError):
            divide(0, 10)

# == == == =

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

# ##########################
# >> >> >> > dbbbb7ff8728499d086d65a0c210cf176b90042d


######## Partner 2
def test_divide_by_zero(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return b / a
    except ZeroDivisionError as e:
        print(f"Error in divide: {e}")
    with self.assertRaises(ZerroDivisionError):
        div(0, 5)


def test_logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive.")
    return math.log(b, a)


def test_log_invalid_base(a, b):
    try:
        if a <= 0 or a == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1.")
        if b <= 0:
            raise ValueError("Logarithm argument must be positive.")
        return math.log(b, a)
    except ValueError as e:
        print(f"Error in logarithm: {e}")
        raise

    ######## Partner 1


class TestMathFunctions(unittest.TestCase):

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)
        from math import isclose
        self.assertTrue(isclose(hypotenuse(-5, 12), 13))

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-4)

        self.assertEqual(square_root(0), 0)
        from math import isclose
        self.assertTrue(isclose(square_root(9), 3))


# Do not touch this
if __name__ == "__main__":
    unittest.main()
