# test_utils.py — unittest suite for utils.py
import unittest

import utils


class TestUtils(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(utils.is_even(2))
        self.assertTrue(utils.is_even(0))
        self.assertFalse(utils.is_even(3))

    def test_to_title(self):
        self.assertEqual(utils.to_title("ada lovelace"), "Ada Lovelace")
        self.assertEqual(utils.to_title("grace hopper"), "Grace Hopper")
        self.assertEqual(utils.to_title("ALAN turing"), "Alan Turing")

    def test_safe_divide_normal(self):
        self.assertEqual(utils.safe_divide(10, 2), 5)

    def test_safe_divide_by_zero(self):
        self.assertIsNone(utils.safe_divide(10, 0))

    def test_average(self):
        self.assertAlmostEqual(utils.average([2, 4, 6]), 4.0)
        self.assertAlmostEqual(utils.average([10]), 10.0)

    def test_average_empty(self):
        self.assertIsNone(utils.average([]))

    def test_first_last(self):
        self.assertEqual(utils.first_last([1, 2, 3, 4]), (1, 4))
        self.assertEqual(utils.first_last(["a"]), ("a", "a"))
        self.assertEqual(utils.first_last([]), (None, None))

    def test_count_vowels(self):
        self.assertEqual(utils.count_vowels("Ada Lovelace"), 6)   # A a o e a e
        self.assertEqual(utils.count_vowels("PYTHON"), 1)         # O
        self.assertEqual(utils.count_vowels("rhythm"), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
