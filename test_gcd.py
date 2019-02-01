from unittest import TestCase
from math_functions import q02


class TestGcd(TestCase):
    def test_gcd_smallest_case(self):
        self.assertEqual(1, q02.gcd(1, 1))

    def test_gcd_general_case(self):
        self.assertEqual(5, q02.gcd(45, 25))

    def test_gcd_both_negatives(self):
        self.assertEqual(5, q02.gcd(-45, -25))

    def test_gcd_negative_a(self):
        self.assertEqual(5, q02.gcd(-45, 25))

    def test_gcd_negative_b(self):
        self.assertEqual(5, q02.gcd(45, -25))

    def test_gcd_zeroes(self):
        with self.assertRaises(Exception):
            q02.gcd(0, 0)

    def test_gcd_zero_a(self):
        with self.assertRaises(Exception):
            q02.gcd(0, 10)

    def test_gcd_zero_b(self):
        with self.assertRaises(Exception):
            q02.gcd(10, 0)

    def test_gcd_primes(self):
        self.assertEqual(1, q02.gcd(17, 29))
