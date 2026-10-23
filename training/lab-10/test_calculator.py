"""Testes automáticos usando a biblioteca padrão do Python."""
import unittest

from calculator import add, divide


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(2, -3), -1)

    def test_add_basic_properties(self):
        self.assertEqual(add(4, 7), add(7, 4))  # comutatividade
        self.assertEqual(add(0, 9), 9)          # identidade
        self.assertEqual(add(9, 0), 9)          # identidade
        self.assertEqual(add(add(2, 3), 4), add(2, add(3, 4)))  # associatividade

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_decimal_result(self):
        self.assertAlmostEqual(divide(5, 2), 2.5)
        self.assertAlmostEqual(divide(7, 4), 1.75)
        self.assertAlmostEqual(divide(-9, 2), -4.5)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(0, -5), 0)

    def test_zero_divisor(self):
        with self.assertRaises(ValueError):
            divide(1, 0)
        with self.assertRaises(ValueError):
            divide(-1, 0)


if __name__ == "__main__":
    unittest.main()
