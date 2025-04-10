#https://github.com/AmberNguyen249/lab10-AN-AW.git
#Partner 1:Amber Nguyen
#Partner 2:Aster Wang
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
   
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
     def divide(a, b):
        try:
            if a == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return b / a
        except ZeroDivisionError as e:
            print(f"Error in divide: {e}")
            with self.assertRaises(ZerroDivisionError):
                div(0, 5)

     def logarithm(a, b):
        if a <= 0 or a == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1.")
        if b <= 0:
            raise ValueError("Logarithm argument must be positive.")
        return math.log(b, a)

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
    
    ######## Partner 1

    class TestMathFunctions(unittest.TestCase):

        def test_log_invalid_argument(self):
            with self.assertRaises(ValueError):
                logarithm(0, 5)  # Invalid base

        def test_hypotenuse(self):
            self.assertEqual(hypotenuse(3, 4), 5)
            self.assertEqual(hypotenuse(0, 0), 0)
            from math import isclose
            self.assertTrue(isclose(hypotenuse(-5, 12), 13))

        def test_sqrt(self):
            with self.assertRaises(ValueError):
                square_root(-4)  # Invalid input

            self.assertEqual(square_root(0), 0)
            from math import isclose
            self.assertTrue(isclose(square_root(9), 3))


# Do not touch this
if __name__ == "__main__":
    unittest.main()
