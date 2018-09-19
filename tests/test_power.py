import unittest

from app.power import powers


class TestPower(unittest.TestCase):
    def test_works_for_pos_base_and_pos_exp(self):
        self.assertEqual(powers(2, 4), 16)
        self.assertEqual(powers(2, 3), 8)

    def test_works_for_neg_base_pos_exp(self):
        self.assertEqual(powers(-2, 3), -8)
        self.assertEqual(powers(-2, 4), 16)

    def test_works_for_pos_base_neg_exp(self):
        self.assertEqual(powers(2, -3), 0.125)
        self.assertEqual(powers(2, -4), 0.0625)

    def test_works_for_neg_base_neg_exp(self):
        self.assertEqual(powers(-2, -3), -0.125)
        self.assertEqual(powers(-2, -4), 0.0625)

    def test_returns_one_for_exp_equal_zero(self):
        self.assertEqual(powers(2, 0), 1)
        self.assertEqual(powers(0, 0), 1)

    def test_returns_base_for_exp_equal_one(self):
        self.assertEqual(powers(2, 1), 2)
        self.assertEqual(powers(0, 1), 0)
