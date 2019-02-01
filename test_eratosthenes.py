from unittest import TestCase
from math_functions import q01


class TestEratosthenes(TestCase):
    def test_eratosthenes_general_case(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], q01.eratosthenes(30))

    def test_eratosthenes_smallest_case(self):
        self.assertEqual([2], q01.eratosthenes(3))

    def test_eratosthenes_smallest_case_with_no_result(self):
        self.assertEqual([], q01.eratosthenes(1))

    def test_eratosthenes_zero(self):
        with self.assertRaises(TypeError):
            q01.eratosthenes(0)

    def test_eratosthenes_negative(self):
        with self.assertRaises(TypeError):
            q01.eratosthenes(-1)

    def test_eratosthenes_float(self):
        with self.assertRaises(TypeError):
            q01.eratosthenes(10.5)

    def test_eratosthenes_negative_float(self):
        with self.assertRaises(TypeError):
            q01.eratosthenes(-10.5)

    def test_eratosthenes_empty(self):
        with self.assertRaises(TypeError):
            q01.eratosthenes()

    def test_eratosthenes_string(self):
        with self.assertRaises(TypeError):
            q01.eratosthenes('a')
