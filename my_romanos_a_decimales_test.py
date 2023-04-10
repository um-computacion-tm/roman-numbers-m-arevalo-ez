import unittest
from my_romanos_a_decimales import roman_to_decimal
class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal("I")
        self.assertEqual(resultado, 1)

    def test_II(self):
        resultado = roman_to_decimal("II")
        self.assertEqual(resultado, 2)

    def test_III(self):
        resultado = roman_to_decimal("III")
        self.assertEqual(resultado, 3)

    def test_IV(self):
        resultado = roman_to_decimal("IV")
        self.assertEqual(resultado, 4)

    def test_V(self):
        resultado = roman_to_decimal("V")
        self.assertEqual(resultado, 5)

    def test_VIII(self):
        resultado = roman_to_decimal("VIII")
        self.assertEqual(resultado, 8)

    def test_IX(self):
        resultado = roman_to_decimal("IX")
        self.assertEqual(resultado, 9)

    def test_X(self):
        resultado = roman_to_decimal("X")
        self.assertEqual(resultado, 10)

    def test_XIII(self):
        resultado = roman_to_decimal("XIII")
        self.assertEqual(resultado, 13)

    def test_XIV(self):
        resultado = roman_to_decimal("XIV")
        self.assertEqual(resultado, 14)

    def test_XXVII(self):
        resultado = roman_to_decimal("XXVII")
        self.assertEqual(resultado, 27)

    def test_LXXIII(self):
        resultado = roman_to_decimal("LXXIII")
        self.assertEqual(resultado, 73)

    def test_CXXXIX(self):
        resultado = roman_to_decimal("CXXXIX")
        self.assertEqual(resultado, 139)

    def test_CDLXVIII(self):
        resultado = roman_to_decimal("CDLXVIII")
        self.assertEqual(resultado, 468)

    def test_DCCLXXXIX(self):
        resultado = roman_to_decimal("DCCLXXXIX")
        self.assertEqual(resultado, 789)

    def test_MCMLXXXIV(self):
        resultado = roman_to_decimal("MCMLXXXIV")
        self.assertEqual(resultado, 1984)
if __name__ == "__main__":
    unittest.main()