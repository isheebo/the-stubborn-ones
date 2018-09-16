import unittest

from app.factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial_zero_equal_one(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_5_equal_120(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_works_not_with_neg_values(self):
        self.assertEqual(factorial(-2), 0)
