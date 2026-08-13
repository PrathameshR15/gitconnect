import unittest
from calculator import (
    add, subtract, multiply, divide,
    power, modulo, square,
    square_root, factorial, absolute_value,
)


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), "Error! Division by zero.")

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(5, 0), "Error! Division by zero.")

    def test_square(self):
        self.assertEqual(square(3), 9)
        self.assertEqual(square(-4), 16)

    # --- New tests for advanced operations ---

    def test_square_root(self):
        self.assertEqual(square_root(25), 5.0)
        self.assertEqual(square_root(0), 0.0)
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)
        self.assertEqual(
            square_root(-1),
            "Error! Cannot compute square root of a negative number.",
        )

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(
            factorial(-3),
            "Error! Factorial is only defined for non-negative integers.",
        )

    def test_absolute_value(self):
        self.assertEqual(absolute_value(5), 5)
        self.assertEqual(absolute_value(-5), 5)
        self.assertEqual(absolute_value(0), 0)
        self.assertAlmostEqual(absolute_value(-3.14), 3.14)

    def test_dummy(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
