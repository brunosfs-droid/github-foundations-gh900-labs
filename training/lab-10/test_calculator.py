"""Testes automáticos usando a biblioteca padrão do Python."""
import unittest
from calculator import add, divide


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_zero_divisor(self):
        with self.assertRaises(ValueError):
            divide(1, 0)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(10, 0), 10)

    def test_divide_decimal(self):
        self.assertAlmostEqual(divide(5, 2), 2.5)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0.0)

if __name__ == "__main__":
    unittest.main()
