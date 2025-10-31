import unittest, calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(7, 2), 5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(calculator.divide(10, 0))

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)

    def test_average_of_three(self):
        self.assertAlmostEqual(calculator.average([2, 4, 6]), 4.0)

    def test_average_single_item(self):
        self.assertEqual(calculator.average([10]), 10.0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
