#https://github.com/AmberNguyen249/lab10-AN-AW.git
#Partner 1:Amber Nguyen
#Partner 2:Aster Wang
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

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