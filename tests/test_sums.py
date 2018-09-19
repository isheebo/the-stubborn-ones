import unittest

from app.sums import recursive_sum


class TestRecursiveSum(unittest.TestCase):
    def test_works_for_one_nested_level(self):
        self.assertEqual(
            recursive_sum([1, 2, 3, [4, 5, 6]]),
            21
        )
        self.assertEqual(
            recursive_sum([[4, 5, 6], 1, 2, 3]),
            21
        )

        self.assertEqual(
            recursive_sum([1, 2, 3, [4, 5, 6], 4]),
            25
        )

    def test_works_for_two_nested_levels(self):
        self.assertEqual(recursive_sum(
            [1, 2, 7, 8, [5, 6, 10], 2, [6, 8]]), 55)

    def test_works_for_3_nested_levels(self):
        self.assertEqual(recursive_sum(
            [5, 1, 34, 6, [2, 3, 4, [6, 7, 8, 19], 6, 2, 6, 4], 5, 12]), 130)
