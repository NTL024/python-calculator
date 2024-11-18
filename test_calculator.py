import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_1(self):
        self.assertEqual(self.calc.add(2, 4), 6)
    
    def test_add_2(self):
        self.assertEqual(self.calc.add(-5, 8), 3)

    def test_subtract_1(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_2(self):
        self.assertEqual(self.calc.subtract(-2, -1), -1)

    def test_multiply_1(self):
        self.assertEqual(self.calc.multiply(5, -4), -20)

    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(-5, -2), 10)

    def test_divide_1(self):
        self.assertEqual(self.calc.divide(-20, -4), 5)

    def test_divide_2(self):
        self.assertEqual(self.calc.divide(12, 4), 3)

    def test_modulo_1(self):
        self.assertEqual(self.calc.modulo(9, 4), 1)

    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(12, 5), 2)


if __name__ == '__main__':
    unittest.main()