import unittest
from my_decimales_a_romanos import decimal_to_roman
class MyTest(unittest.TestCase):

    def test_I(self):
        self.assertEqual(decimal_to_roman(1), "I")

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, "X")

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, "II")

    def test_cien(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, 'C')

    def test_ciento_uno(self):
        resultado = decimal_to_roman(101)
        self.assertEqual(resultado, 'CI')

    def test_ciento_tres(self):
        resultado = decimal_to_roman(103)
        self.assertEqual(resultado, 'CIII')

    def test_ciento_cinco(self):
        resultado = decimal_to_roman(105)
        self.assertEqual(resultado, 'CV')

    def test_ciento_diez(self):
        resultado = decimal_to_roman(110)
        self.assertEqual(resultado, 'CX')

    def test_docientos_tres(self):
        resultado = decimal_to_roman(203)
        self.assertEqual(resultado, 'CCIII')

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, "III")
    
    def test_cuatro(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, "IV")

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, "V")

    def test_seis(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, "VI")

    def test_siete(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, "VII")

    def test_ocho(self):
        resultado = decimal_to_roman(8)
        self.assertEqual(resultado, "VIII")

    def test_nueve(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, "IX")

    def test_once(self):
        resultado = decimal_to_roman(11)
        self.assertEqual(resultado, "XI")
        
if __name__ == "__main__":
    unittest.main()