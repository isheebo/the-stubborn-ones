import unittest
from app.is_prime import is_prime


class TestIsPrimeNumber(unittest.TestCase):
    def test_is_prime_works(self):
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(5))

    def test_fails_for_pseudo_primes(self):
        self.assertFalse(is_prime(600059))
        self.assertFalse(is_prime(989))

    def test_does_nums_below_2(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(0))

    def test_fails_for_composites(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
