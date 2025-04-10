#https://github.com/AmberNguyen249/lab10-AN-AW.git
#Partner 1:Amber Nguyen
#Partner 2:Aster Wang
import unittest
from calculator import *


def multiply(param, param1):
    pass


def divide(param, param1):
    pass

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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